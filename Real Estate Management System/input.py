# input.py
# Handles user input for Real Estate Management System

def get_inputs():
    print("\n--- Real Estate Management ---")
    print("1. Add Property")
    print("2. View Properties")
    print("3. Search Properties")
    print("4. Exit")
    
    choice = input("Enter choice: ").strip().lower()
    if choice in ["1", "add"]:
        details = {
            "name": input("Enter property name: "),
            "location": input("Enter location: "),
            "price": input("Enter price: ")
        }
        return "add", details
    elif choice in ["2", "view"]:
        return "view", {}
    elif choice in ["3", "search"]:
        keyword = input("Enter keyword to search: ")
        return "search", {"keyword": keyword}
    elif choice in ["4", "exit"]:
        return "exit", {}
    return "invalid", {}
