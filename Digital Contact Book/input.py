# input.py
# Handles user input for Digital Contact Book

def get_inputs():
    """
    Collects menu choice and required details from the user.
    :return: (choice, details as tuple/list)
    """
    print("\n--- Digital Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        return choice, (name, number)
    elif choice == "2":
        name = input("Enter name to search: ")
        return choice, (name,)
    else:
        return choice, ()
