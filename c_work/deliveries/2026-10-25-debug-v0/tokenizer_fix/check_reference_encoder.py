from pathlib import Path
import torch
from safetensors.torch import save_file
from moshi.server_conditioner import EncoderService

root = Path.home() / "projects/moshi-rag"
config = root / "tokenizer_fix/artifacts/moshirag.local.json"
weights = Path.home() / "models/moshika-rag-pytorch-bf16/model.safetensors"

assert config.is_file(), f"找不到配置：{config}"
assert weights.is_file(), f"找不到模型权重：{weights}"
assert torch.cuda.is_available(), "没有可用 GPU，请通过 sbatch 运行"

print("GPU:", torch.cuda.get_device_name(0), flush=True)
print("正在加载参考编码器……", flush=True)

with torch.inference_mode():
    service = EncoderService(
        config=str(config),
        moshi_weight=str(weights),
        conditioner="reference_with_time",
        device="cuda:0",
    )
    service.condition_provider.eval()

    text = "Apollo 11 launched on July 16, 1969."
    print("测试资料：", text, flush=True)
    tensor = service.encode(text)

    assert isinstance(tensor, torch.Tensor), "输出不是张量"
    assert tensor.ndim == 3, f"输出形状异常：{tensor.shape}"
    assert tensor.shape[0] == 1 and tensor.shape[1] > 0
    assert tensor.shape[2] == 4096, f"输出维度异常：{tensor.shape}"
    assert torch.isfinite(tensor).all().item(), "输出包含无效数字"

    output = root / "tokenizer_fix/artifacts/reference_smoke.safetensors"
    save_file({"tensor": tensor.detach().cpu().contiguous()}, str(output))

print("输出形状：", tuple(tensor.shape), flush=True)
print("保存位置：", output, flush=True)
print("REFERENCE ENCODER PASSED", flush=True)
