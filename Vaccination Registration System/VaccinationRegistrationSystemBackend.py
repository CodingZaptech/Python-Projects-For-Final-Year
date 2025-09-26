# VaccinationRegistrationSystemBackend.py
# Backend logic for Vaccination Registration System

class VaccinationManager:
    def __init__(self):
        self.registrations = []

    def register(self, details: dict):
        self.registrations.append(details)
        print(f"Successfully registered {details['name']} for vaccination.")

    def view_registered(self):
        if not self.registrations:
            print("No registrations found.")
            return
        print("\n--- Registered Users ---")
        for i, user in enumerate(self.registrations, start=1):
            print(f"{i}. {user['name']} | Age: {user['age']} | Vaccine: {user['vaccine_type']}")
