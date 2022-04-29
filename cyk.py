import tkinter as tk
import random


def switch(index):
    if random_number[index] == min(random_number): 
        buttons[index]["state"] = "disabled"
        random_number[index] = 1000

def time():
    if not min(random_number) == 1000:
        timer["text"] += 1
        timer.after(1000, time)
    else:
        timer.after_cancel(timer)



window = tk.Tk()
window.title("Clicker")

buttons = []
r = 0
c = 0
random_number = random.sample(range(1,1000),25)
for i in range(25):
    buttons.append(tk.Button(window, text=str(random_number[i]), width=10, command=lambda index=i: switch(index)))
    buttons[i].grid(row=r, column=c)
    if c == 4:
        r += 1  
    if c < 4:   
        c += 1
    else:
        c = 0

timer = tk.Label(window, text=0)
timer.after(1000, time)
timer.grid(row=5, column=2)

window.mainloop()

