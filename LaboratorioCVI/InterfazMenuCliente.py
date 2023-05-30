from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazBorrarCliente
import InterfazBuscarCliente
import InterfazCrearCliente
import InterfazEditar
import sys

import InterfazMenu


class MenuCliente(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Menu Cliente"))
        self.BotonCrear.setText(_translate("MainWindow", "CREAR"))
        self.BotonBuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.BotonEditar.setText(_translate("MainWindow", "EDITAR"))
        self.BotonBorrar.setText(_translate("MainWindow", "BORRAR"))
        self.Titulo.setText(_translate("MainWindow", "MENU CLIENTE"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(991, 521)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BotonCrear = QtWidgets.QPushButton(self.centralwidget)
        self.BotonCrear.setGeometry(QtCore.QRect(90, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonCrear.setFont(font)
        self.BotonCrear.setTabletTracking(True)
        self.BotonCrear.setAcceptDrops(True)
        self.BotonCrear.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonCrear.setAutoRepeatDelay(300)
        self.BotonCrear.setObjectName("BotonCrear")
        self.BotonBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonBuscar.setGeometry(QtCore.QRect(310, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonBuscar.setFont(font)
        self.BotonBuscar.setTabletTracking(True)
        self.BotonBuscar.setAcceptDrops(True)
        self.BotonBuscar.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonBuscar.setAutoRepeatDelay(300)
        self.BotonBuscar.setObjectName("BotonBuscar")
        self.BotonEditar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonEditar.setGeometry(QtCore.QRect(530, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonEditar.setFont(font)
        self.BotonEditar.setTabletTracking(True)
        self.BotonEditar.setAcceptDrops(True)
        self.BotonEditar.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonEditar.setAutoRepeatDelay(300)
        self.BotonEditar.setObjectName("BotonEditar")
        self.BotonBorrar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonBorrar.setGeometry(QtCore.QRect(760, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonBorrar.setFont(font)
        self.BotonBorrar.setTabletTracking(True)
        self.BotonBorrar.setAcceptDrops(True)
        self.BotonBorrar.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonBorrar.setAutoRepeatDelay(300)
        self.BotonBorrar.setObjectName("BotonBorrar")
        self.ImgCrearCliente = QtWidgets.QLabel(self.centralwidget)
        self.ImgCrearCliente.setGeometry(QtCore.QRect(110, 230, 91, 91))
        self.ImgCrearCliente.setStyleSheet("background-color: no color")
        self.ImgCrearCliente.setText("")
        self.ImgCrearCliente.setPixmap(QtGui.QPixmap("alo/CrearCliente.png"))
        self.ImgCrearCliente.setScaledContents(True)
        self.ImgCrearCliente.setObjectName("ImgCrearCliente")
        self.ImgEditarCliente = QtWidgets.QLabel(self.centralwidget)
        self.ImgEditarCliente.setGeometry(QtCore.QRect(540, 230, 101, 101))
        self.ImgEditarCliente.setStyleSheet("background-color: no color;")
        self.ImgEditarCliente.setText("")
        self.ImgEditarCliente.setPixmap(QtGui.QPixmap("alo/Editar.png"))
        self.ImgEditarCliente.setScaledContents(True)
        self.ImgEditarCliente.setObjectName("ImgEditarCliente")
        self.ImgBuscarCliente = QtWidgets.QLabel(self.centralwidget)
        self.ImgBuscarCliente.setGeometry(QtCore.QRect(320, 230, 91, 91))
        self.ImgBuscarCliente.setStyleSheet("background-color: no color;")
        self.ImgBuscarCliente.setText("")
        self.ImgBuscarCliente.setPixmap(QtGui.QPixmap("alo/Buscar.png"))
        self.ImgBuscarCliente.setScaledContents(True)
        self.ImgBuscarCliente.setObjectName("ImgBuscarCliente")
        self.ImgBorrarCiente = QtWidgets.QLabel(self.centralwidget)
        self.ImgBorrarCiente.setGeometry(QtCore.QRect(770, 230, 101, 101))
        self.ImgBorrarCiente.setStyleSheet("background-color: no color")
        self.ImgBorrarCiente.setText("")
        self.ImgBorrarCiente.setPixmap(QtGui.QPixmap("alo/Borrar.png"))
        self.ImgBorrarCiente.setScaledContents(True)
        self.ImgBorrarCiente.setObjectName("ImgBorrarCiente")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(90, 50, 781, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;")
        self.Titulo.setTextFormat(QtCore.Qt.AutoText)
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.Titulo.setObjectName("Titulo")
        self.Fondo = QtWidgets.QLabel(self.centralwidget)
        self.Fondo.setGeometry(QtCore.QRect(0, 0, 991, 521))
        self.Fondo.setMouseTracking(False)
        self.Fondo.setAcceptDrops(False)
        self.Fondo.setAutoFillBackground(False)
        self.Fondo.setStyleSheet("background-color: #F1F1F1;\n"
        "border-style: solid;\n"
        "border-color: #00A2FF;\n"
        "border-width: 10px;")
        self.Fondo.setText("")
        self.Fondo.setObjectName("Fondo")
        self.Fondo.raise_()
        self.BotonCrear.raise_()
        self.BotonBuscar.raise_()
        self.BotonEditar.raise_()
        self.BotonBorrar.raise_()
        self.ImgCrearCliente.raise_()
        self.ImgEditarCliente.raise_()
        self.ImgBuscarCliente.raise_()
        self.ImgBorrarCiente.raise_()
        self.Titulo.raise_()
        self.BotonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.BotonAtras.setGeometry(QtCore.QRect(920, 460, 41, 41))
        self.BotonAtras.setStyleSheet("background-color: no color;\n"
                                      "border-style: solid;\n"
                                      "border-width: 0px;")
        self.BotonAtras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alo/Atras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonAtras.setIcon(icon)
        self.BotonAtras.setIconSize(QtCore.QSize(40, 40))
        self.BotonAtras.setObjectName("BotonAtras")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BotonEditar.clicked.connect(lambda : self.cambio2(MainWindow,InterfazBuscarCliente.BuscarCliente,True))
        self.BotonBuscar.clicked.connect(lambda : self.cambio2(MainWindow,InterfazBuscarCliente.BuscarCliente,False))
        self.BotonBorrar.clicked.connect(lambda: self.cambio(MainWindow, InterfazBorrarCliente.BorrarCliente))
        self.BotonCrear.clicked.connect(lambda: self.cambio(MainWindow, InterfazCrearCliente.CrearCliente))
        self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazMenu.Menu))

    def cambio2(self, MainWindow,Interfaz,Bandera):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana,Bandera)
        self.ventana.show()
        MainWindow.close()

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()