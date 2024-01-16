from PyQt5.QtWidgets import (QFileDialog)

class Functions():

    def dialogSaveFile(self, title, directory, typeFile): 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(title, directory, typeFile, options=options)
        return fileName
    