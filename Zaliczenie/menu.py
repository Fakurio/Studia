import tkinter as tk

class App:
    label_width = 22
    
    def __init__(self, master):
        self.master = master
        self.master.title("Przykładowe operacje z biblioteką math")
        self.master.geometry("480x300")
        self.master.configure(bg="#ffcc99")
        
        self.container = tk.Frame(self.master, bg="#ffcc99")
        self.trygo_button = tk.Button(self.container, text="Funkcje trygonometryczne", bg="lightgreen", height=3, width=App.label_width, command=self.trygo)
        self.log_button = tk.Button(self.container, text="Oblicz logarytm", bg="lightgreen", height=3, width=App.label_width, command=self.log)
        self.sqrt_button = tk.Button(self.container, text="Oblicz pierwiastek", bg="lightgreen", height=3, width=App.label_width, command=self.sqrt)

        self.container.pack()
        self.trygo_button.grid(column=1, row=0, pady=15)
        self.log_button.grid(column=1, row=1, pady=15)
        self.sqrt_button.grid(column=1, row=2, pady=15)
    
    def trygo(self):
        import trygonometria
        self.container.destroy()
        self.trygo_page = trygonometria.Trygo(self.master)
    
    def log(self):
       import logarytm
       self.container.destroy()
       self.log_page = logarytm.Log(self.master)

    def sqrt(self):
        import pierwiastek
        self.container.destroy()
        self.sqrt_page = pierwiastek.Sqrt(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()