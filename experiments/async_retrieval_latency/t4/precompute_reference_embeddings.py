#!/usr/bin/env python
"""Precompute MoshiRAG reference embeddings once and cache them on disk.

The T4 sweep then injects these cached tensors and never loads the reference encoder, so the
encoder never shares the GPU with the LM. Run this as its own process; when it exits, all of
its GPU memory is released.

This mirrors ``moshi.server_conditioner.EncoderService`` (same config subset, same weight
sources and load order, same ``encode()``), with one change to fit a 16 GB GPU:
``ArcEncoderTransformer`` / ``EmbProjector`` are built on the ``meta`` device and the
checkpoint is assigned into them tensor by tensor. The official service first allocates
randomly initialised fp32 weights on the GPU (12.1 GB) and then loads another 12.1 GB copy.

Hardware note: the official encoder autocasts to bfloat16. T4 (sm_75) has no bf16 tensor
cores, and xformers' attention kernels need sm_80 for bf16, so ``--autocast auto`` uses
float16 there. Embeddings computed on a T4 are therefore not bit-identical to ones computed on
an A100. The autocast dtype is stored in each cache file. For exact parity, run this script on
an A100 (bf16) and copy the cache directory.

    python experiments/async_retrieval_latency/t4/precompute_reference_embeddings.py \
        --manifest experiments/async_retrieval_latency/configs/samples.jsonl \
        --cache-dir /content/drive/MyDrive/moshirag_t4/reference_cache

Needs Hugging Face access to the gated meta-llama/Llama-3.2-3B-Instruct tokenizer.
"""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import logging
import sys
import time
from pathlib import Path

T4_DIR = Path(__file__).resolve().parent
REPO_ROOT = T4_DIR.parents[2]
sys.path[:0] = [str(REPO_ROOT / "moshi"), str(T4_DIR), str(T4_DIR.parent / "scripts")]

from reference_cache import cache_path, read_cache_header, reference_sha256  # noqa: E402

CONDITIONER = "reference_with_time"
logger = logging.getLogger("precompute_reference")


def load_texts(manifests: list[Path]) -> list[str]:
    from run_latency_sweep import load_manifest  # stdlib-only module

    texts: list[str] = []
    for m in manifests:
        samples, errors = load_manifest(m.resolve())
        if errors:
            raise SystemExit("\n".join(errors))
        for s in samples:
            if s["reference_text"] not in texts:
                texts.append(s["reference_text"])
    return texts


def build_encoder(hf_repo: str, device: str, autocast: str, weights_dtype: str):
    import torch
    from safetensors import safe_open

    from moshi.conditioners import ConditionProvider
    from moshi.conditioners.arc_encoder import ArcEncoderTransformer, EmbProjector, MultiArcEncoderConditioner
    from moshi.models import loaders

    class LowMemoryArcConditioner(MultiArcEncoderConditioner):
        """Same conditioner, but the 3B encoder is created on ``meta`` and filled by assignment."""

        def _init_modules(self):
            with torch.device("meta"):
                self.embedder = ArcEncoderTransformer(compression_rate=self.compression_rate)
                self.bridge_module = EmbProjector(
                    in_dim=self.bridge_module_params["in_dim"],
                    out_dim=self.bridge_module_params["out_dim"],
                    hidden_dim=self.bridge_module_params["hidden_dim"],
                )
            self.embedder.eval()
            self.bridge_module.eval()

    info = loaders.CheckpointInfo.from_hf_repo(hf_repo)
    lm_config = copy.deepcopy(info.raw_config)
    for key in ["moshi_name", "mimi_name", "mimi_config_name", "tokenizer_name", "lora_name", "model_type",
                "lm_gen_config", "tts_config", "stt_config", "model_id"]:
        lm_config.pop(key, None)
    # Same as server_conditioner.subset_lm_config_conditioners(lm_config, CONDITIONER).
    lm_config["conditioners"] = {CONDITIONER: lm_config["conditioners"][CONDITIONER]}
    lm_config["fuser"] = {k: ([x for x in v if x == CONDITIONER] if isinstance(v, list) else v)
                          for k, v in lm_config["fuser"].items()}
    cond_cfg = lm_config["conditioners"][CONDITIONER]
    assert cond_cfg["type"] == "multi_arc_encoder", cond_cfg["type"]
    kwargs = dict(cond_cfg["multi_arc_encoder"])
    kwargs.update({"output_dim": lm_config["dim"], "device": device})

    if autocast == "auto":
        major, _ = torch.cuda.get_device_capability(device) if device.startswith("cuda") else (8, 0)
        autocast = "bfloat16" if major >= 8 else "float16"
    kwargs["autocast_dtype"] = None if autocast == "none" else autocast

    cond = LowMemoryArcConditioner(**kwargs)
    hf_repo_arc = kwargs.get("hf_repo")

    # 1) Conditioner weights stored in the MoshiRAG checkpoint (output_proj, learnt_padding),
    #    copied into the fp32 parameters like EncoderService._load_from_checkpoint (strict=False).
    prefix = f"condition_provider.conditioners.{CONDITIONER}."
    with safe_open(str(info.moshi_weights), framework="pt", device="cpu") as f:
        state = {k[len(prefix):]: f.get_tensor(k).to(device) for k in f.keys() if k.startswith(prefix)}
    if not state:
        raise RuntimeError(f"no '{prefix}*' tensors in {info.moshi_weights}")
    cond.load_state_dict(state, strict=False)

    # 2) ARC encoder + bridge from kyutai/ARC4_Encoder_Llama, assigned like load_weights().
    from huggingface_hub import hf_hub_download

    arc_path = hf_hub_download(hf_repo_arc, "model.safetensors")
    target = getattr(torch, weights_dtype)
    with safe_open(arc_path, framework="pt", device="cpu") as f:
        arc_state = {k: f.get_tensor(k).to(device=device, dtype=target) for k in f.keys()}
    result = cond.load_state_dict(arc_state, assign=True, strict=False)
    del arc_state
    left_on_meta = [n for n, t in list(cond.named_parameters()) + list(cond.named_buffers()) if t.is_meta]
    if left_on_meta:
        raise RuntimeError(f"encoder tensors not loaded: {left_on_meta[:10]}")
    logger.info("ARC weights assigned (%d unexpected keys ignored)", len(result.unexpected_keys))

    provider = ConditionProvider({CONDITIONER: cond}, device=device)
    fuser = loaders.get_condition_fuser(lm_config)
    provenance = {
        "hf_repo": hf_repo,
        "moshi_weights": str(info.moshi_weights),
        "arc_repo": hf_repo_arc,
        "arc_weights": arc_path,
        "autocast_dtype": autocast,
        "weights_dtype": weights_dtype,
        "device": torch.cuda.get_device_name(device) if device.startswith("cuda") else device,
        "torch": torch.__version__,
    }
    return provider, fuser, provenance


def encode(provider, fuser, text: str):
    """Same as moshi.server_conditioner.EncoderService.encode for a streaming_sum conditioner."""
    from moshi.conditioners import ConditionAttributes

    prepared = provider.prepare([ConditionAttributes(text={CONDITIONER: text}, tensor={})])
    condition_tensors = provider(prepared)
    assert fuser.cond2fuse[CONDITIONER] == "streaming_sum"
    return fuser.get_streaming_sum(condition_tensors)  # [1, T, dim]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--manifest", type=Path, nargs="+", required=True)
    p.add_argument("--cache-dir", type=Path, required=True)
    p.add_argument("--hf-repo", type=str, default="kyutai/moshika-rag-pytorch-bf16")
    p.add_argument("--device", type=str, default="cuda:0")
    p.add_argument("--autocast", choices=["auto", "bfloat16", "float16", "none"], default="auto",
                   help="auto = bfloat16 on sm_80+ (as the official encoder), float16 on older GPUs.")
    p.add_argument("--weights-dtype", choices=["float32", "float16"], default="float32",
                   help="float32 = as the official encoder (12.1 GB); float16 halves memory (deviation).")
    p.add_argument("--overwrite", action="store_true")
    args = p.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")

    texts = load_texts(args.manifest)
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    todo = [t for t in texts if args.overwrite or not cache_path(args.cache_dir, t).is_file()]
    logger.info("%d distinct references, %d to encode, cache: %s", len(texts), len(todo), args.cache_dir)
    if not todo:
        return 0

    import torch
    from safetensors.torch import save_file

    torch.set_grad_enabled(False)
    t0 = time.monotonic()
    provider, fuser, provenance = build_encoder(args.hf_repo, args.device, args.autocast, args.weights_dtype)
    if args.device.startswith("cuda"):
        logger.info("encoder loaded in %.0fs; GPU allocated %.2f GB (peak %.2f GB)", time.monotonic() - t0,
                    torch.cuda.memory_allocated() / 1e9, torch.cuda.max_memory_allocated() / 1e9)
    for text in todo:
        emb = encode(provider, fuser, text)
        tensor = emb.squeeze(0).contiguous().cpu()
        path = cache_path(args.cache_dir, text)
        metadata = {k: str(v) for k, v in provenance.items()} | {
            "reference_text": text,
            "reference_sha256": reference_sha256(text),
            "shape": json.dumps(list(tensor.shape)),
            "dtype": str(tensor.dtype),
            "created": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        }
        tmp = path.with_suffix(".tmp")
        save_file({"embedding": tensor}, str(tmp), metadata=metadata)
        tmp.replace(path)
        logger.info("cached %s: shape %s (%s)", path.name, tuple(tensor.shape), text[:60])
    for text in texts:
        read_cache_header(cache_path(args.cache_dir, text), expected_text=text)  # validates every file
    logger.info("done; all %d references cached", len(texts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
