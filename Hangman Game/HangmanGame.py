# HangmanGame.py
# Main runner file for Hangman Game project

from HangmanGameBackend import Hangman
import input

def main():
    word = input.get_word()
    game = Hangman(word)

    while not game.is_over():
        print("\nWord so far:", game.get_display_word())
        guess = input.get_guess()
        message = game.make_guess(guess)
        print(message)

    if game.is_won():
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    main()
