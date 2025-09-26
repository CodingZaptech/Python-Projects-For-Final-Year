# CountdownTimer.py
# Main runner file for Countdown Timer project

from CountdownTimerBackend import Countdown
import input

def main():
    seconds = input.get_inputs()
    timer = Countdown(seconds)
    timer.start()

if __name__ == "__main__":
    main()
