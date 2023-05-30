import InterfazMenuUsuario
import main
import res

from PyQt5 import QtCore, QtGui, QtWidgets


class DatosUsuario(object):
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
        self.nombrecl_edit.setGeometry(QtCore.QRect(190, 270, 311, 20))
        self.nombrecl_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.nombrecl_edit.setText("")
        self.nombrecl_edit.setObjectName("nombrecl_edit")
        self.lbl_namecl = QtWidgets.QLabel(self.principal)
        self.lbl_namecl.setGeometry(QtCore.QRect(122, 270, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_namecl.setFont(font)
        self.lbl_namecl.setStyleSheet("")
        self.lbl_namecl.setObjectName("lbl_namecl")
        self.lbl_appa = QtWidgets.QLabel(self.principal)
        self.lbl_appa.setGeometry(QtCore.QRect(520, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_appa.setFont(font)
        self.lbl_appa.setStyleSheet("")
        self.lbl_appa.setObjectName("lbl_appa")
        self.lbl_apm = QtWidgets.QLabel(self.principal)
        self.lbl_apm.setGeometry(QtCore.QRect(120, 330, 121, 21))
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
        self.ApellidoM_edit.setGeometry(QtCore.QRect(240, 330, 261, 20))
        self.ApellidoM_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.ApellidoM_edit.setObjectName("ApellidoM_edit")
        self.ApellidoP_edit = QtWidgets.QLineEdit(self.principal)
        self.ApellidoP_edit.setGeometry(QtCore.QRect(640, 270, 281, 20))
        self.ApellidoP_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.ApellidoP_edit.setObjectName("ApellidoP_edit")
        self.lbl_mascota = QtWidgets.QLabel(self.principal)
        self.lbl_mascota.setGeometry(QtCore.QRect(525, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mascota.setFont(font)
        self.lbl_mascota.setStyleSheet("")
        self.lbl_mascota.setObjectName("lbl_mascota")
        self.lbl_fecha = QtWidgets.QLabel(self.principal)
        self.lbl_fecha.setGeometry(QtCore.QRect(684, 330, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fecha.setFont(font)
        self.lbl_fecha.setStyleSheet("")
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.lbl_precio = QtWidgets.QLabel(self.principal)
        self.lbl_precio.setGeometry(QtCore.QRect(122, 380, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setStyleSheet("")
        self.lbl_precio.setObjectName("lbl_precio")
        self.rut_edit = QtWidgets.QLineEdit(self.principal)
        self.rut_edit.setGeometry(QtCore.QRect(150, 380, 201, 20))
        self.rut_edit.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.rut_edit.setObjectName("rut_edit")
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
        self.email_edit_2 = QtWidgets.QLineEdit(self.principal)
        self.email_edit_2.setGeometry(QtCore.QRect(426, 380, 201, 20))
        self.email_edit_2.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.email_edit_2.setText("")
        self.email_edit_2.setObjectName("email_edit_2")
        self.lbl_precio_2 = QtWidgets.QLabel(self.principal)
        self.lbl_precio_2.setGeometry(QtCore.QRect(380, 380, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_2.setFont(font)
        self.lbl_precio_2.setStyleSheet("")
        self.lbl_precio_2.setObjectName("lbl_precio_2")
        self.lbl_precio_3 = QtWidgets.QLabel(self.principal)
        self.lbl_precio_3.setGeometry(QtCore.QRect(670, 380, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_3.setFont(font)
        self.lbl_precio_3.setStyleSheet("")
        self.lbl_precio_3.setObjectName("lbl_precio_3")
        self.cargo_edit_3 = QtWidgets.QLineEdit(self.principal)
        self.cargo_edit_3.setGeometry(QtCore.QRect(720, 380, 201, 20))
        self.cargo_edit_3.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.cargo_edit_3.setText("")
        self.cargo_edit_3.setObjectName("cargo_edit_3")
        self.lbl_precio_4 = QtWidgets.QLabel(self.principal)
        self.lbl_precio_4.setGeometry(QtCore.QRect(120, 430, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_4.setFont(font)
        self.lbl_precio_4.setStyleSheet("")
        self.lbl_precio_4.setObjectName("lbl_precio_4")
        self.label = QtWidgets.QLabel(self.principal)
        self.label.setGeometry(QtCore.QRect(200, 430, 201, 20))
        self.label.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.principal)
        self.widget.setGeometry(QtCore.QRect(370, 421, 31, 41))
        self.widget.setObjectName("widget")
        self.boton_verpass = QtWidgets.QPushButton(self.widget)
        self.boton_verpass.setGeometry(QtCore.QRect(0, 10, 30, 18))
        self.boton_verpass.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"    border: 0;\n"
"    background: #7EC6FF;\n"
"    border-radius: 5px;\n"
"    border-top-left-radius: 0px;\n"
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
        self.boton_verpass.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/IMAGE_INTER/ver1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_verpass.setIcon(icon1)
        self.boton_verpass.setIconSize(QtCore.QSize(20, 20))
        self.boton_verpass.setObjectName("boton_verpass")
        self.contrasenaEdit = QtWidgets.QLineEdit(self.principal)
        self.contrasenaEdit.setGeometry(QtCore.QRect(210, 430, 161, 21))
        self.contrasenaEdit.setStyleSheet("background: transparent;\n"
"border-radius:0px;\n"
"\n"
"")
        self.contrasenaEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenaEdit.setObjectName("contrasenaEdit")
        self.genero_edit = QtWidgets.QLineEdit(self.principal)
        self.genero_edit.setGeometry(QtCore.QRect(580, 330, 91, 20))
        self.genero_edit.setStyleSheet("background: #FFFFFF;\n"
                                       "border-radius:5px;\n"
                                       "\n"
                                       "border: 1px solid #222d5b ;")
        self.genero_edit.setText("")
        self.genero_edit.setObjectName("genero_edit")
        self.fecha_edit = QtWidgets.QLineEdit(self.principal)
        self.fecha_edit.setGeometry(QtCore.QRect(810, 330, 111, 20))
        self.fecha_edit.setStyleSheet("background: #FFFFFF;\n"
                                      "border-radius:5px;\n"
                                      "\n"
                                      "border: 1px solid #222d5b ;")
        self.fecha_edit.setText("")
        self.fecha_edit.setObjectName("fecha_edit")
        self.nombrecl_edit.setReadOnly(True)
        self.ApellidoP_edit.setReadOnly(True)
        self.ApellidoM_edit.setReadOnly(True)
        self.genero_edit.setReadOnly(True)
        self.fecha_edit.setReadOnly(True)
        self.rut_edit.setReadOnly(True)
        self.email_edit_2.setReadOnly(True)
        self.cargo_edit_3.setReadOnly(True)
        self.contrasenaEdit.setReadOnly(True)

        self.nombrecl_edit.setText(f"{main.usuarioedit.nombres}")
        self.ApellidoP_edit.setText(f"{main.usuarioedit.apellidoP}")
        self.ApellidoM_edit.setText(f"{main.usuarioedit.apellidoM}")
        self.genero_edit.setText(f"{main.usuarioedit.genero}")
        self.fecha_edit.setText(f"{main.usuarioedit.fecha}")
        self.rut_edit.setText(f"{main.usuarioedit.rut}")
        self.email_edit_2.setText(f"{main.usuarioedit.email}")
        self.cargo_edit_3.setText(f"{main.usuarioedit.cargo}")
        self.contrasenaEdit.setText(f"{main.usuarioedit.clave}")

        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow,InterfazMenuUsuario.MenuUsuario))
        self.tit_labcvi.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.boton_verpass.clicked.connect(self.cambiar_mod_pass)

 

    def cerrar_ventana(self):
        QtCore.QCoreApplication.quit()
 

         
    def cambiar_icono_pass(self):
        size_pass_visible = QtCore.QSize(43, 43)  
        size_pass_hidden = QtCore.QSize(20, 20)      

        if self.is_pass_visible:
                icon = QtGui.QIcon(":/images/IMAGE_INTER/OculatarContraseñaBlanco.png")
                icon_actual = icon.pixmap(size_pass_visible)
        else:
                icon = QtGui.QIcon(":/images/IMAGE_INTER/ver1.png")
                icon_actual = icon.pixmap(size_pass_hidden)

        self.boton_verpass.setIcon(QtGui.QIcon(icon_actual))
        self.boton_verpass.setIconSize(icon_actual.size())

    def cambiar_mod_pass(self):

        if self.contrasenaEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.contrasenaEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.is_pass_visible = True


        else:
            self.contrasenaEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.is_pass_visible = False
        
        self.cambiar_icono_pass()
#no tocar

    def cambio(self, MainWindow,Interfaz):
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
        self.tit_labcvi.setText(_translate("MainWindow", "Datos Usuario"))
        self.lbl_namecl.setText(_translate("MainWindow", "Nombres:"))
        self.lbl_appa.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.lbl_apm.setText(_translate("MainWindow", "Apellido Materno:"))
        self.lbl_mascota.setText(_translate("MainWindow", "Genero:"))
        self.lbl_fecha.setText(_translate("MainWindow", "Fecha de Nacimiento:"))
        self.lbl_precio.setText(_translate("MainWindow", "Rut:"))
        self.lbl_precio_2.setText(_translate("MainWindow", "Email:"))
        self.lbl_precio_3.setText(_translate("MainWindow", "Cargo:"))
        self.lbl_precio_4.setText(_translate("MainWindow", "Contraseña:"))