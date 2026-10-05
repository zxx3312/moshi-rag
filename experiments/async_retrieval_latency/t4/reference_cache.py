"""Cache of precomputed reference embeddings, one safetensors file per distinct reference text.

Stdlib only (header parsing), so ``--dry-run`` can validate the cache without importing torch.
"""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path
from typing import Any


def reference_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def cache_path(cache_dir: Path, text: str) -> Path:
    return Path(cache_dir) / f"ref_{reference_sha256(text)[:16]}.safetensors"


def read_cache_header(path: Path, expected_text: str | None = None) -> dict[str, Any]:
    """Validate a cache file from its header alone and return its metadata."""
    if not path.is_file():
        raise FileNotFoundError(f"reference embedding not cached: {path}")
    size = path.stat().st_size
    with path.open("rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(n))
    meta = header.pop("__metadata__", {}) or {}
    if set(header) != {"embedding"}:
        raise ValueError(f"{path}: expected a single 'embedding' tensor, got {sorted(header)}")
    info = header["embedding"]
    if 8 + n + info["data_offsets"][1] != size:
        raise ValueError(f"{path}: truncated file")
    if len(info["shape"]) != 2:
        raise ValueError(f"{path}: expected shape [T, dim], got {info['shape']}")
    if expected_text is not None:
        if meta.get("reference_sha256") != reference_sha256(expected_text):
            raise ValueError(f"{path}: cached for a different reference text")
    return {"shape": info["shape"], "dtype": info["dtype"], **meta}
