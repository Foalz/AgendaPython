import sqlite3
import tkinter as tk
from tkinter import ttk
from .add_contact import Add
from .find_contact import Find

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        add_contact_btn = ttk.Button(self, text="Agregar Contacto",
        command = lambda : controller.show_frame(Find))
        add_contact_btn.grid(row=1, column=1, padx=10, pady=10)
