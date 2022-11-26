from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow

import sys

def application():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.BindButtons()
    MainWindow.show()
    sys.exit(app.exec_())

application()
