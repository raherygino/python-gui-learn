import sys
from PyQt5.QtWidgets import QApplication
from model import *
from presenter import *
from view import *

def main():
    app = QApplication(sys.argv)
    model = Model()
    view = View()
    presenter = Presenter(view, model)
    view.presenter = presenter
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
