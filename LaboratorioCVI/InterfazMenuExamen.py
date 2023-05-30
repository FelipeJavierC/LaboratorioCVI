import InterfazBorrarExamen
import InterfazBuscarCliente
import InterfazBuscarUsuario
import InterfazCrearExamen
import InterfazElegirExamen
import InterfazMenu
import InterfazNumeroDeExamenes
import main
import res
from PyQt5 import QtCore, QtGui, QtWidgets


class MenuExamen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 860)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.principal = QtWidgets.QWidget(self.centralwidget)
        self.principal.setGeometry(QtCore.QRect(90, 60, 1081, 701))
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
        self.examen.setGeometry(QtCore.QRect(190, 290, 111, 111))
        self.examen.setStyleSheet("border-image: url(:/images/IMAGE_INTER/Examen.png);")
        self.examen.setText("")
        self.examen.setObjectName("examen")
        self.botonAgendar = QtWidgets.QPushButton(self.principal)
        self.botonAgendar.setGeometry(QtCore.QRect(170, 440, 141, 51))
        self.botonAgendar.setStyleSheet("QPushButton {\n"
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
        self.botonAgendar.setObjectName("botonAgendar")
        self.examen_2 = QtWidgets.QLabel(self.principal)
        self.examen_2.setGeometry(QtCore.QRect(370, 300, 111, 111))
        self.examen_2.setStyleSheet("border-image:url(:/images/IMAGE_INTER/BuscarExamen.png)")
        self.examen_2.setText("")
        self.examen_2.setObjectName("examen_2")
        self.botonBuscar = QtWidgets.QPushButton(self.principal)
        self.botonBuscar.setGeometry(QtCore.QRect(360, 440, 141, 51))
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
        self.examen_3 = QtWidgets.QLabel(self.principal)
        self.examen_3.setGeometry(QtCore.QRect(580, 310, 111, 111))
        self.examen_3.setStyleSheet("border-image: url(:/images/IMAGE_INTER/EditarExamen.png)")
        self.examen_3.setText("")
        self.examen_3.setObjectName("examen_3")
        self.botonEditar = QtWidgets.QPushButton(self.principal)
        self.botonEditar.setGeometry(QtCore.QRect(560, 440, 141, 51))
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
        self.examen_4 = QtWidgets.QLabel(self.principal)
        self.examen_4.setGeometry(QtCore.QRect(790, 310, 111, 111))
        self.examen_4.setStyleSheet("border-image: url(:/images/IMAGE_INTER/Borrar.png)")
        self.examen_4.setText("")
        self.examen_4.setObjectName("examen_4")
        self.botonBorrar = QtWidgets.QPushButton(self.principal)
        self.botonBorrar.setGeometry(QtCore.QRect(770, 440, 141, 51))
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
        self.botonAtras = QtWidgets.QPushButton(self.principal)
        self.botonAtras.setGeometry(QtCore.QRect(960, 515, 41, 41))
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
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(430, 560, 371, 21))
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
        self.TxtNoEncontrado2 = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado2.setGeometry(QtCore.QRect(430, 560, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.TxtNoEncontrado2.setFont(font)
        self.TxtNoEncontrado2.setStyleSheet("background-color: no color;\n"
                                           "color:red;")
        self.TxtNoEncontrado2.setTextFormat(QtCore.Qt.AutoText)
        self.TxtNoEncontrado2.setAlignment(QtCore.Qt.AlignCenter)
        self.TxtNoEncontrado2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TxtNoEncontrado2.setObjectName("TxtNoEncontrado")
        self.TxtNoEncontrado2.hide()
        self.tit_labcvi.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow,InterfazMenu.Menu))
        self.botonAgendar.clicked.connect(lambda: self.cambio(MainWindow,InterfazNumeroDeExamenes.NumeroExamenes))

        main.examenes.clear()
        main.horarios.clear()

        self.botonBuscar.clicked.connect(lambda: self.cambio2(MainWindow,InterfazElegirExamen.ElegirExamen,False))
        self.botonEditar.clicked.connect(lambda: self.verificar(MainWindow,InterfazElegirExamen.ElegirExamen,False))
        self.botonBorrar.clicked.connect(lambda: self.verificar(MainWindow,InterfazBorrarExamen.BorrarExamen,True))

          
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

    def verificar(self,MainWindow,Interfaz,x):
        if (main.usuario.cargo == "Programador" or main.usuario.cargo == "Veterinario") and x == True:
            self.cambio3(MainWindow, InterfazBorrarExamen.BorrarExamen)
        elif (main.usuario.cargo == "Programador" or main.usuario.cargo == "Veterinario") and x == False:
            self.cambio2(MainWindow,InterfazElegirExamen.ElegirExamen,True)
        else:
            self.TxtNoEncontrado.show()

    def cambio3(self, MainWindow,Interfaz):
        main.cargarDatosExamen()
        if len(main.examenes) > 0:
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Interfaz()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
            MainWindow.close()
        else:
            self.TxtNoEncontrado2.show()

    def cambio2(self, MainWindow,Interfaz,bandera):
        main.cargarDatosExamen()
        if len(main.examenes) > 0:
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Interfaz()
            self.ui.setupUi(self.ventana,bandera)
            self.ventana.show()
            MainWindow.close()
        else:
            self.TxtNoEncontrado2.show()

 # No tocar

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Menu Examen"))
        self.botonAgendar.setText(_translate("MainWindow", "Agendar"))
        self.botonBuscar.setText(_translate("MainWindow", "Buscar"))
        self.botonEditar.setText(_translate("MainWindow", "Editar"))
        self.botonBorrar.setText(_translate("MainWindow", "Borrar"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Este Usuario No Tiene Los Permisos Requeridos."))
        self.TxtNoEncontrado2.setText(_translate("MainWindow", "Este Cliente No Tiene Examenes Agendados."))