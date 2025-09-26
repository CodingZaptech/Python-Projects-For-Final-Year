# input.py
# Handles user input for Story Generator

def get_inputs() -> dict:
    """
    Collects words for story placeholders.
    :return: dictionary of words
    """
    words = {}
    words["place"] = input("Enter a place: ")
    words["adjective"] = input("Enter an adjective: ")
    words["character"] = input("Enter a character: ")
    words["activity"] = input("Enter an activity: ")
    words["event"] = input("Enter an event: ")
    return words
