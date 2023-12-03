# utils.py

def read_input(filename):
    with open(filename, 'r') as input:
        data = input.readlines()
    return data

def remove_duplicates(input_list):
    """Remove duplicates from a list while preserving the order."""
    return list(dict.fromkeys(input_list))

def file_exists(filename):
    """Check if a file exists."""
    import os
    return os.path.isfile(filename)

def main():
    # Example usage of the utility functions
    numbers = [1, 2, 3, 4, 4, 5, 5]
    unique_numbers = remove_duplicates(numbers)
    # avg = calculate_average(numbers)

    print(f"Original list: {numbers}")
    print(f"List with duplicates removed: {unique_numbers}")
    print(f"Average of numbers: {avg}")

if __name__ == '__main__':
    main()