# RealEstateManagementSystemBackend.py
# Backend logic for Real Estate Management System

class RealEstateManager:
    def __init__(self):
        self.properties = []

    def add_property(self, details: dict):
        self.properties.append(details)
        print("Property added successfully!")

    def view_properties(self):
        if not self.properties:
            print("No properties available.")
            return
        print("\n--- Property Listings ---")
        for i, prop in enumerate(self.properties, start=1):
            print(f"{i}. {prop['name']} | Location: {prop['location']} | Price: {prop['price']}")

    def search_properties(self, keyword: str):
        results = [prop for prop in self.properties if keyword.lower() in prop['name'].lower() or keyword.lower() in prop['location'].lower()]
        if results:
            print("\n--- Search Results ---")
            for prop in results:
                print(f"{prop['name']} | {prop['location']} | {prop['price']}")
        else:
            print("No matching properties found.")
