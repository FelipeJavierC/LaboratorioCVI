from PyQt5 import QtCore, QtGui, QtWidgets
import InterfazBuscarCliente
import InterfazDatosCliente
import InterfazDatosMascota
import InterfazElegirMascota
import main


class Detalle(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(991, 521)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BotonDatosCliente = QtWidgets.QPushButton(self.centralwidget)
        self.BotonDatosCliente.setGeometry(QtCore.QRect(260, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonDatosCliente.setFont(font)
        self.BotonDatosCliente.setTabletTracking(True)
        self.BotonDatosCliente.setAcceptDrops(True)
        self.BotonDatosCliente.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonDatosCliente.setAutoRepeatDelay(300)
        self.BotonDatosCliente.setObjectName("BotonDatosCliente")
        self.BotonDatosMascota = QtWidgets.QPushButton(self.centralwidget)
        self.BotonDatosMascota.setGeometry(QtCore.QRect(580, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonDatosMascota.setFont(font)
        self.BotonDatosMascota.setTabletTracking(True)
        self.BotonDatosMascota.setAcceptDrops(True)
        self.BotonDatosMascota.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonDatosMascota.setAutoRepeatDelay(300)
        self.BotonDatosMascota.setObjectName("BotonDatosMascota")
        self.ImgMascota = QtWidgets.QLabel(self.centralwidget)
        self.ImgMascota.setGeometry(QtCore.QRect(590, 230, 101, 101))
        self.ImgMascota.setStyleSheet("background-color: no color;")
        self.ImgMascota.setText("")
        self.ImgMascota.setPixmap(QtGui.QPixmap("alo/Mascota.png"))
        self.ImgMascota.setScaledContents(True)
        self.ImgMascota.setObjectName("ImgMascota")
        self.ImgCliente = QtWidgets.QLabel(self.centralwidget)
        self.ImgCliente.setGeometry(QtCore.QRect(270, 230, 91, 91))
        self.ImgCliente.setStyleSheet("background-color: no color;")
        self.ImgCliente.setText("")
        self.ImgCliente.setPixmap(QtGui.QPixmap("alo/Cliente.png"))
        self.ImgCliente.setScaledContents(True)
        self.ImgCliente.setObjectName("ImgCliente")
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
        self.Fondo.raise_()
        self.BotonDatosCliente.raise_()
        self.BotonDatosMascota.raise_()
        self.ImgMascota.raise_()
        self.ImgCliente.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.TxtNombre = QtWidgets.QLabel(self.centralwidget)
        self.TxtNombre.setGeometry(QtCore.QRect(300, 400, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.TxtNombre.setFont(font)
        self.TxtNombre.setStyleSheet("background-color: no color;\n"
        "color:black;")
        self.TxtNombre.setTextFormat(QtCore.Qt.AutoText)
        self.TxtNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.TxtNombre.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TxtNombre.setObjectName("TxtNombre")
        self.TxtRut = QtWidgets.QLabel(self.centralwidget)
        self.TxtRut.setGeometry(QtCore.QRect(300, 420, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.TxtRut.setFont(font)
        self.TxtRut.setStyleSheet("background-color: no color;\n"
        "color:black;")
        self.TxtRut.setTextFormat(QtCore.Qt.AutoText)
        self.TxtRut.setAlignment(QtCore.Qt.AlignCenter)
        self.TxtRut.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TxtRut.setObjectName("TxtRut")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BotonAtras.clicked.connect(lambda: self.cambio2(MainWindow, InterfazBuscarCliente.BuscarCliente,False))
        self.BotonDatosCliente.clicked.connect(lambda: self.cambio(MainWindow, InterfazDatosCliente.DatosCliente))
        self.BotonDatosMascota.clicked.connect(lambda: self.cambio2(MainWindow, InterfazElegirMascota.ElegirMascota,True))

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Detalle"))
        self.BotonDatosCliente.setText(_translate("MainWindow", "DATOS CLIENTE"))
        self.BotonDatosMascota.setText(_translate("MainWindow", "DATOS MASCOTA"))
        self.Titulo.setText(_translate("MainWindow", "DETALLE"))
        self.TxtNombre.setText(_translate("MainWindow", f"Cliente: {main.cliente.nombreCompleto}"))
        self.TxtRut.setText(_translate("MainWindow", f"Rut: {main.cliente.rut}"))
