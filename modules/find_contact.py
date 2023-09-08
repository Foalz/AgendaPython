import sqlite3
import tkinter as tk
from tkinter import ttk

class Find(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Buscar contacto",)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
