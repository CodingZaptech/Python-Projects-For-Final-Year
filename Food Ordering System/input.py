# input.py
# Handles user input for Food Ordering System

def get_inputs():
    """
    Collects menu choice and details from user.
    :return: (choice, details)
    """
    print("\n--- Food Ordering System ---")
    print("1. Show Menu")
    print("2. Order Food")
    print("3. View Orders")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "2":
        item = input("Enter food item name: ")
        return choice, (item,)
    return choice, ()
