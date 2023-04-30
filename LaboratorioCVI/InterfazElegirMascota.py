from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazDatosMascota
import InterfazDetalle
import InterfazEditar
import InterfazEditarMascota
import main


class ElegirMascota(object):
    def setupUi(self, MainWindow,Bandera):
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
        self.BotonContinuar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonContinuar.setGeometry(QtCore.QRect(430, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonContinuar.setFont(font)
        self.BotonContinuar.setTabletTracking(True)
        self.BotonContinuar.setAcceptDrops(True)
        self.BotonContinuar.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonContinuar.setAutoRepeatDelay(300)
        self.BotonContinuar.setObjectName("BotonContinuar")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(150, 280, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.MascotaEditar = QtWidgets.QComboBox(self.centralwidget)
        self.MascotaEditar.setGeometry(QtCore.QRect(420, 280, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MascotaEditar.setFont(font)
        self.MascotaEditar.setObjectName("MascotaEditar")
        self.MascotaEditar.addItem("")
        self.MascotaEditar.setItemText(0, "")
        self.Fondo.raise_()
        self.ImgBorrar.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.BotonContinuar.raise_()
        self.text.raise_()
        self.MascotaEditar.raise_()
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(300, 350, 371, 21))
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

        for i in main.cliente.mascotas:
            self.MascotaEditar.addItem(f"{i.nombreM}")


        if Bandera == True:
            self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazDetalle.Detalle))

        else:
            self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazEditar.Editar))
        self.BotonContinuar.clicked.connect(lambda: self.guardar(Bandera,MainWindow))

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def cambio2(self, MainWindow,Interfaz,mascota):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana,mascota)
        self.ventana.show()
        MainWindow.close()

    def guardar(self, Bandera, MainWindow):
        nombre = self.MascotaEditar.currentText()
        mascota = main.BuscarMascota(nombre)
        if mascota != False:
            if Bandera == True:
                self.cambio2(MainWindow, InterfazDatosMascota.DatosMascota,mascota)

            else:
                self.cambio2(MainWindow, InterfazEditarMascota.EditarMascota,mascota)
        else:
            self.TxtNoEncontrado.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Elegir Mascota"))
        self.Titulo.setText(_translate("MainWindow", "ELEGIR MASCOTA"))
        self.BotonContinuar.setText(_translate("MainWindow", "CONTINUAR"))
        self.text.setText(_translate("MainWindow", "MASCOTA:"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "No se pudo encontrar la mascota. Vuelva a intentar."))