from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazCrearExamen
import InterfazEditar
import InterfazMenu
import InterfazMenuCliente
import InterfazDetalle
import InterfazMenuExamen
import main


class BuscarCliente(object):
    def setupUi(self, MainWindow,Bandera):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(991, 521)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImgClienteBuscar = QtWidgets.QLabel(self.centralwidget)
        self.ImgClienteBuscar.setGeometry(QtCore.QRect(440, 160, 101, 101))
        self.ImgClienteBuscar.setStyleSheet("background-color: no color;")
        self.ImgClienteBuscar.setText("")
        self.ImgClienteBuscar.setPixmap(QtGui.QPixmap("alo/Buscar.png"))
        self.ImgClienteBuscar.setScaledContents(True)
        self.ImgClienteBuscar.setObjectName("ImgClienteBuscar")
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
        self.BuscarRut = QtWidgets.QLineEdit(self.centralwidget)
        self.BuscarRut.setGeometry(QtCore.QRect(90, 300, 781, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.BuscarRut.setFont(font)
        self.BuscarRut.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRut.setAccessibleDescription("")
        self.BuscarRut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BuscarRut.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BuscarRut.setText("")
        self.BuscarRut.setAlignment(QtCore.Qt.AlignCenter)
        self.BuscarRut.setObjectName("BuscarRut")
        self.ImgLupa = QtWidgets.QLabel(self.centralwidget)
        self.ImgLupa.setGeometry(QtCore.QRect(97, 304, 51, 51))
        self.ImgLupa.setStyleSheet("background-color: no color;")
        self.ImgLupa.setText("")
        self.ImgLupa.setPixmap(QtGui.QPixmap("alo/Lupa.png"))
        self.ImgLupa.setScaledContents(True)
        self.ImgLupa.setObjectName("ImgLupa")
        self.Fondo.raise_()
        self.ImgClienteBuscar.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.BuscarRut.raise_()
        self.ImgLupa.raise_()
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
        self.TxtNoEncontrado.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if Bandera == None:
            self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazMenu.Menu))
        else:
            self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazMenuCliente.MenuCliente))
        self.BuscarRut.returnPressed.connect(lambda: self.guardar(MainWindow,Bandera))

    def guardar(self,MainWindow,Bandera):
        rut = self.BuscarRut.text()
        mascotas = main.cargarDatosMascota(rut)
        cliente = main.cargarDatosCliente(rut, mascotas)
        if cliente != False:
            if Bandera == True:
                self.cambio(MainWindow, InterfazEditar.Editar)
            elif Bandera == False:
                self.cambio(MainWindow, InterfazDetalle.Detalle)
            else:
                self.cambio(MainWindow, InterfazMenuExamen.MenuExamen)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Buscar Cliente"))
        self.Titulo.setText(_translate("MainWindow", "BUSCAR CLIENTE"))
        self.BuscarRut.setPlaceholderText(_translate("MainWindow", "INGRESE RUT DEL CLIENTE"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "No se pudo encontrar el cliente. Vuelva a intentar."))
