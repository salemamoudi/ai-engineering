"""Buggy code for debugging practice"""

def calculate_average(numbers):
    """Calculate average of a list"""
    total = 0
    for i in range(len(numbers) + 1):  # Off-by-one bug!
        total += numbers[i]
    return total / len(numbers)

def process_data(data):
    """Process data with potential issues"""
    result = []
    for item in data:
        if item > 10:
            result.append(item * 2)
        else:
            result.append(item / 0)  # Division by zero!
    return result

def main():
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    print(f"Average: {avg}")
    
    data = [5, 15, 20, 0]
    processed = process_data(data)
    print(f"Processed: {processed}")

if __name__ == "__main__":
    main()
