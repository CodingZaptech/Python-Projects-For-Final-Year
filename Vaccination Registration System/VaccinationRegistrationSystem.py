# VaccinationRegistrationSystem.py
# Main runner for Vaccination Registration System

from VaccinationRegistrationSystemBackend import VaccinationManager
import input

def main():
    manager = VaccinationManager()
    while True:
        choice, details = input.get_inputs()
        if choice == "register":
            manager.register(details)
        elif choice == "view":
            manager.view_registered()
        elif choice == "exit":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
