# RollOutTheDiceBackend.py
# Backend logic for Dice Roll GUI

import tkinter as tk
from random import randint

class DiceApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Roll Out The Dice")
        self.window.geometry("300x200")

        self.label = tk.Label(self.window, text="Click Roll to start", font=("Arial", 16))
        self.label.pack(pady=20)

        self.roll_button = tk.Button(self.window, text="ROLL", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack(pady=10)

    def roll_dice(self):
        dice_value = randint(1,6)
        self.label.config(text=f"You rolled: {dice_value}")

    def run(self):
        self.window.mainloop()
