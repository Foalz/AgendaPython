import sqlite3
import tkinter as tk
from tkinter import ttk
from .add_contact import Add
from .find_contact import Find
import os.path

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        add_contact_btn = ttk.Button(self, text="Agregar Contacto",
        # command = lambda : controller.show_frame(Find))
        command = lambda : self.add_contact())
        add_contact_btn.grid(row=1, column=1, padx=10, pady=10)

    def add_contact(self, name="d", phone="123", email="123"):
        db = sqlite3.connect("./databases/contactos.db")
        res = db.execute(f"""
        INSERT INTO contactos (nombre, telefono, email)
        VALUES ('{name}', '{phone}', '{email}');
        """)
        print(res.fetchone())
        db.commit()
        db.close()
