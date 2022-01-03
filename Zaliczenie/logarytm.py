import tkinter as tk
from math import log

class Log:
    label_width = 25

    def __init__(self, parent):
        self.parent = parent
        self.container = tk.Frame(self.parent, bg="#ffcc99", pady=10)
        self.base = tk.Label(self.container, text="Podaj podstawę logarytmu:", width=Log.label_width)
        self.number = tk.Label(self.container, text="Podaj liczbę do zlogarytmowania:", width=Log.label_width)
        self.base_input = tk.Entry(self.container)
        self.number_input = tk.Entry(self.container)
        self.calculate_button = tk.Button(self.container, text="Oblicz", width=10, command=self.calculate_log)
        self.menu_button = tk.Button(self.container, text="Menu", width=10, command=self.return_menu) 

        self.parent.bind("<Return>", self.enter_click)
        self.base_input.focus()

        self.container.pack()
        self.base.grid(column=0, row=0)
        self.base_input.grid(column=1, row=0, padx=10, pady=10)
        self.calculate_button.grid(column=2, row=0)
        self.number.grid(column=0, row=1)
        self.number_input.grid(column=1, row=1, padx=10)
        self.menu_button.grid(column=2, row=1)

    def enter_click(self, event):
        self.calculate_log()
    
    def calculate_log(self):
        if hasattr(self, "error"):
            self.error.destroy()
        if hasattr(self, "result_container"):
            self.result_container.destroy()
        
        self.base_number = self.base_input.get()
        self.number_number = self.number_input.get()
        try:
            self.base_number = float(self.base_number)
            self.number_number = float(self.number_number)
            if self.base_number <= 0 or self.base_number == 1:
                raise ValueError
            if self.number_number <= 0:
                raise ValueError
            self.result = round(log(self.number_number, self.base_number),2)

            self.result_container = tk.Frame(self.container, width=Log.label_width)
            self.log = tk.Label(self.result_container, text="Logarytm o podstawie "+str(self.base_number)+" z "+str(self.number_number)+" = ", anchor="e")
            self.log_result = tk.Label(self.result_container, text=str(self.result))

            self.result_container.grid(columnspan=2, row=2, pady=10, sticky="w")
            self.log.grid(column=0, row=0)
            self.log_result.grid(column=1, row=0)
        except ValueError:
            if hasattr(self, "result_container"):
                self.result_container.destroy()
            self.error = tk.Label(self.container,text="BŁĘDNE DANE", fg="red", width=Log.label_width)
            self.error.grid(column=0, row=2, pady=10)

    def return_menu(self):
        import menu
        self.container.destroy()
        self.menu_page = menu.App(self.parent)