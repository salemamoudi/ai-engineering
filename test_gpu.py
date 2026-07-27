#!/usr/bin/env python
"""GPU Verification Script"""

import torch
import sys
import time

print("=" * 50)
print("GPU Verification Test")
print("=" * 50)

print(f"PyTorch version: {torch.__version__}")

cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

if cuda_available:
    print(f"CUDA version: {torch.version.cuda}")
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    
    for i in range(torch.cuda.device_count()):
        print(f"\nGPU {i}:")
        print(f"  Name: {torch.cuda.get_device_name(i)}")
        print(f"  Memory: {torch.cuda.get_device_properties(i).total_memory / 1024**3:.2f} GB")
    
    # Test tensor operations on GPU
    print("\nTesting tensor operations on GPU:")
    x = torch.randn(1000, 1000).cuda()
    y = torch.randn(1000, 1000).cuda()
    
    start_time = time.time()
    z = torch.matmul(x, y)
    torch.cuda.synchronize()
    elapsed_time = time.time() - start_time
    
    print(f"  Matrix multiplication: {elapsed_time:.4f} seconds")
    print("✅ GPU is working correctly!")
else:
    print("\n⚠️ No GPU detected. Running on CPU mode.")
    print("   For cloud GPU setup, see instructions below.")

print("\n" + "=" * 50)
