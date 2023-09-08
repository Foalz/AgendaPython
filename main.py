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
        container.pack()

        self.frames = {} 
        for F in (Menu, Find):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")        

        self.show_frame(Menu)

    def show_frame(self, cont):
        self.frames[cont].tkraise()


if __name__ == "__main__":
    try:
        db = sqlite3.connect("./databases/contactos.db")
        cursor = db.execute("SELECT * FROM contactos;")
        print([i for i in cursor])
        # db.execute("""
        # CREATE TABLE contactos (
            # nombre TEXT NOT NULL, 
            # telefono TEXT NOT NULL, 
            # email TEXT NOT NULL);
         # """)
        # db.commit()
        db.close()
    except Exception as e:
        print(e)
        db = sqlite3.connect("./databases/contactos.db")
        res = db.execute("""
        CREATE TABLE contactos (
            nombre TEXT NOT NULL, 
            telefono TEXT NOT NULL, 
            email TEXT NOT NULL);
         """)
        print(res.fetchone())
        db.commit()
        db.close()

app = App()
app.geometry("500x500")
app.mainloop()
