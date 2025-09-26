# input.py
# Handles user input for Vaccination Registration System

def get_inputs():
    print("\n--- Vaccination Registration ---")
    print("1. Register User")
    print("2. View Registered Users")
    print("3. Exit")
    choice = input("Enter choice: ").strip().lower()
    if choice in ["1", "register"]:
        details = {
            "name": input("Enter name: "),
            "age": input("Enter age: "),
            "vaccine_type": input("Enter vaccine type: ")
        }
        return "register", details
    elif choice in ["2", "view"]:
        return "view", {}
    elif choice in ["3", "exit"]:
        return "exit", {}
    return "invalid", {}
