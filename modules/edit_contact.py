import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import Database

DB = Database("contactos")

class Edit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

