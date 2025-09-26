# input.py
# Handles user input for Hangman Game

def get_word():
    """
    Collects the secret word for the game.
    (In real gameplay, it could be hidden from the guesser.)
    """
    return input("Enter the secret word: ")

def get_guess():
    """
    Collects a single letter guess from the user.
    """
    return input("Guess a letter: ").lower()
