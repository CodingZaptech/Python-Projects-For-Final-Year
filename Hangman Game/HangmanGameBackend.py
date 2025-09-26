# HangmanGameBackend.py
# Backend logic for Hangman Game

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = set()
        self.attempts_left = 6

    def make_guess(self, letter: str) -> str:
        if letter in self.guessed_letters:
            return "You already guessed that letter."
        
        self.guessed_letters.add(letter)

        if letter in self.word:
            return "Correct guess!"
        else:
            self.attempts_left -= 1
            return f"Wrong guess. Attempts left: {self.attempts_left}"

    def get_display_word(self) -> str:
        return " ".join([ch if ch in self.guessed_letters else "_" for ch in self.word])

    def is_over(self) -> bool:
        return self.attempts_left == 0 or self.is_won()

    def is_won(self) -> bool:
        return all(ch in self.guessed_letters for ch in self.word)
