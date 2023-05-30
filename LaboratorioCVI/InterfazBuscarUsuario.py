import InterfazDatosUsuario
import InterfazEditarUsuario
import InterfazMenuUsuario
import main
import res
from PyQt5 import QtCore, QtGui, QtWidgets


class BuscarUsuario(object):
    def setupUi(self, MainWindow,Bandera):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 860)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.principal = QtWidgets.QWidget(self.centralwidget)
        self.principal.setGeometry(QtCore.QRect(90, 60, 1081, 651))
        self.principal.setObjectName("principal")
        self.fondo = QtWidgets.QLabel(self.principal)
        self.fondo.setGeometry(QtCore.QRect(40, 60, 991, 521))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fondo.setFont(font)
        self.fondo.setStyleSheet("border-image:url(:/images/IMAGE_INTER/Image(main).jpg);\n"
"border-radius: 20px;")
        self.fondo.setText("")
        self.fondo.setTextFormat(QtCore.Qt.MarkdownText)
        self.fondo.setObjectName("fondo")
        self.frame_superior = QtWidgets.QFrame(self.principal)
        self.frame_superior.setGeometry(QtCore.QRect(40, 60, 991, 46))
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.boton_minimize = QtWidgets.QPushButton(self.frame_superior)
        self.boton_minimize.setGeometry(QtCore.QRect(890, 0, 51, 43))
        self.boton_minimize.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: #00a2ff;\n"
"    \n"
"    color: white;\n"
"    font-family: Helvetica Neue;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #0e74ae;\n"
"}\n"
"")
        self.boton_minimize.setObjectName("boton_minimize")
        self.botonExit = QtWidgets.QPushButton(self.frame_superior)
        self.botonExit.setGeometry(QtCore.QRect(940, 0, 51, 43))
        self.botonExit.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: #00a2ff;\n"
"    border-right: none;\n"
"    border-top-right-radius: 20px;   /* Ajusta el radio de la esquina superior derecha según tus preferencias */\n"
"    color: white;\n"
"    font-family: Helvetica Neue;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #DE0F34;\n"
"}\n"
"")
        self.botonExit.setObjectName("botonExit")
        self.tit_labcvi = QtWidgets.QLabel(self.principal)
        self.tit_labcvi.setGeometry(QtCore.QRect(270, 140, 511, 71))
        self.tit_labcvi.setStyleSheet("font: 75 17pt \"MS Sans Serif\";\n"
"background: #FFFFFF;\n"
"border-radius:20px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.tit_labcvi.setObjectName("tit_labcvi")
        self.botonAtras = QtWidgets.QPushButton(self.principal)
        self.botonAtras.setGeometry(QtCore.QRect(960, 510, 41, 41))
        self.botonAtras.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"    border: 0;\n"
"    background: #7EC6FF;\n"
"    border-radius: 10px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    color: white;\n"
"    font-family: Helvetica Neue;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #9500ff, stop:1 #00DDFF);\n"
"}\n"
"")
        self.botonAtras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/IMAGE_INTER/FlechABLANCA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonAtras.setIcon(icon)
        self.botonAtras.setObjectName("botonAtras")
        self.label = QtWidgets.QLabel(self.principal)
        self.label.setGeometry(QtCore.QRect(160, 426, 771, 51))
        self.label.setStyleSheet("font: 75 17pt \"MS Sans Serif\";\n"
"background: #FFFFFF;\n"
"border-radius:20px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.principal)
        self.widget.setGeometry(QtCore.QRect(160, 430, 61, 51))
        self.widget.setObjectName("widget")
        self.botonBuscar = QtWidgets.QPushButton(self.widget)
        self.botonBuscar.setGeometry(QtCore.QRect(3, 0, 59, 43))
        self.botonBuscar.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"    border: 0;\n"
"    background: #7EC6FF;\n"
"    border-radius: 18px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    color: white;\n"
"    font-family: Helvetica Neue;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #9500ff, stop:1 #00DDFF);\n"
"}\n"
"")
        self.botonBuscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/IMAGE_INTER/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonBuscar.setIcon(icon1)
        self.botonBuscar.setIconSize(QtCore.QSize(30, 30))
        self.botonBuscar.setObjectName("botonBuscar")
        self.lineEdit_ingrsRut = QtWidgets.QLineEdit(self.principal)
        self.lineEdit_ingrsRut.setGeometry(QtCore.QRect(230, 426, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ingrsRut.setFont(font)
        self.lineEdit_ingrsRut.setStyleSheet("background-color: transparent;\n"
"border: 0px;")
        self.lineEdit_ingrsRut.setObjectName("lineEdit_ingrsRut")
        self.cliente = QtWidgets.QLabel(self.principal)
        self.cliente.setGeometry(QtCore.QRect(480, 260, 121, 111))
        self.cliente.setStyleSheet("border-image: url(:/images/IMAGE_INTER/Usuario.png)")
        self.cliente.setText("")
        self.cliente.setObjectName("cliente")
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(440, 540, 371, 21))
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
        self.tit_labcvi.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.botonBuscar.clicked.connect(lambda: self.guardar(MainWindow,Bandera))
        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow,InterfazMenuUsuario.MenuUsuario))

          
 # No tocar

        self.draggable = False
        self.offset = None

        def mousePressEvent(event):
            if event.button() == QtCore.Qt.LeftButton:
                self.draggable = True
                self.offset = event.pos()

        def mouseMoveEvent(event):
            if self.draggable and self.offset is not None:
                diff = event.pos() - self.offset
                MainWindow.move(MainWindow.pos() + diff)

        def mouseReleaseEvent(event):
            if event.button() == QtCore.Qt.LeftButton:
                self.draggable = False
                self.offset = None

        self.frame_superior.mousePressEvent = mousePressEvent
        self.frame_superior.mouseMoveEvent = mouseMoveEvent
        self.frame_superior.mouseReleaseEvent = mouseReleaseEvent
    


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   
        self.boton_minimize.clicked.connect(MainWindow.showMinimized)
        self.botonExit.clicked.connect(self.cerrar_ventana)

   

    def cerrar_ventana(self):
        QtCore.QCoreApplication.quit()

 # No tocar

    def guardar(self,MainWindow,Bandera):
        usuario = main.buscarUsuario(self.lineEdit_ingrsRut.text())
        if usuario != False:
            if Bandera == True:
                self.cambio(MainWindow, InterfazEditarUsuario.EditarUsuario)
            else:
                self.cambio(MainWindow, InterfazDatosUsuario.DatosUsuario)
        else:
            self.TxtNoEncontrado.show()

    def cambio(self, MainWindow, Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Buscar Usuario"))
        self.lineEdit_ingrsRut.setPlaceholderText(_translate("MainWindow", "                              Ingrese Rut del Cliente"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "No se pudo encontrar el Usuario. Vuelva a intentar."))