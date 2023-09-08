import sqlite3
import logging

logging.basicConfig(filename="logs.log", encoding='utf-8', level=logging.DEBUG)

class Database():
    def __init__(self, table):
        self.table = table
        try:
            logging.info(f'Connecting to sqlite database')
            self.con = sqlite3.connect("./databases/contactos.db")
            logging.info(f'Connected successfully')
        except Exception as e:
            logging.error(e)

    def check_table_exists(self):
        try:
            logging.info(f'Checking if {self.table}.db exists')
            cursor = self.con.execute(f"SELECT * FROM {self.table};")
            self.con.commit()
            logging.info(f'{self.table}.db already exists!')
        except Exception as e:
            logging.info(f'{self.table}.db does not exists, creating file...')
            cursor = self.con.execute(f"""
            CREATE TABLE {self.table} (
                nombre TEXT NOT NULL, 
                telefono TEXT NOT NULL, 
                email TEXT NOT NULL);
             """)
            self.con.commit()
            logging.info(f'{self.table}.db successfully created!')

    def close(self):
        logging.info(f'Program closed, ending database connection...')
        self.con.close()
        logging.info(f'Connection finished successfully')

    def get_all(self):
        try:
            logging.info(f'Getting all data from {self.table}')
            cursor = self.con.execute(f"SELECT * FROM {self.table};")
            self.con.commit()
            logging.info(f'Query executed successfully')
            return cursor
        except Exception as e:
            logging.error(e)
    
    def get_by_id(self, rowid):
        try:
            cursor = self.con.execute(f"SELECT * FROM {self.table} WHERE rowid={rowid};")
            self.con.commit()
            logging.info(f'Query executed successfully')
            return cursor
        except Exception as e:
            logging.error(e)

    def find(self, name):
        try:
            logging.info(f'Getting data by name on {self.table}')
            cursor = self.con.execute(f"SELECT * FROM {self.table} WHERE nombre='{name}';")
            self.con.commit()
            logging.info(f'Query executed successfully')
            return cursor
        except Exception as e:
            logging.error(e)    
    
    def add(self, data):
        try:
            logging.info(f'Adding record {data} on {self.table}')
            cursor = self.con.execute(f""" INSERT INTO {self.table} (nombre, telefono, email) VALUES ('{data[0]}','{data[1]}','{data[2]}');
            """)
            logging.info(f'Query executed successfully')
            self.con.commit()
        except Exception as e:
            logging.error(e)    


    def update(self, rowid):
        cursor = self.con.execute(f"SELECT FROM {self.table} WHERE rowid={rowid};")

DB = Database("contactos")



