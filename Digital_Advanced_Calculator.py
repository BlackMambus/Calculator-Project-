import tkinter as tk
from tkinter import ttk
import math

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Digital Calculator")
        self.geometry("400x550")
        self.configure(bg="#282c34")
        self.resizable(False, False)

        self.expression = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        style = ttk.Style(self)
        style.theme_use('default')
        style.configure('TButton', background='#61afef', foreground='white', font=('Arial', 14), padding=10)
        style.map('TButton', background=[('active', '#528bff')])
        
        # Display Entry
        self.display = tk.Entry(self, font=('Consolas', 14), borderwidth=0, relief=tk.FLAT, justify='right', bg='#21252b', fg='white', insertbackground='white')
        self.display.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

        # Buttons Frame
        btns_frame = tk.Frame(self, bg="#282c34")
        btns_frame.pack(expand=True, fill="both")

        # Define buttons layout
        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'exp'],
            ['1', '2', '3', '-', 'ln'],
            ['0', '.', '%', '+', 'log'],
            ['(', ')', 'sin', 'cos', 'tan'],
            ['C', 'CE', '^', 'Ans', '=']
        ]

        for r, row in enumerate(buttons):
            row_frame = tk.Frame(btns_frame, bg="#282c34")
            row_frame.pack(expand=True, fill="both")
            for c, btn_text in enumerate(row):
                btn = ttk.Button(row_frame, text=btn_text)
                btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)
                btn.config(command=lambda b=btn_text: self.on_button_click(b))
        
        self.ans = ""

    def on_button_click(self, char):
        if char == "C":
            # Clear all
            self.expression = ""
            self.update_display()
        elif char == "CE":
            # Clear last entry
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == "=":
            self.calculate()
        elif char == "Ans":
            self.expression += self.ans
            self.update_display()
        elif char in ("sin", "cos", "tan", "log", "ln", "exp", "sqrt"):
            self.expression += char + "("
            self.update_display()
        elif char == "^":
            self.expression += "**"
            self.update_display()
        else:
            self.expression += char
            self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
    
    def calculate(self):
        try:
            # Replace known functions with math module functions
            expression = self.expression
            expression = expression.replace("sqrt", "math.sqrt")
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("log", "math.log10")
            expression = expression.replace("ln", "math.log")
            expression = expression.replace("exp", "math.exp")
            expression = expression.replace("%", "/100")

            # Evaluate the expression safely
            result = eval(expression, {"math": math, "__builtins__": None})
            self.ans = str(result)

            # Show result and set expression to result for further calculations
            self.expression = self.ans
            self.update_display()
        except Exception as e:
            self.expression = ""
            self.update_display()
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()



