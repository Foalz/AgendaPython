import sqlite3
import tkinter as tk
from tkinter import ttk

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def add_contact(self, name="d", phone="123", email="123"):
        connection = sqlite3.connect("./databases/contactos.db")
        db = connection.cursor()
        res = db.execute(f"""
        INSERT INTO TABLE contactos (nombre, telefono, email)
        VALUES ('{name}', '{phone}', '{email}');
        """)


