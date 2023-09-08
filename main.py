import sqlite3
import tkinter as tk
from tkinter import ttk
from modules.main_menu import Menu 

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True)

        self.frameList = []
        self.frameList.append(Menu(container))
        self.show_menu()



    def show_menu(self, cont=None):
        self.frameList[0].tkraise()


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
