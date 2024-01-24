import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Taschenrechner")

        # Eingabefeld
        self.entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Tasten
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), bd=8, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_expression = self.entry.get()

        if value == '=':
            try:
                result = eval(current_expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Fehler", "Ungültiger Ausdruck")
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
