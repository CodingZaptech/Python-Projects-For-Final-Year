# input.py
# Handles user input for Binary Search project

def get_inputs():
    """
    Collects a list of numbers and target value from user.
    :return: (list of numbers, target number)
    """
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the number to search: "))
    return numbers, target
