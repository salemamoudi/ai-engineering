"""GPU profiling with PyTorch"""

import torch
import time

def gpu_heavy_work():
    """Perform heavy GPU operations"""
    if not torch.cuda.is_available():
        print("No GPU available, using CPU")
        device = torch.device("cpu")
    else:
        device = torch.device("cuda")
    
    # Create large tensors
    x = torch.randn(5000, 5000, device=device)
    y = torch.randn(5000, 5000, device=device)
    
    # Matrix multiplication
    start = time.time()
    z = torch.matmul(x, y)
    torch.cuda.synchronize() if torch.cuda.is_available() else None
    elapsed = time.time() - start
    print(f"Matrix multiplication time: {elapsed:.4f}s")
    
    # Memory usage
    if torch.cuda.is_available():
        print(f"GPU Memory allocated: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
        print(f"GPU Memory cached: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")

if __name__ == "__main__":
    print("Running GPU-heavy workload...")
    gpu_heavy_work()
