# JackpotGame.py
# Main runner file for Jackpot Game project

from JackpotGameBackend import Jackpot
import input

def main():
    # Get user guess
    guess = input.get_inputs()
    
    # Create Jackpot instance
    game = Jackpot()
    
    # Play game
    result, winning_number = game.play(guess)
    
    # Display result
    print(f"The winning number was: {winning_number}")
    if result:
        print("Congratulations! You won the Jackpot!")
    else:
        print("Sorry, better luck next time.")

if __name__ == "__main__":
    main()
