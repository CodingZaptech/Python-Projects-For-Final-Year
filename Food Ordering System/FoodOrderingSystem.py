# FoodOrderingSystem.py
# Main runner file for Food Ordering System project

from FoodOrderingSystemBackend import FoodSystem
import input

def main():
    system = FoodSystem()

    while True:
        choice, details = input.get_inputs()

        if choice == "1":
            system.show_menu()
        elif choice == "2":
            item = details[0]
            print(system.order_food(item))
        elif choice == "3":
            system.view_orders()
        elif choice == "4":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
