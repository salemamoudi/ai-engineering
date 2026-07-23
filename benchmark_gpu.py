#!/usr/bin/env python
"""
GPU Performance Benchmark
Tests matrix multiplication speed on GPU vs CPU
"""

import torch
import time

def benchmark(size=2000, iterations=10):
    """Benchmark matrix multiplication on GPU and CPU"""
    print(f"Benchmarking matrix multiplication ({size}x{size})")
    print(f"Running {iterations} iterations each\n")
    
    # GPU Test
    if torch.cuda.is_available():
        print("GPU Test:")
        x_gpu = torch.randn(size, size).cuda()
        y_gpu = torch.randn(size, size).cuda()
        
        # Warmup
        for _ in range(3):
            z_gpu = torch.matmul(x_gpu, y_gpu)
        torch.cuda.synchronize()
        
        # Benchmark
        start = time.time()
        for _ in range(iterations):
            z_gpu = torch.matmul(x_gpu, y_gpu)
        torch.cuda.synchronize()
        gpu_time = (time.time() - start) / iterations
        
        print(f"  GPU time: {gpu_time:.4f} seconds per multiplication")
        print(f"  GPU memory used: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    else:
        gpu_time = None
        print("  GPU: Not available")
    
    # CPU Test
    print("\nCPU Test:")
    x_cpu = torch.randn(size, size)
    y_cpu = torch.randn(size, size)
    
    # Warmup
    for _ in range(3):
        z_cpu = torch.matmul(x_cpu, y_cpu)
    
    # Benchmark
    start = time.time()
    for _ in range(iterations):
        z_cpu = torch.matmul(x_cpu, y_cpu)
    cpu_time = (time.time() - start) / iterations
    
    print(f"  CPU time: {cpu_time:.4f} seconds per multiplication")
    
    # Speed comparison
    if gpu_time:
        speedup = cpu_time / gpu_time
        print(f"\n🚀 GPU is {speedup:.2f}x faster than CPU!")

if __name__ == "__main__":
    benchmark()
