"""
Created on Sun Jun  2 16:05:59 2024
@author: saketh
"""
from tkinter import *

class Calculator:
    def __init__(self):
        self.math = 'start'

    def evaluate_expression(self, expression):
        try:
            return str(eval(expression.replace("^", "**")))
        except Exception as e:
            return 'undefined'

def run_gui_calculator():
    root = Tk()
    calculator = Calculator()
    e = Entry(root, borderwidth=5, font=('Arial 13', 15))
    e.grid(row=0, columnspan=4)

    def bottom_click(num):
        if calculator.math == 'stop':
            bottom_clear()
            calculator.math = 'start'
        c = e.get()
        e.delete(0, END)
        e.insert(0, c + str(num))

    def bottom_clear():
        e.delete(0, END)
        e.config(background='white')

    def bottom_equal():
        result = calculator.evaluate_expression(e.get())
        bottom_clear()
        e.insert(0, result)
        if result == 'undefined':
            e.config(background='red')
        else:
            e.config(background='white')
        calculator.math = 'stop'

    b1 = Button(root, text="1", command=lambda: bottom_click(1), padx=20, pady=20)
    b2 = Button(root, text="2", command=lambda: bottom_click(2), padx=20, pady=20)
    b3 = Button(root, text="3", command=lambda: bottom_click(3), padx=20, pady=20)
    b4 = Button(root, text="4", command=lambda: bottom_click(4), padx=20, pady=20)
    b5 = Button(root, text="5", command=lambda: bottom_click(5), padx=20, pady=20)
    b6 = Button(root, text="6", command=lambda: bottom_click(6), padx=20, pady=20)
    b7 = Button(root, text="7", command=lambda: bottom_click(7), padx=20, pady=20)
    b8 = Button(root, text="8", command=lambda: bottom_click(8), padx=20, pady=20)
    b9 = Button(root, text="9", command=lambda: bottom_click(9), padx=20, pady=20)
    b0 = Button(root, text="0", command=lambda: bottom_click(0), padx=50, pady=20)
    badd = Button(root, text="+", command=lambda: bottom_click("+"), padx=30, pady=20)
    bsub = Button(root, text="-", command=lambda: bottom_click("-"), padx=20, pady=20)
    bmul = Button(root, text="*", command=lambda: bottom_click("*"), padx=20, pady=20)
    bdiv = Button(root, text="/", command=lambda: bottom_click("/"), padx=20, pady=20)
    bpower = Button(root, text="^", command=lambda: bottom_click("^"), padx=30, pady=20)
    bclear = Button(root, text="clear", command=bottom_clear, padx=10, pady=20)
    bequal = Button(root, text="=", command=bottom_equal, padx=30, pady=55)
    bexit = Button(root, text="off", command=root.quit, padx=25, pady=20)

    b1.grid(row=4, column=0)
    b2.grid(row=4, column=1)
    b3.grid(row=4, column=2)
    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    b0.grid(row=5, column=0, columnspan=2)
    badd.grid(row=2, column=3)
    bclear.grid(row=5, column=2)
    bequal.grid(row=4, column=3, rowspan=2)
    bsub.grid(row=1, column=0)
    bdiv.grid(row=1, column=1)
    bmul.grid(row=1, column=2)
    bpower.grid(row=3, column=3)
    bexit.grid(row=1, column=3)
    root.mainloop()

def run_command_line_calculator():
    calculator = Calculator()
    print("Command-line Calculator. Type 'exit' to quit.")
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'exit':
            break
        result = calculator.evaluate_expression(expression)
        print("Result:", result)


print("Choose Calculator Interface:")
print("1. GUI")
print("2. Command Line")
choice = input("Enter choice (1/2): ")
if choice == '1':
    run_gui_calculator()
elif choice == '2':
    run_command_line_calculator()
else:
    print("Invalid choice")
