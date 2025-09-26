# RockPaperScissorGameBackend.py
# Backend logic for Rock, Paper, Scissor Game

import random

class RPSGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor"]

    def play(self, user_choice: str):
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            return "It's a Tie!", computer_choice
        elif (
            (user_choice == "rock" and computer_choice == "scissor") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissor" and computer_choice == "paper")
        ):
            return "You Win!", computer_choice
        else:
            return "You Lose!", computer_choice
