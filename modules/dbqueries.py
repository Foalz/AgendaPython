import sqlite3

class Database():
    def __init__(self, table):
        self.table = table
        self.con = sqlite3.connect("./databases/contactos.db")

    def get_all(self):
        cursor = self.con.execute(f"SELECT * FROM {self.table};")
        return cursor
    
    def get_by_id(self, rowid):
        cursor = self.con.execute(f"SELECT FROM {self.table} WHERE rowid={rowid};")
        return cursor

    def update(self, rowid):
        cursor = self.con.execute(f"SELECT FROM {self.table} WHERE rowid={rowid};")




