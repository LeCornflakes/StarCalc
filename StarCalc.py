import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

def add_number(number):
    display.insert(tk.END, number)

def add_operator(operator):
    display.insert(tk.END, operator)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

display = tk.Entry(window, font=("Arial", 24), justify="right")
display.pack(fill="x", padx=10, pady=10)

buttons_frame = tk.Frame(window)
buttons_frame.pack()

Button7 = tk.Button(buttons_frame, text="7", font=("Arial", 20), width=5, height=2, command=lambda: add_number(7))
Button7.grid(row=0, column=0)

Button8 = tk.Button(buttons_frame, text="8", font=("Arial", 20), width=5, height=2, command=lambda: add_number(8))
Button8.grid(row=0, column=1)

Button9 = tk.Button(buttons_frame, text="9", font=("Arial", 20), width=5, height=2, command=lambda: add_number(9))
Button9.grid(row=0, column=2)

Plus = tk.Button(buttons_frame, text="+", font=("Arial", 20), width=5, height=2, command=lambda: add_operator("+"))
Plus.grid(row=0, column=3)

Button4 = tk.Button(buttons_frame, text="4", font=("Arial", 20), width=5, height=2, command=lambda: add_number(4))
Button4.grid(row=1, column=0)

Button5 = tk.Button(buttons_frame, text="5", font=("Arial", 20), width=5, height=2, command=lambda: add_number(5))
Button5.grid(row=1, column=1)

Button6 = tk.Button(buttons_frame, text="6", font=("Arial", 20), width=5, height=2, command=lambda: add_number(6))
Button6.grid(row=1, column=2)

Minus = tk.Button(buttons_frame, text="-", font=("Arial", 20), width=5, height=2, command=lambda: add_operator("-"))
Minus.grid(row=1, column=3)

Button1 = tk.Button(buttons_frame, text="1", font=("Arial", 20), width=5, height=2, command=lambda: add_number(1))
Button1.grid(row=2, column=0)

Button2 = tk.Button(buttons_frame, text="2", font=("Arial", 20), width=5, height=2, command=lambda: add_number(2))
Button2.grid(row=2, column=1)

Button3 = tk.Button(buttons_frame, text="3", font=("Arial", 20), width=5, height=2, command=lambda: add_number(3))
Button3.grid(row=2, column=2)

Multiply = tk.Button(buttons_frame, text="×", font=("Arial", 20), width=5, height=2, command=lambda: add_operator("*"))
Multiply.grid(row=2, column=3)

Clear = tk.Button(buttons_frame, text="C", font=("Arial", 20), width=5, height=2, command=clear)
Clear.grid(row=3, column=0)

Button0 = tk.Button(buttons_frame, text="0", font=("Arial", 20), width=5, height=2, command=lambda: add_number(0))
Button0.grid(row=3, column=1)

Equal = tk.Button(buttons_frame, text="=", font=("Arial", 20), width=5, height=2, command=calculate)
Equal.grid(row=3, column=2)

Divide = tk.Button(buttons_frame, text="÷", font=("Arial", 20), width=5, height=2, command=lambda: add_operator("/"))
Divide.grid(row=3, column=3)

window.mainloop()
