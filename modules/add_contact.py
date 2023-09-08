import sqlite3
import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
