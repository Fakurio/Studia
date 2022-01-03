import tkinter as tk
import math

class Trygo:
    label_width = 22
    
    def __init__(self, parent):
        self.parent = parent
        self.container = tk.Frame(self.parent, bg="#ffcc99", pady=10)
        self.input = tk.Label(self.container, text="Podaj kąt w stopniach:", width=Trygo.label_width)     
        self.kat_input = tk.Entry(self.container)
        self.calculate_button = tk.Button(self.container, text="Oblicz", width=10, command=self.calculate_trygo)
        self.menu_button = tk.Button(self.container, text="Menu", width=10, command=self.return_menu) 

        self.parent.bind("<Return>", self.enter_click)
        self.kat_input.focus()

        self.container.pack()
        self.input.grid(column=0, row=0)
        self.kat_input.grid(column=1, row=0, padx=5, pady=1)
        self.calculate_button.grid(column=2, row=0, padx=5)
        self.menu_button.grid(column=3, row=0)

    def enter_click(self, event):
        self.calculate_trygo()
    
    def calculate_trygo(self):
        if hasattr(self,"error"):
            self.error.destroy()
        if hasattr(self,"result_container"):
            self.result_container.destroy()

        self.kat = self.kat_input.get()
        try:
            self.kat_w_rad= math.radians(float(self.kat))
            self.sinus = round(math.sin(self.kat_w_rad),2)
            self.cosin = round(math.cos(self.kat_w_rad),2)
            if not float(self.kat)%180:
                self.tg = 0
                self.ctg = "brak"
            elif not float(self.kat)%90:
                self.tg = "brak"
                self.ctg = 0
            else:
                self.tg = round(math.tan(self.kat_w_rad),2)
                self.ctg = round(1/self.tg,2)


            self.result_container = tk.Frame(self.container)
            self.sinus_result = tk.Label(self.result_container, text="Sinus z "+self.kat+" = ",width=Trygo.label_width, anchor="e")      
            self.cosin_result = tk.Label(self.result_container, text="Cosinus z "+self.kat+" = ",width=Trygo.label_width, anchor="e")        
            self.tg_result = tk.Label(self.result_container, text="Tangens z "+self.kat+" = ",width=Trygo.label_width, anchor="e")        
            self.ctg_result = tk.Label(self.result_container, text="Contangens z "+self.kat+" = ",width=Trygo.label_width, anchor="e")     
            
            self.result_container.grid(columnspan=2, row=1, sticky="w", pady=10)
            self.sinus_result.grid(row=0, column=0)
            tk.Label(self.result_container, text=str(self.sinus)).grid(row=0, column=1)
            self.cosin_result.grid(row=1, column=0)
            tk.Label(self.result_container, text=str(self.cosin)).grid(row=1, column=1)
            self.tg_result.grid(row=2, column=0)
            tk.Label(self.result_container, text=str(self.tg)).grid(row=2, column=1)
            self.ctg_result.grid(row=3, column=0)
            tk.Label(self.result_container, text=str(self.ctg)).grid(row=3, column=1)
        except ValueError:
            if hasattr(self,"result_container"):
                self.result_container.destroy()
            self.error = tk.Label(self.container,text="BŁĘDNE DANE", fg="red", width=Trygo.label_width)
            self.error.grid(column=0, row=1, pady=10)

    def return_menu(self):
        import menu
        self.container.destroy()
        self.menu_page = menu.App(self.parent)
        