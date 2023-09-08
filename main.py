import sqlite3
import logging
import tkinter as tk
from tkinter import ttk
from modules.main_menu import Menu 
from modules.all_contacts import All 
from modules.add_contact import Add
from modules.edit_contact import Edit
from modules.dbqueries import DB

logging.basicConfig(filename="logs.log", encoding='utf-8', level=logging.DEBUG)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
         
        logging.info('Creating Tkinter frame container')
        container = tk.Frame(self) 
        container.pack()
        logging.info('Creating frames')

        self.frames = {} 
        for F in (Menu, All, Add, Edit):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")        

        self.show_frame(Menu)

    def show_frame(self, cont):
        logging.info(f'Rendering {cont}')
        self.frames[cont].tkraise()
        self.frames[cont].update()
        self.frames[cont].event_generate("<<ShowFrame>>")


    def go_back(self):
        logging.info(f'Rendering {Menu}')
        self.frames[Menu].tkraise()
        self.frames[Menu].update()
        self.frames[Menu].event_generate("<<ShowFrame>>")


if __name__ == "__main__":
    DB.check_table_exists()

app = App()
app.title("Agenda de contactos")
app.geometry("1000x500")
app.resizable(False, False)
app.mainloop()
DB.close()
