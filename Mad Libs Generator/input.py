# input.py
# Handles user input for Mad Libs Generator

def get_inputs() -> dict:
    """
    Collects inputs from the user for the placeholders
    :return: Dictionary of words
    """
    words = {}
    words["place"] = input("Enter a place: ")
    words["adjective"] = input("Enter an adjective: ")
    words["noun"] = input("Enter a noun: ")
    words["verb"] = input("Enter a verb: ")
    return words
