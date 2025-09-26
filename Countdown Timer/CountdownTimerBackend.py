# CountdownTimerBackend.py
# Backend logic for Countdown Timer

import time

class Countdown:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def start(self):
        print("\nStarting countdown...")
        while self.seconds:
            mins, secs = divmod(self.seconds, 60)
            timer_format = f"{mins:02}:{secs:02}"
            print(timer_format, end="\r")
            time.sleep(1)
            self.seconds -= 1
        print("00:00\nTime's up!")
