# TicTacToeGameBackend.py
# Backend logic for Tic-Tac-Toe Game

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        board = self.board
        print(f"\n{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def check_winner(self):
        b = self.board
        combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for x,y,z in combos:
            if b[x] == b[y] == b[z] != " ":
                return b[x]
        if " " not in b:
            return "Tie"
        return None

    def start_game(self):
        while True:
            self.display_board()
            move = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
            if self.board[move] == " ":
                self.board[move] = self.current_player
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    if winner == "Tie":
                        print("The game is a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    break
                self.current_player = "O" if self.current_player == "X" else "X"
            else:
                print("Position already taken. Try again.")
