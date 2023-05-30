import InterfazCrearExamen
import InterfazMenuExamen
import res
from PyQt5 import QtCore, QtGui, QtWidgets

numeroExamenes = 0

class NumeroExamenes(object):
    def setupUi(self, MainWindow):
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
        self.lineEdit_ingrsNEX = QtWidgets.QLineEdit(self.principal)
        self.lineEdit_ingrsNEX.setGeometry(QtCore.QRect(190, 426, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ingrsNEX.setFont(font)
        self.lineEdit_ingrsNEX.setStyleSheet("background-color: transparent;\n"
"border: 0px;")
        self.lineEdit_ingrsNEX.setObjectName("lineEdit_ingrsNEX")
        self.cliente = QtWidgets.QLabel(self.principal)
        self.cliente.setGeometry(QtCore.QRect(480, 260, 121, 111))
        self.cliente.setStyleSheet("border-image:url(:/images/IMAGE_INTER/Examen.png)")
        self.cliente.setText("")
        self.cliente.setObjectName("cliente")
        self.botonContinuar = QtWidgets.QPushButton(self.principal)
        self.botonContinuar.setGeometry(QtCore.QRect(470, 510, 141, 41))
        self.botonContinuar.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: #7EC6FF;\n"
"    border-radius: 10px;\n"
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
        self.botonContinuar.setObjectName("botonContinuar")
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

        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazMenuExamen.MenuExamen))
        self.botonContinuar.clicked.connect(lambda: self.guardar(MainWindow))

          
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

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def guardar(self, MainWindow):
        global numeroExamenes
        try:
            numeroExamenes = int(self.lineEdit_ingrsNEX.text())
        except:
            numeroExamenes = 0
        print(numeroExamenes)
        if numeroExamenes != 0:
            self.cambio(MainWindow,InterfazCrearExamen.CrearExamen)
        else:
            self.TxtNoEncontrado.show()

 # No tocar

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Numero de Examenes"))
        self.lineEdit_ingrsNEX.setPlaceholderText(_translate("MainWindow", "                     Ingrese numero de examenes a agendar"))
        self.botonContinuar.setText(_translate("MainWindow", "Continuar"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Ingrese Un Numero Valido."))