# FoodOrderingSystemBackend.py
# Backend logic for Food Ordering System

class FoodSystem:
    def __init__(self):
        self.menu = {"Burger": 50, "Pizza": 100, "Pasta": 80}
        self.orders = []

    def show_menu(self):
        print("\n--- Menu ---")
        for item, price in self.menu.items():
            print(f"{item}: Rs {price}")

    def order_food(self, item: str):
        if item in self.menu:
            self.orders.append(item)
            return f"{item} ordered successfully."
        return "Item not available."

    def view_orders(self):
        if not self.orders:
            print("No orders yet.")
        else:
            print("\n--- Orders ---")
            for order in self.orders:
                print(order)
