# input.py
# Handles user input for Rock, Paper, Scissor Game

def get_inputs():
    """
    Collects user choice for the game.
    :return: user choice string
    """
    return input("Enter your choice (rock/paper/scissor): ").lower()
