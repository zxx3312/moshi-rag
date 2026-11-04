"""Train the LoRA judge on B's SFT data (b_work/step4/sft) with a small base model.

    python a_work/train_lora_judge.py --train sft_train.jsonl --dev sft_dev.jsonl --out DIR

The SFT records carry A's few-shot examples. They are dropped here: the same example replies would be
learned 2,000 times, and the LoRA judge does not need them at inference. Examples longer than --max-len
are dropped, never truncated, so a label cannot lose the evidence it refers to. Loss covers the final
assistant reply only, and the prompt comes from the chat template the vLLM server applies at inference.
"""
import argparse
import json
import math
import random
import time
from pathlib import Path
from typing import List, Optional

IGNORE = -100


def strip_examples(messages: List[dict]) -> List[dict]:
    """system + final user + final assistant; the turns in between are the few-shot examples."""
    return messages[:1] + messages[-2:]


def load_examples(path, limit: Optional[int] = None) -> List[List[dict]]:
    rows = [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    if limit is not None:
        rows = rows[:limit]
    return [strip_examples(r["messages"]) for r in rows]


def encode(messages: List[dict], tokenizer, max_len: int, end_token: str = "<|im_end|>"):
    """(input_ids, labels) with the prompt masked, or None if too long."""
    prompt = tokenizer.apply_chat_template(messages[:-1], tokenize=False, add_generation_prompt=True,
                                           enable_thinking=False)
    prompt_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    target_ids = tokenizer(messages[-1]["content"] + end_token, add_special_tokens=False)["input_ids"]
    if len(prompt_ids) + len(target_ids) > max_len:
        return None
    return prompt_ids + target_ids, [IGNORE] * len(prompt_ids) + target_ids


def batches(items: list, size: int, pad_id: int, rng: Optional[random.Random] = None):
    """Yield padded (input_ids, labels, attention_mask) lists; similar lengths batch together when shuffled."""
    order = list(range(len(items)))
    if rng is not None:
        rng.shuffle(order)
        pools = [order[i:i + size * 50] for i in range(0, len(order), size * 50)]
        order = [i for pool in pools for i in sorted(pool, key=lambda k: len(items[k][0]))]
    chunks = [order[i:i + size] for i in range(0, len(order), size)]
    if rng is not None:
        rng.shuffle(chunks)
    for chunk in chunks:
        width = max(len(items[i][0]) for i in chunk)
        ids, labels, mask = [], [], []
        for i in chunk:
            a, b = items[i]
            gap = width - len(a)
            ids.append(a + [pad_id] * gap)
            labels.append(b + [IGNORE] * gap)
            mask.append([1] * len(a) + [0] * gap)
        yield ids, labels, mask


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="Qwen/Qwen3-4B")
    ap.add_argument("--train", type=Path, required=True)
    ap.add_argument("--dev", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--max-len", type=int, default=4096)
    ap.add_argument("--epochs", type=int, default=3)
    ap.add_argument("--batch-size", type=int, default=2)
    ap.add_argument("--grad-accum", type=int, default=4)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--rank", type=int, default=16)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--max-train", type=int, default=None, help="Smoke test: only the first N examples.")
    ap.add_argument("--max-dev", type=int, default=None)
    args = ap.parse_args()

    import torch
    from peft import LoraConfig, get_peft_model
    from transformers import AutoModelForCausalLM, AutoTokenizer

    random.seed(args.seed)
    torch.manual_seed(args.seed)
    args.out.mkdir(parents=True, exist_ok=True)
    tokenizer = AutoTokenizer.from_pretrained(args.base)
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id

    def prepare(path, limit):
        raw = load_examples(path, limit)
        encoded = [encode(m, tokenizer, args.max_len) for m in raw]
        kept = [e for e in encoded if e is not None]
        return kept, len(raw) - len(kept)

    train, train_dropped = prepare(args.train, args.max_train)
    dev, dev_dropped = prepare(args.dev, args.max_dev)
    print(f"train {len(train)} (dropped {train_dropped} over {args.max_len} tokens), dev {len(dev)} (dropped {dev_dropped})",
          flush=True)

    model = AutoModelForCausalLM.from_pretrained(args.base, dtype=torch.bfloat16).cuda()
    model.config.use_cache = False
    model.gradient_checkpointing_enable()
    model.enable_input_require_grads()
    model = get_peft_model(model, LoraConfig(
        r=args.rank, lora_alpha=2 * args.rank, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"]))
    model.print_trainable_parameters()

    optimizer = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=args.lr, weight_decay=0.0)
    steps_per_epoch = math.ceil(math.ceil(len(train) / args.batch_size) / args.grad_accum)
    total_steps = steps_per_epoch * args.epochs
    scheduler = torch.optim.lr_scheduler.LambdaLR(
        optimizer, lambda s: min(1.0, (s + 1) / max(1, total_steps // 20)) * max(0.0, 1 - s / max(1, total_steps)))

    def forward(ids, labels, mask):
        with torch.autocast("cuda", dtype=torch.bfloat16):
            return model(input_ids=torch.tensor(ids).cuda(), labels=torch.tensor(labels).cuda(),
                         attention_mask=torch.tensor(mask).cuda()).loss

    def dev_loss():
        model.eval()
        total, n = 0.0, 0
        with torch.no_grad():
            for ids, labels, mask in batches(dev, args.batch_size, pad_id):
                total += forward(ids, labels, mask).item() * len(ids)
                n += len(ids)
        model.train()
        return total / max(1, n)

    rng = random.Random(args.seed)
    log, best = [], float("inf")
    model.train()
    start = time.time()
    for epoch in range(1, args.epochs + 1):
        optimizer.zero_grad()
        running, count = 0.0, 0
        all_batches = list(batches(train, args.batch_size, pad_id, rng))
        for i, (ids, labels, mask) in enumerate(all_batches, 1):
            loss = forward(ids, labels, mask)
            (loss / args.grad_accum).backward()
            running += loss.item()
            count += 1
            if i % args.grad_accum == 0 or i == len(all_batches):
                torch.nn.utils.clip_grad_norm_([p for p in model.parameters() if p.requires_grad], 1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
            if i % 50 == 0:
                print(f"epoch {epoch} batch {i}/{len(all_batches)} loss {running / count:.4f} "
                      f"elapsed {time.time() - start:.0f}s", flush=True)
        current = dev_loss()
        entry = {"epoch": epoch, "train_loss": running / max(1, count), "dev_loss": current,
                 "elapsed_s": round(time.time() - start, 1),
                 "gpu_gb": round(torch.cuda.max_memory_allocated() / 1e9, 1)}
        log.append(entry)
        print(json.dumps(entry), flush=True)
        if current < best:
            best = current
            model.save_pretrained(args.out / "best")
    config = {"args": {k: str(v) for k, v in vars(args).items()}, "train_examples": len(train),
              "train_dropped": train_dropped, "dev_examples": len(dev), "dev_dropped": dev_dropped, "log": log}
    (args.out / "train_log.json").write_text(json.dumps(config, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
