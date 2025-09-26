# DigitalContactBookBackend.py
# Backend logic for Digital Contact Book

class ContactBook:
    def __init__(self):
        # Stores contacts in dictionary
        self.contacts = {}

    def add_contact(self, name: str, number: str) -> str:
        self.contacts[name] = number
        return f"Contact {name} added successfully."

    def search_contact(self, name: str) -> str:
        if name in self.contacts:
            return f"{name}: {self.contacts[name]}"
        return "Contact not found."

    def view_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\n--- Contact List ---")
        for name, number in self.contacts.items():
            print(f"{name}: {number}")
