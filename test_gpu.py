#!/usr/bin/env python
"""
GPU Verification Script
Tests if PyTorch can detect and use your GPU
"""

import torch
import sys
import time

print("=" * 50)
print("GPU Verification Test")
print("=" * 50)

# Check PyTorch version
print(f"PyTorch version: {torch.__version__}")

# Check CUDA availability
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

if cuda_available:
    # Get GPU information
    print(f"CUDA version: {torch.version.cuda}")
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    
    for i in range(torch.cuda.device_count()):
        print(f"\nGPU {i}:")
        print(f"  Name: {torch.cuda.get_device_name(i)}")
        print(f"  Memory: {torch.cuda.get_device_properties(i).total_memory / 1024**3:.2f} GB")
        print(f"  Compute capability: {torch.cuda.get_device_properties(i).major}.{torch.cuda.get_device_properties(i).minor}")
    
    # Test tensor operations on GPU
    print("\nTesting tensor operations on GPU:")
    
    # Create tensors on GPU
    x = torch.randn(1000, 1000).cuda()
    y = torch.randn(1000, 1000).cuda()
    
    # Matrix multiplication
    start_time = time.time()
    z = torch.matmul(x, y)
    torch.cuda.synchronize()  # Wait for GPU to finish
    elapsed_time = time.time() - start_time
    
    print(f"  Matrix multiplication (1000x1000): {elapsed_time:.4f} seconds")
    print(f"  Result shape: {z.shape}")
    print(f"  First value: {z[0,0]:.4f}")
    
    # Memory usage
    print(f"\nMemory usage:")
    print(f"  Allocated: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    print(f"  Cached: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")
    
    print("\n✅ GPU is working correctly!")
else:
    print("\n⚠️ No GPU detected. Running on CPU mode.")
    print("   For cloud GPU setup, see instructions below.")
    
    # Test CPU operation
    x = torch.randn(1000, 1000)
    y = torch.randn(1000, 1000)
    z = torch.matmul(x, y)
    print(f"  CPU matrix multiplication: {z.shape}")
    print("\n✅ CPU mode is working (GPU not required for this course)")

print("\n" + "=" * 50)
