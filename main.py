import sqlite3
import tkinter as tk
from tkinter import ttk
from modules.main_menu import Menu 
from modules.find_contact import Find

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True)

        self.frames = {} 
        for F in (Menu, Find):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")        

        self.show_menu()

    def show_menu(self, cont=None):
        self.frames[Menu].tkraise()


if __name__ == "__main__":
    try:
        connection = sqlite3.connect("./databases/contactos.db")
        db = connection.cursor()
        res = db.execute("SELECT * FROM contactos;")
        print(res.fetchone())
    except Exception as e:
        print(e)
        connection = sqlite3.connect("./databases/contactos.db")
        db = connection.cursor()
        res = db.execute("""
        CREATE TABLE contactos (
            rowid int primary key, 
            nombre text not null, 
            telefono text, 
            email text);
         """)

app = App()
app.mainloop()
