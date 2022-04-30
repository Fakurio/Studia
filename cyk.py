import tkinter as tk


def draw_circle(x, y, r, canvas_name):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, width=3, fill="lightgrey")

def initial_state():
    for i in range(3):
        if phases[0][0]:
            canvas.itemconfig(red, fill="red") 
        if phases[0][1]:
            canvas.itemconfig(yellow, fill="yellow") 
        if phases[0][2]:
            canvas.itemconfig(green, fill="green") 

def change_state():
    global current_state
    current_state += 1
    if current_state == len(phases):
        current_state = 0
    if phases[current_state][0]:
        canvas.itemconfig(red, fill="red")
    else:
        canvas.itemconfig(red, fill="lightgrey")
    if phases[current_state][1]:
        canvas.itemconfig(yellow, fill="yellow") 
    else:
        canvas.itemconfig(yellow, fill="lightgrey")
    if phases[current_state][2]:
        canvas.itemconfig(green, fill="green")
    else:
        canvas.itemconfig(green, fill="lightgrey")


phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))


window = tk.Tk()
window.resizable(False, False)

canvas = tk.Canvas(window, bg="grey", height=400, width=200)
red = draw_circle(100, 70, 60, canvas)
yellow = draw_circle(100, 200, 60, canvas)
green = draw_circle(100, 330, 60, canvas)
next_button = tk.Button(window, text="Next", command=change_state)
quit_button = tk.Button(window, text="Quit", command=lambda: window.destroy())

current_state = 0
initial_state()

canvas.grid(row=0, column=0)
next_button.grid(row=1, column=0)
quit_button.grid(row=2, column=0)
window.mainloop()