# JackpotGameBackend.py
# Backend logic for Jackpot Game

import random

class Jackpot:
    def __init__(self):
        # Jackpot numbers will be between 1 and 10
        self.range = (1, 10)

    def play(self, guess: int):
        """
        Compares user guess with random winning number
        :param guess: user's guessed number
        :return: (True/False, winning number)
        """
        winning_number = random.randint(*self.range)
        return guess == winning_number, winning_number
