# TicTacToeGame.py
# Main runner file for Tic-Tac-Toe Game

from TicTacToeGameBackend import TicTacToe
import input

def main():
    game = TicTacToe()
    game.start_game()

if __name__ == "__main__":
    main()
