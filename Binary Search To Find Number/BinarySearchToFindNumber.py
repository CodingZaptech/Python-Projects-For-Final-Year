# BinarySearchToFindNumber.py
# Main runner file for Binary Search project

from BinarySearchToFindNumberBackend import BinarySearch
import input

def main():
    # Get the list and target from input handler
    numbers, target = input.get_inputs()
    
    # Create BinarySearch instance
    bs = BinarySearch(numbers)
    
    # Perform search
    result = bs.search(target)
    
    # Display result
    if result != -1:
        print(f"Number {target} found at index {result}.")
    else:
        print(f"Number {target} not found in the list.")

if __name__ == "__main__":
    main()
