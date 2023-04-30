from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Borrado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(262, 220)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Fondo = QtWidgets.QLabel(self.centralwidget)
        self.Fondo.setGeometry(QtCore.QRect(0, 0, 262, 220))
        self.Fondo.setMouseTracking(False)
        self.Fondo.setAcceptDrops(False)
        self.Fondo.setAutoFillBackground(False)
        self.Fondo.setStyleSheet("background-color: #F1F1F1;")
        self.Fondo.setText("")
        self.Fondo.setObjectName("Fondo")
        self.ImgBorrado = QtWidgets.QLabel(self.centralwidget)
        self.ImgBorrado.setGeometry(QtCore.QRect(30, 0, 211, 221))
        self.ImgBorrado.setStyleSheet("background-color: no color;")
        self.ImgBorrado.setText("")
        self.movi = QMovie("alo/Borrado.gif")
        self.ImgBorrado.setMovie(self.movi)
        self.movi.start()
        self.ImgBorrado.setScaledContents(True)
        self.ImgBorrado.setObjectName("ImgBorrar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Se Ha Borrado Con Exito"))