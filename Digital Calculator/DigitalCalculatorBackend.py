# DigitalCalculatorBackend.py
# Backend logic for Digital Calculator with Tkinter GUI

import tkinter as tk

class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Digital Calculator")

        self.entry = tk.Entry(self.window, width=20, font=('Arial', 18), bd=5, relief=tk.RIDGE)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(self.window, text=text, width=5, height=2, font=('Arial', 14),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

    def run(self):
        self.window.mainloop()
