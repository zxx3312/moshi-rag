import os
os.environ["HF_HUB_OFFLINE"] = "1"

from pathlib import Path
import torch
from moshi.models import loaders

if not torch.cuda.is_available():
    raise SystemExit("No GPU available. Run this inside the allocated GPU session.")

device = "cuda"
folder = Path.home() / "models" / "moshika-rag-pytorch-bf16"

print("GPU:", torch.cuda.get_device_name(0), flush=True)

checkpoint = loaders.CheckpointInfo.from_hf_repo(
    "kyutai/moshika-rag-pytorch-bf16",
    moshi_weights=folder / "model.safetensors",
    mimi_weights=folder / "tokenizer-e351c8d8-checkpoint125.safetensors",
    tokenizer=folder / "tokenizer_spm_32k_3.model",
    config_path=folder / "config.json",
)

with torch.inference_mode():
    print("Loading Moshi...", flush=True)
    model = checkpoint.get_moshi(
        device=device,
        dtype=torch.bfloat16,
        skip_conditioners=["reference_with_time"],
    )
    missing = [name for name, p in model.named_parameters() if p.is_meta]
    if missing:
        raise RuntimeError(f"Parameters were not loaded: {missing[:10]}")
    print("Moshi loaded.", flush=True)

    print("Loading Mimi...", flush=True)
    mimi = checkpoint.get_mimi(device=device)
    wav = torch.zeros(1, 1, 24000, device=device)
    codes = mimi.encode(wav)
    audio = mimi.decode(codes)
    torch.cuda.synchronize()

print("Audio shape:", tuple(audio.shape))
print("GPU memory used (GiB):",
      round(torch.cuda.memory_allocated() / 1024**3, 2))
print("SMOKE TEST PASSED")
