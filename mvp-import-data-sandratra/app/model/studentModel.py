import sqlite3
import dataclasses
from .entity.student import Student
from .entity.entity import Entity

class StudentModel:
    fields = ['id']
    def __init__(self):
        self.data = None
        self.dbName = "database.db"
        self.table = "student"
        self.connection = sqlite3.connect(self.dbName)
        self.create_table(Student())

    def create_table(self, obj):
        cursor = self.connection.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {self.table}("
        query += f"id_{self.table} INTEGER PRIMARY KEY, "
        
        for field in dataclasses.fields(obj):
            fieldType = str(field.type)
            if (fieldType.find('str') != -1):
                fieldType = "TEXT"
            else:
                fieldType = "INTEGER"
            query += f"{field.name} {fieldType}, "

        query += "updated_at, created_at DATETIME)"
        cursor.execute(query)
        self.connection.commit()
    
    def set_data(self, data):
        self.data = data
    
    def create(self, cursor, student: Student):
        fieldsEntity = dataclasses.fields(student)
        values = ','.join([f'"{student.get(field.name)}"' for field in fieldsEntity])
        fields = ','.join([f'"{field.name}"' for field in fieldsEntity])
        sql = f"INSERT INTO {self.table}({fields}) VALUES ({values})"
        return cursor.execute(sql)

    def import_data(self):
        connection = sqlite3.connect(self.dbName)
        cursor = connection.cursor()
        total_records = len(self.data)
        for index, student in enumerate(self.data):
            # Insert your data into the SQLite database
            self.create(cursor, student)
            # Update progress every 10 records (adjust as needed)
            if index % 10 == 0:
                progress_percentage = int((index / total_records) * 100)
                yield progress_percentage

        connection.commit()
        connection.close()

