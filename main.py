import sqlite3
import tkinter as tk
from tkinter import ttk
from modules.main_menu import Menu 
from modules.all_contacts import All 
from modules.add_contact import Add
from modules.dbqueries import DB

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack()

        self.frames = {} 
        for F in (Menu, All, Add):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")        

        self.show_frame(Menu)

    def show_frame(self, cont):
        self.frames[cont].tkraise()
        self.frames[cont].update()
        self.frames[cont].event_generate("<<ShowFrame>>")


    def go_back(self):
        self.frames[Menu].tkraise()
        self.frames[Menu].update()
        self.frames[Menu].event_generate("<<ShowFrame>>")


if __name__ == "__main__":
    DB.check_table_exists()

app = App()
app.geometry("500x500")
app.mainloop()
DB.close()
