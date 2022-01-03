import tkinter as tk
from math import sqrt

class Sqrt:
    label_width = 25
    
    def __init__(self, parent):
        self.parent = parent
        self.container = tk.Frame(self.parent, bg="#ffcc99", pady=10)
        self.input = tk.Label(self.container, text="Podaj liczbę podpierwiastkową:", width=Sqrt.label_width)
        self.number_input = tk.Entry(self.container)
        self.calculate_button = tk.Button(self.container, text="Oblicz", width=10, command=self.calculate_sqrt)
        self.menu_button = tk.Button(self.container, text="Menu", width=10, command=self.return_menu)

        self.parent.bind("<Return>", self.enter_click)
        self.number_input.focus()
        
        self.container.pack()
        self.input.grid(column=0, row=0)
        self.number_input.grid(column=1, row=0, pady=10, padx=10)
        self.calculate_button.grid(column=2, row=0)
        self.menu_button.grid(column=2, row=1)

    def enter_click(self, event):
        self.calculate_sqrt()
    
    def calculate_sqrt(self):
        if hasattr(self, "error"):
            self.error.destroy()
        if hasattr(self, "result_container"):
            self.result_container.destroy()
        
        self.number = self.number_input.get()
        try:
            self.number = float(self.number)
            if self.number < 0:
                raise ValueError
            self.result = round(sqrt(self.number),2)

            self.result_container = tk.Frame(self.container, width=Sqrt.label_width)
            self.sqrt = tk.Label(self.result_container, text="Pierwiastek z "+str(self.number)+" = ", anchor="e")
            self.sqrt_result = tk.Label(self.result_container, text=str(self.result))

            self.result_container.grid(columnspan=2, row=1, sticky="w")
            self.sqrt.grid(column=0, row=0)
            self.sqrt_result.grid(column=1, row=0)
        except ValueError:
            if hasattr(self, "result_container"):
                self.result_container.destroy()
            self.error = tk.Label(self.container,text="BŁĘDNE DANE", fg="red", width=Sqrt.label_width)
            self.error.grid(column=0, row=1)

    def return_menu(self):
        import menu
        self.container.destroy()
        self.menu_page = menu.App(self.parent)