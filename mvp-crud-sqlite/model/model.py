from PyQt5.QtCore import Qt
import sqlite3

class Model:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, firstname)''')
        self.conn.commit()

    def fetch_all_items(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM items''')
        return cursor.fetchall()

    def add_item(self, name, firstname):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO items (name, firstname) VALUES (?,?)''', (name,firstname,))
        self.conn.commit()

    def update_item(self, item_id, new_name):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE items SET name=? WHERE id=?''', (new_name, item_id))
        self.conn.commit()

    def delete_item(self, item_id):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM items WHERE id=?''', (item_id,))
        self.conn.commit()