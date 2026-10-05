"""Low-memory int8 (q8) loader for the MoshiRAG LM, for single 16 GB GPUs such as a T4.

Why not the repo's own q8 path:
- ``kyutai/moshika-rag-pytorch-bf16`` ships no pre-quantized ``model.q8.safetensors``.
  ``scripts/export_quantized.py`` would make one, but it first builds the full bf16 model
  (15.4 GB) plus the in-process ARC encoder (12.1 GB) on the GPU, which a T4 cannot hold.
- ``models.loaders.get_moshi_lm`` casts every floating tensor outside ``condition_provider.`` /
  ``fuser.`` to the model dtype, including each ``*.weight_scb`` scale. ``QLinear.forward``
  raises when the scale is not float32, so loading an exported q8 checkpoint through it fails
  (checked on a tiny model in ``tests/test_q8_cpu.py``).

What this loader does instead (same building blocks as the repo):
1. Builds ``LMModel`` on the ``meta`` device, exactly as ``get_moshi_lm`` does, from the repo's
   config with the ``reference_with_time`` conditioner removed (identical to ``get_moshi``'s
   ``skip_conditioners`` when ``REFERENCE_ENCODER_URL`` is set).
2. Reads the bf16 checkpoint lazily, one transformer layer at a time, applying the same dtype
   rule as ``get_moshi_lm`` and the attention ``_load_hook`` (via ``load_state_dict``).
3. Quantizes each layer right after loading it with ``moshi.utils.quantize.replace_linear_with_qlinear``
   (bitsandbytes ``int8_vectorwise_quant`` of the fp16 weight), so peak GPU memory is
   ~one fp16 layer on top of the int8 model. Then it quantizes the remaining ``nn.Linear``
   modules, which is the same set ``export_quantized.py`` / ``LMModel(quantize=True)`` quantize.

The int8 weights are bit-identical to what ``replace_linear_with_qlinear`` produces on the fully
loaded model (also checked in ``tests/test_q8_cpu.py``). Quantization itself still changes the
model's numerics: q8 MoshiRAG is a different condition from bf16 MoshiRAG.
"""

from __future__ import annotations

import copy
import logging
from typing import Any, Callable

import torch
from safetensors import safe_open
from torch import nn

from moshi.inference_utils.utils import get_condition_tensors
from moshi.models import LMGen, LMModel
from moshi.models.loaders import CheckpointInfo, get_condition_fuser, get_conditioner_provider
from moshi.utils.quantize import QLinear, replace_linear_with_qlinear

logger = logging.getLogger(__name__)

REFERENCE_CONDITIONER = "reference_with_time"
LAYER_STACKS = ("transformer", "depformer")


def lm_config_without_reference(lm_config: dict[str, Any]) -> dict[str, Any]:
    """Copy of the LM config with the reference conditioner removed (the precomputed
    embedding is injected through ``LMGen.update_streaming_sum_tensors`` instead)."""
    cfg = copy.deepcopy(lm_config)
    cfg.get("conditioners", {}).pop(REFERENCE_CONDITIONER, None)
    for key, value in (cfg.get("fuser") or {}).items():
        if isinstance(value, list) and REFERENCE_CONDITIONER in value:
            cfg["fuser"][key] = [v for v in value if v != REFERENCE_CONDITIONER]
    return cfg


def _target_dtype(key: str, value: torch.Tensor, dtype: torch.dtype) -> torch.dtype:
    # Same rule as moshi.models.loaders.get_moshi_lm.
    if not value.dtype.is_floating_point:
        return value.dtype
    if key.startswith("condition_provider.") or key.startswith("fuser."):
        return torch.float32
    return dtype


def _meta_tensors(module: nn.Module) -> list[str]:
    return [n for n, t in list(module.named_parameters()) + list(module.named_buffers()) if t.is_meta]


def load_q8_lm(
    checkpoint_info: CheckpointInfo,
    device: str | torch.device,
    dtype: torch.dtype = torch.float16,
    quantize: bool = True,
    on_stage: Callable[[str], None] | None = None,
) -> LMModel:
    """Build the MoshiRAG LM without the reference conditioner, int8-quantized layer by layer."""
    assert checkpoint_info.lm_config is not None, "MoshiRAG needs its config.json"
    if checkpoint_info.lora_weights is not None:
        raise RuntimeError("LoRA checkpoints are not supported by the q8 loader")
    lm_kwargs = lm_config_without_reference(checkpoint_info.lm_config)
    if lm_kwargs.pop("quantize", False):
        raise RuntimeError("expected a bf16 checkpoint, got a config with quantize=True")

    # --- same preprocessing as get_moshi_lm ---
    if "conditioners" in lm_kwargs:
        lm_kwargs["condition_provider"] = get_conditioner_provider(lm_kwargs["dim"], device, lm_kwargs)
        del lm_kwargs["conditioners"]
    if lm_kwargs.get("fuser", None) is not None:
        lm_kwargs["fuser"] = get_condition_fuser(lm_kwargs)
    lm_kwargs.pop("depformer_causal", None)
    if "demux_second_stream" in lm_kwargs:
        lm_kwargs["demux_second_text_stream"] = lm_kwargs.pop("demux_second_stream")
    if lm_kwargs.pop("lora", False):
        raise RuntimeError("LoRA configs are not supported by the q8 loader")
    lm_kwargs.pop("lora_rank", None)
    lm_kwargs.pop("lora_scaling", None)

    model = LMModel(device=torch.device("meta"), dtype=dtype, **lm_kwargs)
    if on_stage:
        on_stage("lm_skeleton_on_meta")

    consumed: set[str] = set()
    with safe_open(str(checkpoint_info.moshi_weights), framework="pt", device="cpu") as f:
        # The removed reference conditioner's tensors live in the precomputed embedding instead
        # (get_moshi's skip_conditioners ignores them the same way, via strict=False).
        skip_prefix = f"condition_provider.conditioners.{REFERENCE_CONDITIONER}."
        keys = [k for k in f.keys() if not k.startswith(skip_prefix)]
        logger.info("q8 loader: %d tensors to load, %d reference-conditioner tensors skipped",
                    len(keys), sum(k.startswith(skip_prefix) for k in f.keys()))

        def read(prefix: str) -> dict[str, torch.Tensor]:
            out = {}
            for k in keys:
                if k.startswith(prefix) and k not in consumed:
                    t = f.get_tensor(k)
                    out[k[len(prefix):]] = t.to(device=device, dtype=_target_dtype(k, t, dtype))
                    consumed.add(k)
            return out

        for stack_name in LAYER_STACKS:
            stack = getattr(model, stack_name, None)
            if stack is None:
                continue
            for i, layer in enumerate(stack.layers):
                prefix = f"{stack_name}.layers.{i}."
                # strict=True: every parameter of the layer must come from the checkpoint
                # (the attention _load_hook maps the fused in_proj/out_proj keys).
                layer.load_state_dict(read(prefix), assign=True, strict=True)
                if quantize:
                    replace_linear_with_qlinear(layer)
            if on_stage:
                on_stage(f"{stack_name}_layers_loaded{'_q8' if quantize else ''}")

        rest = read("")
        result = model.load_state_dict(rest, assign=True, strict=False)
        if result.unexpected_keys:
            raise RuntimeError(f"unexpected checkpoint keys: {result.unexpected_keys[:10]}")

    unread = [k for k in keys if k not in consumed]
    if unread:
        raise RuntimeError(f"checkpoint keys not loaded: {unread[:10]}")
    meta = _meta_tensors(model)
    if meta:
        raise RuntimeError(f"tensors left uninitialized (still on meta): {meta[:10]}")

    if quantize:
        # Remaining nn.Linear (text_linear, depformer_in, linears, conditioner projections),
        # i.e. the same set as LMModel(quantize=True). Existing QLinear scales are kept float32.
        replace_linear_with_qlinear(model)
        bad_scales = [n for n, m in model.named_modules() if isinstance(m, QLinear) and m.weight_scb.dtype != torch.float32]
        if bad_scales:
            raise RuntimeError(f"QLinear scales not float32: {bad_scales[:5]}")
    model.eval()
    if on_stage:
        on_stage("lm_loaded")
    return model


def build_lm_gen(
    lm: LMModel, checkpoint_info: CheckpointInfo, init_active_speaker: str
) -> LMGen:
    """Same LMGen construction as moshi.inference_utils.utils.load_models."""
    condition_tensors = get_condition_tensors(
        model_type="moshi",
        lm=lm,
        batch_size=1,
        cfg_coef=1.0,
        reference_text=None,
        first_speaker=init_active_speaker,
    )
    return LMGen(
        lm,
        cfg_coef=1.0,
        condition_tensors=condition_tensors,
        force_streaming_sum=True,
        **checkpoint_info.lm_gen_config,
    )


def count_linear_types(model: nn.Module) -> dict[str, int]:
    return {
        "QLinear": sum(isinstance(m, QLinear) for m in model.modules()),
        "nn.Linear": sum(type(m) is nn.Linear for m in model.modules()),
    }
