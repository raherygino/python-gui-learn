import sys
from PyQt5.QtWidgets import QApplication
from app import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = StudentModel()
    view = StudentView()
    presenter = StudentPresenter(view, model)
    view.show()
    
    sys.exit(app.exec_())