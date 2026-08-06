"""Line-by-line profiling"""

import time
import random

@profile  # line_profiler decorator
def slow_function():
    total = 0
    for i in range(1000000):
        total += i * random.random()
    return total

def main():
    result = slow_function()
    print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()
