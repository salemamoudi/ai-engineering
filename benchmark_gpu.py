"""GPU Performance Benchmark"""

import torch
import time

def benchmark(size=2000, iterations=10):
    """Benchmark matrix multiplication"""
    print(f"Benchmarking ({size}x{size}) - {iterations} iterations\n")
    
    # GPU Test
    if torch.cuda.is_available():
        print("GPU Test:")
        x_gpu = torch.randn(size, size).cuda()
        y_gpu = torch.randn(size, size).cuda()
        
        for _ in range(3):
            z_gpu = torch.matmul(x_gpu, y_gpu)
        torch.cuda.synchronize()
        
        start = time.time()
        for _ in range(iterations):
            z_gpu = torch.matmul(x_gpu, y_gpu)
        torch.cuda.synchronize()
        gpu_time = (time.time() - start) / iterations
        
        print(f"  GPU time: {gpu_time:.4f}s per multiplication")
    else:
        gpu_time = None
        print("  GPU: Not available")
    
    # CPU Test
    print("\nCPU Test:")
    x_cpu = torch.randn(size, size)
    y_cpu = torch.randn(size, size)
    
    for _ in range(3):
        z_cpu = torch.matmul(x_cpu, y_cpu)
    
    start = time.time()
    for _ in range(iterations):
        z_cpu = torch.matmul(x_cpu, y_cpu)
    cpu_time = (time.time() - start) / iterations
    
    print(f"  CPU time: {cpu_time:.4f}s per multiplication")
    
    if gpu_time:
        speedup = cpu_time / gpu_time
        print(f"\n🚀 GPU is {speedup:.2f}x faster than CPU!")

if __name__ == "__main__":
    benchmark()
