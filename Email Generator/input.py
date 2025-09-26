# input.py
# Handles user input for Email Generator

def get_inputs():
    """
    Collects name and domain from user.
    :return: (name, domain)
    """
    name = input("Enter your name: ")
    domain = input("Enter domain (e.g., gmail.com): ")
    return name, domain
