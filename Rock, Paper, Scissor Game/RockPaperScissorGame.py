# RockPaperScissorGame.py
# Main runner file for Rock, Paper, Scissor Game project

from RockPaperScissorGameBackend import RPSGame
import input

def main():
    user_choice = input.get_inputs()
    game = RPSGame()
    result, computer_choice = game.play(user_choice)

    print(f"Computer chose: {computer_choice}")
    print(result)

if __name__ == "__main__":
    main()
