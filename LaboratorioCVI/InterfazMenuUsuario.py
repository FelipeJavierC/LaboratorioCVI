import InterfazBorrarUsuario
import InterfazBuscarUsuario
import InterfazCrearUsuario
import InterfazEditarUsuario
import InterfazMenu
import res
from PyQt5 import QtCore, QtGui, QtWidgets


class MenuUsuario(object):
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
        self.fondo.setStyleSheet("border-image:url(:/images/IMAGE_INTER/Image(main).jpg);\n"
"border-radius: 20px;")
        self.fondo.setText("")
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
        self.examen = QtWidgets.QLabel(self.principal)
        self.examen.setGeometry(QtCore.QRect(180, 300, 111, 111))
        self.examen.setStyleSheet("border-image: url(:/images/IMAGE_INTER/CrearUsuario.png);")
        self.examen.setText("")
        self.examen.setObjectName("examen")
        self.examen_2 = QtWidgets.QLabel(self.principal)
        self.examen_2.setGeometry(QtCore.QRect(380, 310, 111, 111))
        self.examen_2.setStyleSheet("border-image: url(:/images/IMAGE_INTER/BuscarUsuario.png);")
        self.examen_2.setText("")
        self.examen_2.setObjectName("examen_2")
        self.examen_3 = QtWidgets.QLabel(self.principal)
        self.examen_3.setGeometry(QtCore.QRect(600, 310, 111, 111))
        self.examen_3.setStyleSheet("border-image: url(:/images/IMAGE_INTER/EditarUsuario.png);")
        self.examen_3.setText("")
        self.examen_3.setObjectName("examen_3")
        self.examen_4 = QtWidgets.QLabel(self.principal)
        self.examen_4.setGeometry(QtCore.QRect(800, 310, 111, 111))
        self.examen_4.setStyleSheet("border-image: url(:/images/IMAGE_INTER/Borrar.png)")
        self.examen_4.setText("")
        self.examen_4.setObjectName("examen_4")
        self.botonCrear = QtWidgets.QPushButton(self.principal)
        self.botonCrear.setGeometry(QtCore.QRect(160, 440, 141, 51))
        self.botonCrear.setStyleSheet("QPushButton {\n"
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
        self.botonCrear.setObjectName("botonCrear")
        self.botonBuscar = QtWidgets.QPushButton(self.principal)
        self.botonBuscar.setGeometry(QtCore.QRect(370, 440, 141, 51))
        self.botonBuscar.setStyleSheet("QPushButton {\n"
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
        self.botonBuscar.setObjectName("botonBuscar")
        self.botonBorrar = QtWidgets.QPushButton(self.principal)
        self.botonBorrar.setGeometry(QtCore.QRect(790, 440, 141, 51))
        self.botonBorrar.setStyleSheet("QPushButton {\n"
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
        self.botonBorrar.setObjectName("botonBorrar")
        self.botonEditar = QtWidgets.QPushButton(self.principal)
        self.botonEditar.setGeometry(QtCore.QRect(580, 440, 141, 51))
        self.botonEditar.setStyleSheet("QPushButton {\n"
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
        self.botonEditar.setObjectName("botonEditar")
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
        self.tit_labcvi.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.botonCrear.clicked.connect(lambda: self.cambio(MainWindow,InterfazCrearUsuario.CrearUsuario))
        self.botonBuscar.clicked.connect(lambda: self.cambio2(MainWindow,InterfazBuscarUsuario.BuscarUsuario,False))
        self.botonEditar.clicked.connect(lambda: self.cambio2(MainWindow,InterfazBuscarUsuario.BuscarUsuario,True))
        self.botonBorrar.clicked.connect(lambda: self.cambio(MainWindow, InterfazBorrarUsuario.BorrarUsuario))
        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazMenu.Menu))

          
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

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def cambio2(self, MainWindow,Interfaz,Bandera):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana,Bandera)
        self.ventana.show()
        MainWindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Menu Usuario"))
        self.botonCrear.setText(_translate("MainWindow", "Crear"))
        self.botonBuscar.setText(_translate("MainWindow", "Buscar"))
        self.botonBorrar.setText(_translate("MainWindow", "Borrar"))
        self.botonEditar.setText(_translate("MainWindow", "Editar"))