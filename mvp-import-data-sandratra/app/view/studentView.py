import os
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit,
                              QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QProgressBar)
from PyQt5.QtCore import pyqtSignal
from ..model.entity.student import Student

class StudentView(QMainWindow):
    start_import_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Filename (Path):")
        self.name_edit = QLineEdit()
        self.name_edit.setReadOnly(True)

        self.add_file_button = QPushButton("Add file CSV")

        self.import_button = QPushButton("Import")
        self.import_button.clicked.connect(self.start_import_signal.emit)
        self.progress_bar = QProgressBar(self)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Firstname"])

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.add_file_button)
        self.layout.addWidget(self.import_button)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.table)

        self.central_widget.setLayout(self.layout)

    def dialogSaveFile(self, title:str, directory:str, typeFile:str): 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,title, directory, typeFile, options=options)
        return fileName
    
    def openFile(self):
        filename = self.dialogSaveFile("Import CSV", f"{os.path.expanduser('~')}\Documents",  "CSV File (*.csv)")
        if filename:
            self.name_edit.setText(filename)
    
    
    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def reset_progress_bar(self):
        self.progress_bar.setValue(0)

  
    def populate_table(self, items):
        self.table.setRowCount(0)
        for row, item in enumerate(items):
            self.table.insertRow(row)
            for col, value in enumerate(item):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))