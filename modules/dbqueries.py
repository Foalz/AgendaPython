import sqlite3

class Database():
    def __init__(self, table):
        self.table = table
        self.con = sqlite3.connect("./databases/contactos.db")
        print('initialized')

    def check_table_exists(self):
        try:
            cursor = self.con.execute(f"SELECT * FROM {self.table};")
            self.con.commit()
            print(f'Table {self.table} exists!')
        except Exception as e:
            cursor = self.con.execute(f"""
            CREATE TABLE {self.table} (
                nombre TEXT NOT NULL, 
                telefono TEXT NOT NULL, 
                email TEXT NOT NULL);
             """)
            self.con.commit()

    def close(self):
        self.con.close()
        print('closed')

    def get_all(self):
        cursor = self.con.execute(f"SELECT * FROM {self.table};")
        self.con.commit()
        return cursor
    
    def get_by_id(self, rowid):
        cursor = self.con.execute(f"SELECT * FROM {self.table} WHERE rowid={rowid};")
        self.con.commit()
        return cursor

    def find(self, name):
        cursor = self.con.execute(f"SELECT * FROM {self.table} WHERE nombre='{name}';")
        self.con.commit()
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

DB = Database("contactos")



