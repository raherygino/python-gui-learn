import sys
from PyQt5.QtWidgets import QApplication
from app import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = ImportModel()
    view = ImportView()
    presenter = ImportPresenter(view, model)
    view.show()

    sys.exit(app.exec_())