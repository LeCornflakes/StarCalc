import tkinter as tk

#Fenetre
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

#Functions

def add_number(number):
    display.insert(tk.END, number)

#def calculate():
#    result = eval(display.get())
#    display.delete(0, tk.END)
#    display.insert(0, result)

display = tk.Entry(window, font=("Arial", 24))
display.pack(fill="x", padx=10, pady=10)

#Buttons

Button1 = tk.Button(
    window,
    text="1",
    font=("Arial",20),
    command=lambda: add_number(1))
Button1.pack()

Button2 = tk.Button(
    window,
    text="2",
    font=("Arial",20),
    command=lambda: add_number(2))
Button2.pack()

Button3 = tk.Button(
    window,
    text="3",
    font=("Arial",20),
    command=lambda: add_number(3))
Button3.pack()

Button4 = tk.Button(
    window,
    text="4",
    font=("Arial",20),
    command=lambda: add_number(4))
Button4.pack()

Button5 = tk.Button(
    window,
    text="5",
    font=("Arial",20),
    command=lambda: add_number(5))
Button5.pack()

Button6 = tk.Button(
    window,
    text="6",
    font=("Arial",20),
    command=lambda: add_number(6))
Button6.pack()

Button7 = tk.Button(
    window,
    text="7",
    font=("Arial",20),
    command=lambda: add_number(7))
Button7.pack()

Button8 = tk.Button(
    window,
    text="8",
    font=("Arial",20),
    command=lambda: add_number(8))
Button8.pack()

Button9 = tk.Button(
    window,
    text="9",
    font=("Arial",20),
    command=lambda: add_number(9))
Button9.pack()

Equal = tk.Button(
    window,
    text="=",
    font=("Arial",20),
)
Equal.pack()

window.mainloop()