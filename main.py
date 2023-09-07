import sqlite3
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

if __name__ == "__main__":
    try:
        connection = sqlite3.connect("./databases/contacts.db")
        db = connection.cursor()
        res = db.execute("SELECT * FROM contactos")
        print(res.fetchone())
    except Exception as e:
        print(e)

app = App()

app.master.title("App")
app.master.maxsize(1000,400)

app.mainloop()
