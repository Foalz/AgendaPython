import sqlite3

class Database():
    def __init__(self, table):
        self.table = table
        self.con = sqlite3.connect("./databases/contactos.db")

    def get_all(self):
        cursor = self.con.execute(f"SELECT * FROM {self.table};")
        return cursor
    
    def get_by_id(self, rowid):
        cursor = self.con.execute(f"SELECT * FROM {self.table} WHERE rowid={rowid};")
        return cursor
    
    def add(self, data):
        print(f"""
        INSERT INTO {self.table} (nombre, telefono, email) VALUES ({data[0]}, {data[1]}, {data[2]});
        """)
        cursor = self.con.execute(f""" INSERT INTO {self.table} (nombre, telefono, email) VALUES ('{data[0]}','{data[1]}','{data[2]}');
        """)
        self.con.commit()

    def update(self, rowid):
        cursor = self.con.execute(f"SELECT FROM {self.table} WHERE rowid={rowid};")




