# input.py
# Handles user input for Kick Out Unmatched Word

def get_inputs():
    sentence = input("Enter sentence: ")
    valid_words = input("Enter valid words separated by space: ").lower().split()
    return sentence, valid_words
