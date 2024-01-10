import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
import time

class WorkerThread(QThread):
    update_progress = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # Simulate some work
            self.update_progress.emit(i)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        start_button = QPushButton('Start', self)
        start_button.clicked.connect(self.start_progress)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def start_progress(self):
        self.worker_thread = WorkerThread()
        self.worker_thread.update_progress.connect(self.update_progress)
        self.worker_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())