"""Performance profiling example"""

import time
import random

def slow_function():
    """A deliberately slow function"""
    total = 0
    for i in range(1000000):
        total += i * random.random()
    return total

def fast_function():
    """A faster function"""
    return sum(i * random.random() for i in range(100000))

def main():
    print("Running slow_function...")
    start = time.time()
    slow_result = slow_function()
    print(f"Slow function result: {slow_result:.2f}")
    print(f"Time: {time.time() - start:.2f}s")
    
    print("\nRunning fast_function...")
    start = time.time()
    fast_result = fast_function()
    print(f"Fast function result: {fast_result:.2f}")
    print(f"Time: {time.time() - start:.2f}s")

if __name__ == "__main__":
    main()
