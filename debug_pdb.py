"""Debugging with pdb"""

import pdb

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        pdb.set_trace()  # Breakpoint
        total += numbers[i]
    return total / len(numbers)

def main():
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    print(f"Average: {avg}")

if __name__ == "__main__":
    main()
