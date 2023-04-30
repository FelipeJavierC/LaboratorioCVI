from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazBorrado
import InterfazEditar
import main

class BorrarMascota(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(991, 521)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImgBorrar = QtWidgets.QLabel(self.centralwidget)
        self.ImgBorrar.setGeometry(QtCore.QRect(440, 160, 111, 111))
        self.ImgBorrar.setStyleSheet("background-color: no color;")
        self.ImgBorrar.setText("")
        self.ImgBorrar.setPixmap(QtGui.QPixmap("alo/Mascota.png"))
        self.ImgBorrar.setScaledContents(True)
        self.ImgBorrar.setObjectName("ImgBorrar")
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
        self.BuscarNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.BuscarNombre.setGeometry(QtCore.QRect(90, 300, 781, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.BuscarNombre.setFont(font)
        self.BuscarNombre.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarNombre.setAccessibleDescription("")
        self.BuscarNombre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BuscarNombre.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BuscarNombre.setText("")
        self.BuscarNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.BuscarNombre.setObjectName("BuscarRut")
        self.ImgLupa = QtWidgets.QLabel(self.centralwidget)
        self.ImgLupa.setGeometry(QtCore.QRect(97, 304, 51, 51))
        self.ImgLupa.setStyleSheet("background-color: no color;")
        self.ImgLupa.setText("")
        self.ImgLupa.setPixmap(QtGui.QPixmap("alo/Lupa.png"))
        self.ImgLupa.setScaledContents(True)
        self.ImgLupa.setObjectName("ImgLupa")
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
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(300, 270, 371, 21))
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
        self.Fondo.raise_()
        self.ImgBorrar.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.BuscarNombre.raise_()
        self.ImgLupa.raise_()
        self.BotonConfirmar.raise_()
        self.TxtNoEncontrado.raise_()
        self.TxtNoEncontrado.setHidden(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazEditar.Editar))
        self.BotonConfirmar.clicked.connect(lambda: self.guardar())

    def abrir(self,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def guardar(self):
        nombre = self.BuscarNombre.text()
        mascota = main.BuscarMascota(nombre)
        if mascota != False:
            main.borrarMascota(nombre)
            self.abrir(InterfazBorrado.Borrado)
        else:
            self.TxtNoEncontrado.show()

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Borrar Mascota"))
        self.Titulo.setText(_translate("MainWindow", "BORRAR MASCOTA"))
        self.BuscarNombre.setPlaceholderText(_translate("MainWindow", "INGRESE EL NOMBRE DE LA MASCOTA A BORRAR"))
        self.BotonConfirmar.setText(_translate("MainWindow", "CONFIRMAR"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "No se pudo encontrar la mascota. Vuelva a intentar."))