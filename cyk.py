from glob import glob
import tkinter as tk
from tkinter import messagebox

def do_maths():
    global selected
    a = first_number.get()
    b = second_number.get()
    if selected.get() == 0:
        try:
            a = float(a)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            first_number.focus_set()
        try:
            b = float(b)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            second_number.focus_set()
        else:
            messagebox.showinfo("Result",f'{a} + {b} = {float(a)+float(b)}')
    if selected.get() == 1:
        try:
            a = float(a)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            first_number.focus_set()
        try:
            b = float(b)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            second_number.focus_set()
        else:
            messagebox.showinfo("Result",f'{a} - {b} = {float(a)-float(b)}')
    if selected.get() == 2:
        try:
            a = float(a)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            first_number.focus_set()
        try:
            b = float(b)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            second_number.focus_set()
        else:
            messagebox.showinfo("Result",f'{a} * {b} = {float(a)*float(b)}')
    if selected.get() == 3:
        try:
            a = float(a)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            first_number.focus_set()
        try:
            b = float(b)
        except ValueError:
            messagebox.showerror("Error","Your value is incorrect")
            second_number.focus_set()
        else:
            try:
                messagebox.showinfo("Result",f'{a} / {b} = {float(a)/float(b)}')
            except ZeroDivisionError:
                messagebox.showerror("Error","You cannot divide by 0")
                second_number.focus_set()
            


window = tk.Tk()
first_number = tk.Entry(window)
second_number = tk.Entry(window)
math_options = tk.Frame(window)
result_button = tk.Button(window, text="Evaluate", command=do_maths)

selected = tk.IntVar()
add = tk.Radiobutton(math_options, text="+", value=0, variable=selected)
sub = tk.Radiobutton(math_options, text="-", value=1, variable=selected)
mul = tk.Radiobutton(math_options, text="*", value=2, variable=selected)
div = tk.Radiobutton(math_options, text="/", value=3, variable=selected)
add.grid(row=0)
sub.grid(row=1)
mul.grid(row=2)
div.grid(row=3)



first_number.grid(row=0, column=0)
math_options.grid(row=0, column=1)
second_number.grid(row=0, column=2)
result_button.grid(row=1, column=1)

window.mainloop()