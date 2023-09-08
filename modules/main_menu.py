import sqlite3
import tkinter as tk
from tkinter import ttk
from .all_contacts import All
from .add_contact import Add
from .edit_contact import Edit
import os.path

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        add_contact_btn = ttk.Button(self, text="Agregar Contacto",
        command = lambda : controller.show_frame(Add))
        add_contact_btn.grid(row=1, column=1, padx=10, pady=10)

        all_contacts_btn = ttk.Button(self, text="Ver todos los contactos",
        command = lambda : controller.show_frame(All))
        all_contacts_btn.grid(row=2, column=0, padx=10, pady=10)

        find_contacts_btn = ttk.Button(self, text="Ver todos los contactos",
        command = lambda : controller.show_frame(All))
        find_contacts_btn.grid(row=2, column=0, padx=10, pady=10)
