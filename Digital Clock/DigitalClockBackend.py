# DigitalClockBackend.py
# Backend logic for Digital Clock with Tkinter GUI

import tkinter as tk
import time

class ClockApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Digital Clock")
        self.window.geometry("300x100")

        self.label = tk.Label(self.window, font=('Arial', 40), bg="black", fg="cyan")
        self.label.pack(anchor="center")

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.window.after(1000, self.update_time)

    def run(self):
        self.window.mainloop()
