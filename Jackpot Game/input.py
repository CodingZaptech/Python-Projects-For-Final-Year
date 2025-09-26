# input.py
# Handles user input for Jackpot Game

def get_inputs():
    """
    Collects user's guessed number.
    :return: guessed number
    """
    guess = int(input("Enter your guess (1-10): "))
    return guess
