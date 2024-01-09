from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()

        self.firstname_label = QLabel("Firstname:")
        self.firstname_edit = QLineEdit()

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_clicked)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Firstname"])

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.firstname_label)
        self.layout.addWidget(self.firstname_edit)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.table)

        self.central_widget.setLayout(self.layout)

    def add_clicked(self):
        name = self.name_edit.text()
        firstname = self.firstname_edit.text()
        self.presenter.add_item(name, firstname)
        self.name_edit.clear()
        self.firstname_edit.clear()

    def populate_table(self, items):
        self.table.setRowCount(0)
        for row, item in enumerate(items):
            self.table.insertRow(row)
            for col, value in enumerate(item):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))