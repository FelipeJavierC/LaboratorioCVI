from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazCrearCliente
import InterfazCrearMascota

numeroMascotas = 0

class NumeroMascotas(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(991, 521)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.NumeroMascotas = QtWidgets.QLineEdit(self.centralwidget)
        self.NumeroMascotas.setGeometry(QtCore.QRect(160, 300, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NumeroMascotas.setFont(font)
        self.NumeroMascotas.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.NumeroMascotas.setAccessibleDescription("")
        self.NumeroMascotas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NumeroMascotas.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.NumeroMascotas.setText("")
        self.NumeroMascotas.setAlignment(QtCore.Qt.AlignCenter)
        self.NumeroMascotas.setObjectName("NumeroMascotas")
        self.BotonConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonConfirmar.setGeometry(QtCore.QRect(430, 380, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonConfirmar.setFont(font)
        self.BotonConfirmar.setTabletTracking(True)
        self.BotonConfirmar.setAcceptDrops(True)
        self.BotonConfirmar.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonConfirmar.setAutoRepeatDelay(300)
        self.BotonConfirmar.setObjectName("BotonConfirmar")
        self.ImgMascota = QtWidgets.QLabel(self.centralwidget)
        self.ImgMascota.setGeometry(QtCore.QRect(440, 170, 111, 111))
        self.ImgMascota.setStyleSheet("background-color: no color;")
        self.ImgMascota.setText("")
        self.ImgMascota.setPixmap(QtGui.QPixmap("alo/Mascota.png"))
        self.ImgMascota.setScaledContents(True)
        self.ImgMascota.setObjectName("ImgMascota")
        self.Fondo.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.NumeroMascotas.raise_()
        self.BotonConfirmar.raise_()
        self.ImgMascota.raise_()
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(310, 353, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.TxtNoEncontrado.setFont(font)
        self.TxtNoEncontrado.setStyleSheet("background-color: no color;\n"
        "color:red;")
        self.TxtNoEncontrado.setTextFormat(QtCore.Qt.AutoText)
        self.TxtNoEncontrado.setAlignment(QtCore.Qt.AlignCenter)
        self.TxtNoEncontrado.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TxtNoEncontrado.setObjectName("TxtNoEncontrado")
        self.TxtNoEncontrado.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazCrearCliente.CrearCliente))
        self.BotonConfirmar.clicked.connect(lambda: self.guardar(MainWindow))


    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def guardar(self,MainWindow):
        global numeroMascotas
        try:
            numeroMascotas = int(self.NumeroMascotas.text())
        except:
            numeroMascotas = 0
        print(numeroMascotas)
        if numeroMascotas != 0:
            self.cambio2(MainWindow, InterfazCrearMascota.CrearMascota,True)
        else:
            self.TxtNoEncontrado.show()



    def cambio2(self, MainWindow,Interfaz,Bandera):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana,Bandera)
        self.ventana.show()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Numero De Mascotas"))
        self.Titulo.setText(_translate("MainWindow", "NUMERO DE MASCOTAS"))
        self.NumeroMascotas.setPlaceholderText(_translate("MainWindow", "INGRESE NUMERO DE MASCOTAS A INGRESAR"))
        self.BotonConfirmar.setText(_translate("MainWindow", "CONTINUAR"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Ingrese Un Numero Valido."))