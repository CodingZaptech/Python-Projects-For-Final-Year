# DigitalContactBook.py
# Main runner file for Digital Contact Book project

from DigitalContactBookBackend import ContactBook
import input

def main():
    # Create ContactBook instance
    book = ContactBook()

    while True:
        choice, details = input.get_inputs()
        
        if choice == "1":
            name, number = details
            print(book.add_contact(name, number))
        elif choice == "2":
            name = details[0]
            print(book.search_contact(name))
        elif choice == "3":
            book.view_all_contacts()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
