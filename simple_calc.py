#IMPLEMENTATION OF SIMPLE CALCULATOR.......
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.config(bg="black")
        self.root.resizable(False, False)

        self.equation = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 24), bd=8, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ('AC', 1, 0), ('⌫', 1, 1), ('^', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('%', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

    def create_button(self, text, row, column):
        button_width = 6
        button_height = 2
        if text in ('AC', '⌫', '^', '/', '*', '-', '+', '=', '%'):
            button_color = "#546de5"
            fg_color = "white"
        else:
            button_color = "#2f3640"
            fg_color = "white"

        button = tk.Button(self.root,text=text, font=("Arial", 18), bg=button_color, fg=fg_color, bd=0,
                           width=button_width, height=button_height, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'AC':
            self.equation.set('')
        elif char == '⌫':
            self.equation.set(self.equation.get()[:-1])
        elif char == '=':
            try:
                expression = self.equation.get().replace('^', '**')
                self.equation.set(str(eval(expression)))

            except Exception as e:
                self.equation.set('Error')
        else:
            self.equation.set(self.equation.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()