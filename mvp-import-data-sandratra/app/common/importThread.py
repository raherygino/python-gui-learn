from PyQt5.QtCore import QThread, pyqtSignal

class ImportThread(QThread):
    update_progress = pyqtSignal(int)

    def __init__(self, import_model):
        super().__init__()
        self.import_model = import_model

    def run(self):
        for progress in self.import_model.import_data():
            self.update_progress.emit(progress+1)