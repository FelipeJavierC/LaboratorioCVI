import datetime

import InterfazExamenes
import InterfazMenuExamen
import InterfazNumeroDeExamenes
import main
import res

from PyQt5 import QtCore, QtGui, QtWidgets


class CrearExamen(object):
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
        self.nombrecl_edit.setGeometry(QtCore.QRect(240, 270, 261, 20))
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
        self.lbl_mascota.setGeometry(QtCore.QRect(575, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mascota.setFont(font)
        self.lbl_mascota.setStyleSheet("")
        self.lbl_mascota.setObjectName("lbl_mascota")
        self.mascota_edit = QtWidgets.QComboBox(self.principal)
        self.mascota_edit.setGeometry(QtCore.QRect(640, 330, 281, 22))
        self.mascota_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.mascota_edit.setObjectName("mascota_edit")
        self.mascota_edit.addItem("")
        self.mascota_edit.setItemText(0, "")
        self.lb_tipo = QtWidgets.QLabel(self.principal)
        self.lb_tipo.setGeometry(QtCore.QRect(200, 390, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tipo.setFont(font)
        self.lb_tipo.setStyleSheet("")
        self.lb_tipo.setObjectName("lb_tipo")
        self.Tipo_edit = QtWidgets.QComboBox(self.principal)
        self.Tipo_edit.setGeometry(QtCore.QRect(240, 390, 261, 22))
        self.Tipo_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.Tipo_edit.setObjectName("Tipo_edit")
        self.Tipo_edit.addItem("")
        self.Tipo_edit.setItemText(0, "")
        self.Tipo_edit.addItem("Examen De Sangre")
        self.Tipo_edit.addItem("Secuenciamiento De Muestras Biologicas")
        self.Tipo_edit.addItem("Radiografia")
        self.Tipo_edit.addItem("Scanner Y Ecografia")

        self.fecha_edit = QtWidgets.QDateEdit(self.principal)
        self.fecha_edit.setMinimumDate(datetime.datetime.now())
        self.fecha_edit.setGeometry(QtCore.QRect(640, 390, 91, 22))
        self.fecha_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.fecha_edit.setObjectName("fecha_edit")
        self.lbl_fecha = QtWidgets.QLabel(self.principal)
        self.lbl_fecha.setGeometry(QtCore.QRect(588, 390, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fecha.setFont(font)
        self.lbl_fecha.setStyleSheet("")
        self.lbl_fecha.setObjectName("lbl_fecha")

        self.hora_edit = QtWidgets.QComboBox(self.principal)
        self.hora_edit.setGeometry(QtCore.QRect(240, 450, 261, 22))
        self.hora_edit.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.hora_edit.setObjectName("hora_edit")
        self.hora_edit.addItem("")
        self.hora_edit.setItemText(0, "")
        self.lbl_hora = QtWidgets.QLabel(self.principal)
        self.lbl_hora.setGeometry(QtCore.QRect(200, 450, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hora.setFont(font)
        self.lbl_hora.setStyleSheet("")
        self.lbl_hora.setObjectName("lbl_hora")
        self.lbl_precio = QtWidgets.QLabel(self.principal)
        self.lbl_precio.setGeometry(QtCore.QRect(588, 450, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setStyleSheet("")
        self.lbl_precio.setObjectName("lbl_precio")
        self.precio_edit = QtWidgets.QLineEdit(self.principal)
        self.precio_edit.setGeometry(QtCore.QRect(640, 450, 281, 20))
        self.precio_edit.setStyleSheet("background: #FFFFFF;\n"
"border-radius:5px;\n"
"\n"
"border: 1px solid #222d5b ;")
        self.precio_edit.setObjectName("precio_edit")
        self.botonGuardar = QtWidgets.QPushButton(self.principal)
        self.botonGuardar.setGeometry(QtCore.QRect(480, 530, 141, 41))
        self.botonGuardar.setStyleSheet("QPushButton {\n"
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
        self.botonGuardar.setObjectName("botonGuardar")
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
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(440, 530, 371, 21))
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

        self.nombrecl_edit.setReadOnly(True)
        self.ApellidoP_edit.setReadOnly(True)
        self.ApellidoM_edit.setReadOnly(True)
        self.precio_edit.setReadOnly(True)
        self.nombrecl_edit.setText(f"{main.cliente.nombres}")
        self.ApellidoP_edit.setText(f"{main.cliente.apellido_paterno}")
        self.ApellidoM_edit.setText(f"{main.cliente.apellido_materno}")

        for i in main.cliente.mascotas:
            self.mascota_edit.addItem(f"{i.nombreM}")



        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow,InterfazMenuExamen.MenuExamen))
        self.fecha_edit.dateChanged.connect(lambda: self.disponibilidad())
        self.Tipo_edit.activated.connect(lambda: self.disponibilidad())
        self.botonGuardar.clicked.connect(lambda: self.guardar(MainWindow))
          
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

    def guardar(self,MainWindow):
        if self.nombrecl_edit.text() == "" or self.ApellidoP_edit.text() == "" or self.ApellidoM_edit.text() == "" or self.mascota_edit.currentText() == "" \
                or self.Tipo_edit.currentText() == "" or self.fecha_edit.text() == "" or self.hora_edit.currentText() == "" or self.precio_edit.text() == "":
            self.TxtNoEncontrado.show()
            datos = [self.nombrecl_edit, self.ApellidoP_edit, self.ApellidoM_edit, self.mascota_edit, self.Tipo_edit,
                     self.fecha_edit, self.hora_edit, self.precio_edit]
            for i in datos:
                try:
                    if i.text() == "":
                        i.setStyleSheet("border-style: solid;\n"
                                        "border-color: red;\n"
                                        "border-width: 1px;")
                    else:
                        i.setStyleSheet("")
                except:
                    if i.currentText() == "":
                        i.setStyleSheet("border-style: solid;\n"
                                        "border-color: red;\n"
                                        "border-width: 1px;")
                    else:
                        i.setStyleSheet("")
        else:
            nombres = self.nombrecl_edit.text()
            apellidoP = self.ApellidoP_edit.text()
            apellidoM = self.ApellidoM_edit.text()
            mascota = self.mascota_edit.currentText()
            fecha = self.fecha_edit.text()
            tipo = self.Tipo_edit.currentText()
            hora = self.hora_edit.currentText()
            precio = self.precio_edit.text()
            main.crearExamen(nombres,apellidoP,apellidoM,mascota,tipo,fecha,hora,precio)
            if InterfazNumeroDeExamenes.numeroExamenes == 1:
                self.cambio(MainWindow, InterfazExamenes.Examenes)
            elif InterfazNumeroDeExamenes.numeroExamenes > 1:
                InterfazNumeroDeExamenes.numeroExamenes -= 1
                self.cambio(MainWindow, CrearExamen)

    def disponibilidad(self):
        if self.Tipo_edit.currentText() == "Examen De Sangre":
            self.precio_edit.setText("25000")
        elif self.Tipo_edit.currentText() == "Secuenciamiento De Muestras Biologicas":
            self.precio_edit.setText("20000")
        elif self.Tipo_edit.currentText() == "Radiografia":
            self.precio_edit.setText("40000")
        elif self.Tipo_edit.currentText() == "Scanner Y Ecografia":
            self.precio_edit.setText("30000")
        self.hora_edit.clear()
        self.hora_edit.addItem("")
        horario = main.verifDispo(self.Tipo_edit.currentText(),self.fecha_edit.text())
        for i in horario:
            self.hora_edit.addItem(f"{i}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Crear Examen"))
        self.lbl_namecl.setText(_translate("MainWindow", "Nombres Cliente:"))
        self.lbl_appa.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.lbl_apm.setText(_translate("MainWindow", "Apellido Materno:"))
        self.lbl_mascota.setText(_translate("MainWindow", "Mascota:"))
        self.lb_tipo.setText(_translate("MainWindow", "Tipo:"))
        self.lbl_fecha.setText(_translate("MainWindow", "Fecha:"))
        self.lbl_hora.setText(_translate("MainWindow", "Hora:"))
        self.lbl_precio.setText(_translate("MainWindow", "Precio:"))
        self.botonGuardar.setText(_translate("MainWindow", "Guardar"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Complete Los Datos Para Continuar."))