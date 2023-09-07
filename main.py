import sqlite3


if __name__ == "__main__":
    try:
        connection = sqlite3.connect("./databases/contacts.db")
        db = connection.cursor()
        res = db.execute("SELECT * FROM contactos")
        print(res.fetchone())
    except Exception as e:
        print(e)

