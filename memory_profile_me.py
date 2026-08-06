"""Memory profiling example"""

from memory_profiler import profile
import time

@profile
def memory_hungry():
    """Function that uses a lot of memory"""
    large_list = []
    for i in range(1000000):
        large_list.append(i * 2)
    return large_list

@profile
def efficient_memory():
    """More memory-efficient function"""
    return [i * 2 for i in range(1000000)]

def main():
    print("Running memory_hungry...")
    result1 = memory_hungry()
    print(f"List length: {len(result1)}")
    
    print("\nRunning efficient_memory...")
    result2 = efficient_memory()
    print(f"List length: {len(result2)}")

if __name__ == "__main__":
    main()
