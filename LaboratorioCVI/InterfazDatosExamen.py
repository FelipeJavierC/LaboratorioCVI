import InterfazElegirExamen
import res
from PyQt5 import QtCore, QtGui, QtWidgets


class DatosExamen(object):
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
        self.tit_labcvi.setGeometry(QtCore.QRect(270, 131, 511, 71))
        self.tit_labcvi.setStyleSheet("font: 75 17pt \"MS Sans Serif\";\n"
"background: #FFFFFF;\n"
"border-radius:20px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.tit_labcvi.setObjectName("tit_labcvi")
        self.tit_labcvi_2 = QtWidgets.QLabel(self.principal)
        self.tit_labcvi_2.setGeometry(QtCore.QRect(80, 230, 911, 281))
        self.tit_labcvi_2.setStyleSheet("font: 75 17pt \"MS Sans Serif\";\n"
"background: #FFFFFF;\n"
"border-radius:20px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.tit_labcvi_2.setText("")
        self.tit_labcvi_2.setObjectName("tit_labcvi_2")
        self.nombrecl_edit = QtWidgets.QLineEdit(self.principal)
        self.nombrecl_edit.setGeometry(QtCore.QRect(240, 260, 261, 20))
        self.nombrecl_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.nombrecl_edit.setText("")
        self.nombrecl_edit.setObjectName("nombrecl_edit")
        self.lbl_namecl = QtWidgets.QLabel(self.principal)
        self.lbl_namecl.setGeometry(QtCore.QRect(122, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_namecl.setFont(font)
        self.lbl_namecl.setStyleSheet("")
        self.lbl_namecl.setObjectName("lbl_namecl")
        self.lbl_appa = QtWidgets.QLabel(self.principal)
        self.lbl_appa.setGeometry(QtCore.QRect(520, 260, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_appa.setFont(font)
        self.lbl_appa.setStyleSheet("")
        self.lbl_appa.setObjectName("lbl_appa")
        self.lbl_apm = QtWidgets.QLabel(self.principal)
        self.lbl_apm.setGeometry(QtCore.QRect(120, 300, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_apm.setFont(font)
        self.lbl_apm.setStyleSheet("")
        self.lbl_apm.setObjectName("lbl_apm")
        self.ApellidoM_edit = QtWidgets.QLineEdit(self.principal)
        self.ApellidoM_edit.setGeometry(QtCore.QRect(240, 300, 261, 20))
        self.ApellidoM_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.ApellidoM_edit.setObjectName("ApellidoM_edit")
        self.ApellidoP_edit = QtWidgets.QLineEdit(self.principal)
        self.ApellidoP_edit.setGeometry(QtCore.QRect(640, 260, 281, 20))
        self.ApellidoP_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.ApellidoP_edit.setObjectName("ApellidoP_edit")
        self.lbl_mascota = QtWidgets.QLabel(self.principal)
        self.lbl_mascota.setGeometry(QtCore.QRect(575, 300, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mascota.setFont(font)
        self.lbl_mascota.setStyleSheet("")
        self.lbl_mascota.setObjectName("lbl_mascota")
        self.lb_tipo = QtWidgets.QLabel(self.principal)
        self.lb_tipo.setGeometry(QtCore.QRect(200, 350, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tipo.setFont(font)
        self.lb_tipo.setStyleSheet("")
        self.lb_tipo.setObjectName("lb_tipo")
        self.lbl_fecha = QtWidgets.QLabel(self.principal)
        self.lbl_fecha.setGeometry(QtCore.QRect(588, 350, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fecha.setFont(font)
        self.lbl_fecha.setStyleSheet("")
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.lbl_hora = QtWidgets.QLabel(self.principal)
        self.lbl_hora.setGeometry(QtCore.QRect(200, 400, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hora.setFont(font)
        self.lbl_hora.setStyleSheet("")
        self.lbl_hora.setObjectName("lbl_hora")
        self.lbl_precio = QtWidgets.QLabel(self.principal)
        self.lbl_precio.setGeometry(QtCore.QRect(588, 400, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setStyleSheet("")
        self.lbl_precio.setObjectName("lbl_precio")
        self.precio_edit = QtWidgets.QLineEdit(self.principal)
        self.precio_edit.setGeometry(QtCore.QRect(640, 400, 281, 20))
        self.precio_edit.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.precio_edit.setObjectName("precio_edit")
        self.botonAtras = QtWidgets.QPushButton(self.principal)
        self.botonAtras.setGeometry(QtCore.QRect(960, 520, 41, 41))
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
        self.fecha_edit_2 = QtWidgets.QLineEdit(self.principal)
        self.fecha_edit_2.setGeometry(QtCore.QRect(640, 350, 281, 20))
        self.fecha_edit_2.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.fecha_edit_2.setObjectName("fecha_edit_2")
        self.mascota_edit_3 = QtWidgets.QLineEdit(self.principal)
        self.mascota_edit_3.setGeometry(QtCore.QRect(640, 300, 281, 20))
        self.mascota_edit_3.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.mascota_edit_3.setObjectName("mascota_edit_3")
        self.tipo_edit_4 = QtWidgets.QLineEdit(self.principal)
        self.tipo_edit_4.setGeometry(QtCore.QRect(240, 350, 261, 20))
        self.tipo_edit_4.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.tipo_edit_4.setObjectName("tipo_edit_4")
        self.hora_edit_5 = QtWidgets.QLineEdit(self.principal)
        self.hora_edit_5.setGeometry(QtCore.QRect(240, 400, 261, 20))
        self.hora_edit_5.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.hora_edit_5.setObjectName("hora_edit_5")
        self.lbl_estado = QtWidgets.QLabel(self.principal)
        self.lbl_estado.setGeometry(QtCore.QRect(190, 450, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_estado.setFont(font)
        self.lbl_estado.setStyleSheet("")
        self.lbl_estado.setObjectName("lbl_estado")
        self.estado = QtWidgets.QProgressBar(self.principal)
        self.estado.setGeometry(QtCore.QRect(240, 450, 118, 20))
        self.estado.setProperty("value", 0)
        self.estado.setObjectName("estado")
        self.lbl_resultado = QtWidgets.QLabel(self.principal)
        self.lbl_resultado.setGeometry(QtCore.QRect(460, 450, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_resultado.setFont(font)
        self.lbl_resultado.setStyleSheet("")
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.resultado_edit = QtWidgets.QTextEdit(self.principal)
        self.resultado_edit.setGeometry(QtCore.QRect(530, 440, 391, 51))
        self.resultado_edit.setStyleSheet("background: #FFFFFF;\n"
                                          "border-radius:5px;\n"
                                          "\n"
                                          "border: 1px solid #222d5b ;")
        self.resultado_edit.setObjectName("resultado_edit")
        self.tit_labcvi.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.nombrecl_edit.setText(f"{InterfazElegirExamen.examen.nombreCliente}")
        self.ApellidoP_edit.setText(f"{InterfazElegirExamen.examen.apellidoP}")
        self.ApellidoM_edit.setText(f"{InterfazElegirExamen.examen.apellidoM}")
        self.mascota_edit_3.setText(f"{InterfazElegirExamen.examen.mascota}")
        self.tipo_edit_4.setText(f"{InterfazElegirExamen.examen.tipo}")
        self.fecha_edit_2.setText(f"{InterfazElegirExamen.examen.fecha}")
        self.hora_edit_5.setText(f"{InterfazElegirExamen.examen.hora}")
        self.precio_edit.setText(f"{InterfazElegirExamen.examen.precio}")
        if InterfazElegirExamen.examen.estado == "True":
                self.estado.setProperty("value", 100)
        self.resultado_edit.setText(f"{InterfazElegirExamen.examen.resultado}")
        self.nombrecl_edit.setReadOnly(True)
        self.ApellidoP_edit.setReadOnly(True)
        self.ApellidoM_edit.setReadOnly(True)
        self.mascota_edit_3.setReadOnly(True)
        self.tipo_edit_4.setReadOnly(True)
        self.fecha_edit_2.setReadOnly(True)
        self.hora_edit_5.setReadOnly(True)
        self.precio_edit.setReadOnly(True)
        self.resultado_edit.setReadOnly(True)

        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow,InterfazElegirExamen.ElegirExamen,False))

          
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

    def cambio(self, MainWindow,Interfaz,Bandera):
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
        self.tit_labcvi.setText(_translate("MainWindow", "Datos Examen"))
        self.lbl_namecl.setText(_translate("MainWindow", "Nombres Cliente:"))
        self.lbl_appa.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.lbl_apm.setText(_translate("MainWindow", "Apellido Materno:"))
        self.lbl_mascota.setText(_translate("MainWindow", "Mascota:"))
        self.lb_tipo.setText(_translate("MainWindow", "Tipo:"))
        self.lbl_fecha.setText(_translate("MainWindow", "Fecha:"))
        self.lbl_hora.setText(_translate("MainWindow", "Hora:"))
        self.lbl_precio.setText(_translate("MainWindow", "Precio:"))
        self.lbl_estado.setText(_translate("MainWindow", "Estado:"))
        self.lbl_resultado.setText(_translate("MainWindow", "Resultado:"))