"""CPU checks of the q8 loading logic on a *tiny, randomly initialised* MoshiRAG-shaped LM.

Run (no GPU, no real weights, a few seconds):
    python experiments/async_retrieval_latency/t4/tests/test_q8_cpu.py

The tiny checkpoint uses the real checkpoint's key layout: fused ``self_attn.in_proj_weight`` /
``out_proj.weight``, per-step depformer gating, bf16 storage, and extra
``reference_with_time`` conditioner tensors. What these tests cannot show: speed or memory on a
real GPU, CUDA-graph behaviour, or how quantization affects the real model's outputs.
"""

from __future__ import annotations

import copy
import sys
import tempfile
from pathlib import Path

import torch

HERE = Path(__file__).resolve()
T4_DIR = HERE.parents[1]
REPO = HERE.parents[4]
sys.path[:0] = [str(REPO / "moshi"), str(T4_DIR)]

from safetensors.torch import save_file  # noqa: E402

from moshi.models import LMGen  # noqa: E402
from moshi.models.loaders import CheckpointInfo, get_moshi_lm  # noqa: E402
from moshi.utils.quantize import QLinear, replace_linear_with_qlinear  # noqa: E402

from q8_moshirag import build_lm_gen, lm_config_without_reference, load_q8_lm  # noqa: E402

TINY = {
    "card": 64, "n_q": 16, "dep_q": 8,
    "delays": [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    "dim": 64, "text_card": 100, "existing_text_padding_id": 3, "rag_token_id": 4,
    "num_heads": 4, "num_layers": 2, "hidden_scale": 4.125, "causal": True, "layer_scale": None,
    "context": 100, "max_period": 10000, "gating": "silu", "norm": "rms_norm_f32",
    "positional_embedding": "rope", "depformer_dim": 32, "depformer_num_heads": 4,
    "depformer_num_layers": 2, "depformer_dim_feedforward": None, "depformer_multi_linear": True,
    "depformer_pos_emb": "none", "depformer_weights_per_step": True, "demux_second_stream": False,
    "text_card_out": None, "cross_attention": False,
    "conditioners": {
        "first_speaker": {"type": "lut", "lut": {"n_bins": 2, "dim": 16, "tokenizer": "noop",
                                                  "possible_values": ["SPEAKER_MAIN", "SPEAKER_OTHER"]}},
        # Placeholder: only used to check that the loader removes it (never instantiated).
        "reference_with_time": {"type": "multi_arc_encoder", "multi_arc_encoder": {}},
    },
    "fuser": {"sum": [], "streaming_sum": ["reference_with_time"], "prepend": ["first_speaker"], "cross": []},
}


def _fuse_attention_keys(state: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
    """Turn per-step ``in_projs.{i}.weight`` back into the checkpoint's fused layout."""
    out, groups = {}, {}
    for k, v in state.items():
        for kind, fused in (("in_projs", "in_proj_weight"), ("out_projs", "out_proj.weight")):
            marker = f".self_attn.{kind}."
            if marker in k:
                base, idx = k.split(marker)[0], int(k.split(marker)[1].split(".")[0])
                groups.setdefault(f"{base}.self_attn.{fused}", {})[idx] = v
                break
        else:
            out[k] = v
    for k, parts in groups.items():
        out[k] = torch.cat([parts[i] for i in sorted(parts)], 0)
    return out


def make_checkpoint(tmp: Path, cfg: dict | None = None) -> CheckpointInfo:
    torch.manual_seed(0)
    full_cfg = copy.deepcopy(cfg or TINY)
    cfg = lm_config_without_reference(full_cfg)
    dense = get_moshi_lm(None, lm_kwargs=cfg, device="cpu", dtype=torch.float32)
    state = {k: v.to(torch.bfloat16) if v.dtype.is_floating_point else v for k, v in dense.state_dict().items()}
    state = _fuse_attention_keys(state)
    assert any(k.endswith("self_attn.in_proj_weight") for k in state), "fused layout expected"
    state["condition_provider.conditioners.reference_with_time.output_proj.weight"] = torch.randn(64, 64).bfloat16()
    state["condition_provider.conditioners.reference_with_time.learnt_padding"] = torch.randn(1, 1, 64).bfloat16()
    path = tmp / "model.safetensors"
    save_file({k: v.contiguous() for k, v in state.items()}, str(path))
    return CheckpointInfo(moshi_weights=path, mimi_weights=path, tokenizer=path,
                          lm_config=copy.deepcopy(full_cfg), raw_config=copy.deepcopy(full_cfg))


def reference_q8(info: CheckpointInfo, dtype: torch.dtype):
    """What the repo does: load the dense model with get_moshi_lm, then replace_linear_with_qlinear."""
    model = get_moshi_lm(info.moshi_weights, lm_kwargs=lm_config_without_reference(info.lm_config),
                         device="cpu", dtype=dtype)
    replace_linear_with_qlinear(model)
    return model


def test_repo_q8_load_path(tmp: Path, info: CheckpointInfo) -> str:
    """Export a q8 checkpoint like scripts/export_quantized.py, then load it the repo's way
    (config quantize=True through get_moshi_lm). Returns a description of what happens."""
    exported = reference_q8(info, torch.bfloat16)
    q8_path = tmp / "model.q8.safetensors"
    save_file({k: v.contiguous() for k, v in exported.state_dict().items()}, str(q8_path))
    cfg = lm_config_without_reference(info.lm_config) | {"quantize": True}
    try:
        model = get_moshi_lm(q8_path, lm_kwargs=cfg, device="cpu", dtype=torch.float16)
    except Exception as e:  # noqa: BLE001
        return f"get_moshi_lm(quantize=True) failed while loading: {type(e).__name__}: {e}"
    scales = {m.weight_scb.dtype for m in model.modules() if isinstance(m, QLinear)}
    try:
        lm_gen = LMGen(model, cfg_coef=1.0, force_streaming_sum=True)
        lm_gen.streaming_forever(1)
        lm_gen.step(torch.zeros(1, 8, 1, dtype=torch.long))
        return f"loaded and stepped without error (scale dtypes {scales})"
    except Exception as e:  # noqa: BLE001
        return f"loaded with scale dtypes {scales}, then forward failed: {type(e).__name__}: {e}"


def test_q8_weights_identical(info: CheckpointInfo) -> None:
    ref = reference_q8(info, torch.float16)
    mine = load_q8_lm(info, device="cpu", dtype=torch.float16, quantize=True)
    ref_sd, my_sd = ref.state_dict(), mine.state_dict()
    assert ref_sd.keys() == my_sd.keys(), set(ref_sd) ^ set(my_sd)
    for k in ref_sd:
        assert ref_sd[k].dtype == my_sd[k].dtype, (k, ref_sd[k].dtype, my_sd[k].dtype)
        assert torch.equal(ref_sd[k], my_sd[k]), k
    n_q = sum(isinstance(m, QLinear) for m in mine.modules())
    n_lin = sum(type(m) is torch.nn.Linear for m in mine.modules())
    assert n_q > 0 and n_lin == 0, (n_q, n_lin)
    assert all(m.weight_scb.dtype == torch.float32 for m in mine.modules() if isinstance(m, QLinear))
    print(f"  ok: {len(my_sd)} tensors bit-identical to get_moshi_lm + replace_linear_with_qlinear "
          f"({n_q} QLinear, 0 nn.Linear left)")


def _generate(model, info, steps: int = 12) -> list[int]:
    torch.manual_seed(1234)
    lm_gen = build_lm_gen(model, info, init_active_speaker="user")
    lm_gen.streaming_forever(1)
    g = torch.Generator().manual_seed(7)
    text = []
    for _ in range(steps):
        codes = torch.randint(0, 64, (1, lm_gen.needed_tokens, 1), generator=g)
        out = lm_gen.step(codes)
        if out is not None:
            text.append(int(out[0, 0, 0]))
    return text


def test_generation_identical(info: CheckpointInfo) -> None:
    ref = _generate(reference_q8(info, torch.float16), info)
    mine = _generate(load_q8_lm(info, device="cpu", dtype=torch.float16, quantize=True), info)
    assert ref == mine and len(mine) > 0, (ref, mine)
    print(f"  ok: LMGen sampling ({len(mine)} steps, same seed) gives identical text tokens")


def test_unquantized_streaming_load(info: CheckpointInfo) -> None:
    ref = get_moshi_lm(info.moshi_weights, lm_kwargs=lm_config_without_reference(info.lm_config),
                       device="cpu", dtype=torch.float16)
    mine = load_q8_lm(info, device="cpu", dtype=torch.float16, quantize=False)
    ref_sd, my_sd = ref.state_dict(), mine.state_dict()
    assert ref_sd.keys() == my_sd.keys()
    assert all(torch.equal(ref_sd[k], my_sd[k]) and ref_sd[k].dtype == my_sd[k].dtype for k in ref_sd)
    print(f"  ok: quantize=False streaming load equals get_moshi_lm ({len(my_sd)} tensors)")


def main() -> int:
    torch.set_grad_enabled(False)
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        info = make_checkpoint(tmp)
        print("[1] repo q8 path (export_quantized.py output loaded via get_moshi_lm, quantize=True):")
        print("   ", test_repo_q8_load_path(tmp, info))
        print("[2] streaming q8 loader vs repo quantizer:")
        test_q8_weights_identical(info)
        print("[3] generation:")
        test_generation_identical(info)
        print("[4] streaming loader without quantization:")
        test_unquantized_streaming_load(info)
    print("ALL CPU CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
