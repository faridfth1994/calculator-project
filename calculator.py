import tkinter as tk


class calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("480*620")
        self.result = tk.Entry(self, font=("Arial", 36))
        self.result.grid(row=0, column=0, columnspan=4, padx=10,
                         pady=10, ipadx=40, ipady=20, sticky=tk.W+tk.E)
        self.result.config(justify=tk.LEFT)
        self.grid_columnconfigure(0,weight=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        

        