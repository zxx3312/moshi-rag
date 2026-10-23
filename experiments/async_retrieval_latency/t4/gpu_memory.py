"""GPU memory logging: one JSON line per event in RUN_DIR/logs/gpu_memory.jsonl."""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

import torch

logger = logging.getLogger(__name__)
MB = 1024 * 1024


def snapshot(device: str | torch.device) -> dict[str, Any]:
    if not torch.cuda.is_available():
        return {}
    free, total = torch.cuda.mem_get_info(device)
    return {
        # PyTorch caching allocator (tensors only).
        "allocated_mb": round(torch.cuda.memory_allocated(device) / MB, 1),
        "reserved_mb": round(torch.cuda.memory_reserved(device) / MB, 1),
        "peak_allocated_mb": round(torch.cuda.max_memory_allocated(device) / MB, 1),
        "peak_reserved_mb": round(torch.cuda.max_memory_reserved(device) / MB, 1),
        # Whole device as the driver sees it (includes CUDA context, cuBLAS/bitsandbytes workspaces).
        "device_used_mb": round((total - free) / MB, 1),
        "device_total_mb": round(total / MB, 1),
    }


class GpuMemoryLog:
    def __init__(self, path: Path, device: str | torch.device):
        self.path = path
        self.device = device

    def log(self, event: str, **extra: Any) -> dict[str, Any]:
        snap = snapshot(self.device)
        record = {"time": round(time.time(), 3), "event": event, **snap, **extra}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
        if snap:
            logger.info("[GPU] %-28s allocated %8.1f MB | reserved %8.1f MB | peak %8.1f MB | device %8.1f / %.0f MB",
                        event, snap["allocated_mb"], snap["reserved_mb"], snap["peak_allocated_mb"],
                        snap["device_used_mb"], snap["device_total_mb"])
        return record
