# JudgeYourLuckBackend.py
# Backend logic for Wheel of Fortune Game with GUI

import tkinter as tk
from tkinter import messagebox
import random
import math

class WheelOfFortuneApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wheel of Fortune")
        self.window.geometry("400x450")
        
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="white")
        self.canvas.pack()

        self.spin_button = tk.Button(self.window, text="SPIN", font=("Arial", 16), command=self.spin_wheel)
        self.spin_button.pack(pady=10)

        # Wheel slices
        self.sectors = ["100", "200", "300", "400", "500", "Bankrupt", "Lose Turn", "1000"]
        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan"]
        self.angle_per_sector = 360 / len(self.sectors)
        self.draw_wheel(0)

    def draw_wheel(self, rotation_angle):
        self.canvas.delete("all")
        center_x, center_y = 200, 200
        radius = 150
        start_angle = rotation_angle
        for i, sector in enumerate(self.sectors):
            color = self.colors[i % len(self.colors)]
            self.canvas.create_arc(center_x-radius, center_y-radius, center_x+radius, center_y+radius,
                                   start=start_angle, extent=self.angle_per_sector, fill=color)
            mid_angle = math.radians(start_angle + self.angle_per_sector/2)
            text_x = center_x + (radius/1.5) * math.cos(mid_angle)
            text_y = center_y + (radius/1.5) * math.sin(mid_angle)
            self.canvas.create_text(text_x, text_y, text=sector, font=("Arial", 10, "bold"))
            start_angle += self.angle_per_sector

    def spin_wheel(self):
        spins = random.randint(3, 6) * 360  # multiple full rotations
        selected_angle = random.randint(0, 359)
        total_rotation = spins + selected_angle
        sector_index = int((360 - selected_angle) / self.angle_per_sector) % len(self.sectors)
        prize = self.sectors[sector_index]
        self.draw_wheel(total_rotation % 360)
        messagebox.showinfo("Result", f"You won: {prize} points!")

    def run(self):
        self.window.mainloop()
