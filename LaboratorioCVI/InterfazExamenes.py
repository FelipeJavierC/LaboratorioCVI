import InterfazMenuExamen
import main
import res

from PyQt5 import QtCore, QtGui, QtWidgets


class Examenes(object):
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
        self.tableExamen = QtWidgets.QTableWidget(self.principal)
        self.tableExamen.setGeometry(QtCore.QRect(130, 251, 811, 191))

        self.tableExamen.setObjectName("tableExamen")

        data = []
        for i in main.examenes:
            if i.estado == "True":
                estado = "Finalizado"
            elif i.estado == "False":
                estado = "En Espera"
            data.append([f"{i.nombreCliente}",f"{i.apellidoP}",f"{i.mascota}",f"{i.tipo}",f"{i.hora}",f"{i.fecha}",f"{i.precio}",f"{estado}"])
        f = len(data)
        c = len(data[0])
        self.tableExamen.setRowCount(f)
        self.tableExamen.setColumnCount(c)

        for i in range(f):
            for j in range(c):
                self.tableExamen.setItem(i, j,QtWidgets.QTableWidgetItem(data[i][j]))

        self.tableExamen.setHorizontalHeaderLabels(["Nombre Cliente","Apellido","Mascota","Examen","Hora","Fecha","Precio","Estado"])

        self.tableExamen.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableExamen.horizontalHeader().setStretchLastSection(True)

        self.botonAgendar = QtWidgets.QPushButton(self.principal)
        self.botonAgendar.setGeometry(QtCore.QRect(580, 490, 141, 41))
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
        self.label = QtWidgets.QLabel(self.principal)
        self.label.setGeometry(QtCore.QRect(130, 450, 421, 121))
        self.label.setStyleSheet("font: 75 17pt \"MS Sans Serif\";\n"
"background: #FFFFFF;\n"
"border-radius:20px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.principal)
        self.label_2.setGeometry(QtCore.QRect(180, 470, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.principal)
        self.label_3.setGeometry(QtCore.QRect(179, 540, 55, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.principal)
        self.label_4.setGeometry(QtCore.QRect(180, 504, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_subtotal = QtWidgets.QLabel(self.principal)
        self.label_subtotal.setGeometry(QtCore.QRect(370, 460, 161, 31))
        self.label_subtotal.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:10px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.label_subtotal.setText("")
        self.label_subtotal.setObjectName("label_subtotal")
        self.label_total = QtWidgets.QLabel(self.principal)
        self.label_total.setGeometry(QtCore.QRect(370, 530, 161, 31))
        self.label_total.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:10px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.label_total.setText("")
        self.label_total.setObjectName("label_total")
        self.label_descuento = QtWidgets.QLabel(self.principal)
        self.label_descuento.setGeometry(QtCore.QRect(370, 495, 161, 31))
        self.label_descuento.setStyleSheet("\n"
"background: #FFFFFF;\n"
"border-radius:10px;\n"
"\n"
"border: 4px solid #222d5b ;")
        self.label_descuento.setText("")
        self.label_descuento.setObjectName("label_descuento")
        precio = 0
        for i in main.examenes:
            precio+=int(i.precio)
        self.label_subtotal.setText(f"{precio}")
        descuento = main.descuento(precio)
        self.label_descuento.setText(f"{int(descuento)}")
        total = precio-descuento
        self.label_total.setText(f"{int(total)}")
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

        self.botonAtras.clicked.connect(lambda: self.cambio2(MainWindow,InterfazMenuExamen.MenuExamen))
        self.botonAgendar.clicked.connect(lambda: self.guardar(MainWindow))

   

    def cerrar_ventana(self):
        QtCore.QCoreApplication.quit()

 # No tocar

    def cambio2(self, MainWindow,Interfaz):
        main.borrarHorarios()
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def guardar(self, MainWindow):
        main.guardarExamenes()
        self.cambio(MainWindow,InterfazMenuExamen.MenuExamen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Examenes"))
        self.botonAgendar.setText(_translate("MainWindow", "Agendar"))
        self.label_2.setText(_translate("MainWindow", "Subtotal"))
        self.label_3.setText(_translate("MainWindow", "Total"))
        self.label_4.setText(_translate("MainWindow", "Descuento"))