import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import random


def initial_state():
    my_font = font.Font(family="Arial", weight="bold", size=25)
    pos = random.randint(0,8)
    buttons[pos]["text"] = "X"
    buttons[pos]["fg"] = "red"
    buttons[pos]["font"] = my_font

def change_turn(x):
    global counter
    if buttons[x]["text"] == "":
        my_font = font.Font(family="Arial", weight="bold", size=25)
        buttons[x]["text"] = "O"
        buttons[x]["fg"] = "green"
        buttons[x]["font"] = my_font
        counter += 1

        winner = None
        if counter >= 4:
            winner = check_winner()
            if winner:
                messagebox.showinfo("Game Over!",f'Winner is {winner}')
                window.destroy()

        if not winner:
            while True:
                pos = random.randint(0,8)
                if buttons[pos]["text"] == "":
                    break
            my_font = font.Font(family="Arial", weight="bold", size=25)
            buttons[pos]["text"] = "X"
            buttons[pos]["fg"] = "red"
            buttons[pos]["font"] = my_font
            counter += 1
        
            if counter >= 4:
                winner = check_winner()
                if winner:
                    messagebox.showinfo("Game Over!",f'Winner is {winner}')
                    window.destroy()
                elif counter == 8:
                    messagebox.showinfo("Game Over!", "Tie!")
                    window.destroy()

def check_winner():
    sign = ""
    if buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"]:
        sign = buttons[0]["text"]
    elif buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"]:
        sign = buttons[3]["text"]
    elif buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"]:
        sign = buttons[6]["text"]

    elif buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"]:
        sign = buttons[0]["text"]
    elif buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"]:
        sign = buttons[1]["text"]
    elif buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"]:
        sign = buttons[2]["text"]

    elif buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"]:
        sign = buttons[0]["text"]
    elif buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"]:
        sign = buttons[2]["text"]
    
    if sign == "X" or sign == "O":
        return sign
    return False

window = tk.Tk()
window.title("TicTacToe")
buttons = []
row = 0
col = 0
pixel = tk.PhotoImage(width=1, height=1)
for i in range(9):
    button = tk.Button(window, width=70, height=70, image=pixel, compound="center", command=lambda x=i: change_turn(x))
    buttons.append(button)
    button.grid(row=row, column=col)
    if col == 2:
        row += 1
    if col < 2:
        col += 1
    else:
        col = 0


initial_state()
counter = 0
window.mainloop()


