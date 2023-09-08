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

        title = tk.Label(self, text="Menu Principal", font=("Arial", 25))
        title.grid(row = 1, column = 1)

        self.add_contact_icon = tk.PhotoImage(file = r"./assets/add-user.png")
        add_label = tk.Label(self, image=self.add_contact_icon)
        add_label.grid(row=2, column=0)
        add_contact_btn = tk.Button(self, text="Agregar Contacto", width=35, height=5,
        command = lambda : controller.show_frame(Add))
        add_contact_btn.grid(row=2, column=1, padx=10, pady=10)

        self.all_contact_icon = tk.PhotoImage(file = r"./assets/contacts.png")
        all_contacts_label = tk.Label(self, image=self.all_contact_icon)
        all_contacts_label.grid(row=3, column=0)
        all_contacts_btn = tk.Button(self, text="Ver todos los contactos", width=35, height=5,
        command = lambda : controller.show_frame(All))
        all_contacts_btn.grid(row=3, column=1, padx=10, pady=10)
