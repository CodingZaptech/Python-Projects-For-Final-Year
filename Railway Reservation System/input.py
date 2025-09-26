# input.py
# Handles user input for Railway Reservation System

def get_inputs():
    """
    Collects passenger name and train number.
    :return: (name, train number)
    """
    passenger_name = input("Enter passenger name: ")
    train_number = input("Enter train number (101/202): ")
    return passenger_name, train_number
