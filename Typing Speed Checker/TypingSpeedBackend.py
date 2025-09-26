# TypingSpeedBackend.py
# Backend logic for Typing Speed Checker

import time
import random

class TypingSpeedApp:
    def __init__(self):
        self.sentences = [
            "Python is an amazing programming language.",
            "Typing speed improves with consistent practice.",
            "Always comment your code for better readability.",
            "Data science and machine learning are exciting fields."
        ]

    def start_test(self):
        sentence = random.choice(self.sentences)
        print("Type the following sentence as fast as you can:")
        print(f"\n{sentence}\n")
        input("Press Enter to start...")

        start_time = time.time()
        typed = input("Start typing here: ")
        end_time = time.time()

        duration = end_time - start_time
        word_count = len(typed.split())
        speed = word_count / (duration / 60)

        errors = sum(1 for a, b in zip(sentence, typed) if a != b) + abs(len(sentence) - len(typed))

        print(f"\nTyping Speed: {speed:.2f} WPM")
        print(f"Typing Errors: {errors}")
