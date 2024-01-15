import sqlite3

class ImportModel:
    def __init__(self):
        self.data = None
        self.dbName = "database.db"
        self.connection = sqlite3.connect(self.dbName)
        self.create_table()

    def set_data(self, data):
        self.data = data
    
    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, lastname TEXT, firstname TEXT)''')
        self.connection.commit()

    def import_data(self):
        connection = sqlite3.connect(self.dbName)
        cursor = connection.cursor()
        total_records = len(self.data)
        for index, record in enumerate(self.data):
            # Insert your data into the SQLite database
            # Replace the following line with your actual SQL query
            cursor.execute("INSERT INTO items (id, lastname, firstname) VALUES (NULL,?, ?)", record)
           
            # Update progress every 10 records (adjust as needed)
            if index % 10 == 0:
                progress_percentage = int((index / total_records) * 100)
                yield progress_percentage

        connection.commit()
        connection.close()
