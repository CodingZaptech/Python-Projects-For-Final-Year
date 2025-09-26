# RealEstateManagementSystem.py
# Main runner file for Real Estate Management System

from RealEstateManagementSystemBackend import RealEstateManager
import input

def main():
    manager = RealEstateManager()

    while True:
        choice, details = input.get_inputs()
        if choice == "add":
            manager.add_property(details)
        elif choice == "view":
            manager.view_properties()
        elif choice == "search":
            keyword = details.get("keyword")
            manager.search_properties(keyword)
        elif choice == "exit":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
