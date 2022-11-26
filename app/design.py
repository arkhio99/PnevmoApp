# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_files/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import solver
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.predict_btn = QtWidgets.QPushButton(self.centralwidget)
        self.predict_btn.setGeometry(QtCore.QRect(10, 450, 781, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.predict_btn.setFont(font)
        self.predict_btn.setObjectName("predict_btn")
        self.pic_displayer = QtWidgets.QLabel(self.centralwidget)
        self.pic_displayer.setGeometry(QtCore.QRect(10, 0, 781, 441))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.pic_displayer.setFont(font)
        self.pic_displayer.setStyleSheet("background-image: url(resources/image1-7.jpg);")
        self.pic_displayer.setText("")
        self.pic_displayer.setPixmap(QtGui.QPixmap("resources/image1-7.jpg"))
        self.pic_displayer.setScaledContents(True)
        self.pic_displayer.setObjectName("pic_displayer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PnevmoApp"))
        self.predict_btn.setText(_translate("MainWindow", "Узнать, есть ли пневмония"))

    def BindButtons(self):
        self.predict_btn.clicked.connect(self.MakePrediction)

    def MakePrediction(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.predict_btn,"QFileDialog.getOpenFileName()", "","Images (*.jpeg *.jpg *.png *.bmp2)", options=options)
        self.pic_displayer.setPixmap(QtGui.QPixmap(fileName))
        prediction = "Пневмония отсутствует" if solver.solve(fileName) == 0 else "Пневмония присутствует"
        mb = QMessageBox()
        mb.setWindowTitle("Решение")
        mb.setText(prediction)
        mb.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


