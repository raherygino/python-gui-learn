from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QPushButton

class ImportView(QWidget):
    start_import_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SQLite Data Import')
        self.setGeometry(100, 100, 400, 200)

        self.progress_bar = QProgressBar(self)
        self.start_button = QPushButton('Start Import', self)
        self.start_button.clicked.connect(self.start_import_signal.emit)

        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def reset_progress_bar(self):
        self.progress_bar.setValue(0)

    def generate_dummy_data(self):
        # Replace this with your actual data
        return [(i, f"value_{i}") for i in range(1000)]
