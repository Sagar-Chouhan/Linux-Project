import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.result_var = tk.StringVar()

        # Entry for displaying the result
        self.entry = tk.Entry(master, textvariable=self.result_var, width=16, font=('Arial', 24), bd=10, insertwidth=2, borderwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(master, text=text, padx=20, pady=20, command=self.calculate)
            elif text == 'C':
                button = tk.Button(master, text=text, padx=20, pady=20, command=self.clear)
            else:
                button = tk.Button(master, text=text, padx=20, pady=20, command=lambda t=text: self.append_to_expression(t))
            button.grid(row=row, column=col)

    def append_to_expression(self, value):
        current = self.result_var.get()
        self.result_var.set(current + value)

    def clear(self):
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
