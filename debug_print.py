"""Debugging with print statements"""

def calculate_average(numbers):
    print(f"[DEBUG] numbers: {numbers}")
    total = 0
    print(f"[DEBUG] initial total: {total}")
    for i in range(len(numbers)):
        print(f"[DEBUG] i: {i}, numbers[{i}]: {numbers[i]}")
        total += numbers[i]
        print(f"[DEBUG] total after addition: {total}")
    avg = total / len(numbers)
    print(f"[DEBUG] final avg: {avg}")
    return avg

def main():
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    print(f"Average: {avg}")

if __name__ == "__main__":
    main()
