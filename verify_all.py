import sys
import torch

print("=" * 50)
print("Environment Verification")
print("=" * 50)

print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")

if torch.cuda.is_available():
    print(f"CUDA available: ✅")
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
else:
    print("CUDA available: ❌ (CPU mode)")

print("=" * 50)
