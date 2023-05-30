import Examen
import InterfazBorrado
import InterfazMenuExamen
import main
import res
from PyQt5 import QtCore, QtGui, QtWidgets

examen = Examen

class BorrarExamen(object):
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
        self.tableExamen.setGeometry(QtCore.QRect(120, 240, 831, 251))
        self.tableExamen.setObjectName("tableExamen")
        self.tableExamen.setColumnCount(0)
        self.tableExamen.setRowCount(0)

        data = []
        for i in main.examenes:
            if i.estado == "True":
                estado = "Finalizado"
            elif i.estado == "False":
                estado = "En Espera"
            data.append([f"{i.nombreCliente}", f"{i.apellidoP}", f"{i.mascota}", f"{i.tipo}", f"{i.hora}", f"{i.fecha}",
                         f"{i.precio}", f"{estado}"])
        f = len(data)
        c = len(data[0])
        self.tableExamen.setRowCount(f)
        self.tableExamen.setColumnCount(c)

        for i in range(f):
            for j in range(c):
                self.tableExamen.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))

        self.tableExamen.setHorizontalHeaderLabels(
            ["Nombre Cliente", "Apellido", "Mascota", "Examen", "Hora", "Fecha", "Precio", "Estado"])

        self.tableExamen.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableExamen.horizontalHeader().setStretchLastSection(True)

        self.botonConfirmar = QtWidgets.QPushButton(self.principal)
        self.botonConfirmar.setGeometry(QtCore.QRect(460, 510, 141, 41))
        self.botonConfirmar.setStyleSheet("QPushButton {\n"
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
        self.botonConfirmar.setObjectName("botonConfirmar")
        self.tit_labcvi.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.botonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazMenuExamen.MenuExamen))
        self.tableExamen.clicked.connect(lambda: self.guardarExamen(MainWindow, self.tableExamen.currentRow()))
        self.botonConfirmar.clicked.connect(lambda: self.borrar())
  
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

    def borrar(self):
        global examen
        if examen != Examen:
            main.borrarExamen(examen.hora, examen.fecha)
            main.borrarHorario(examen.hora, examen.fecha)
            self.abrir(InterfazBorrado.Borrado)
            main.examenes.clear()
            main.horarios.clear()
            main.cargarDatosExamen()
            self.tableExamen.setRowCount(0)
            self.tableExamen.setColumnCount(0)
            try:
                data = []
                for i in main.examenes:
                    if i.estado == "True":
                        estado = "Finalizado"
                    elif i.estado == "False":
                        estado = "En Espera"
                    data.append([f"{i.nombreCliente}", f"{i.apellidoP}", f"{i.mascota}", f"{i.tipo}", f"{i.hora}", f"{i.fecha}",
                                 f"{i.precio}", f"{estado}"])
                f = len(data)
                c = len(data[0])
                self.tableExamen.setRowCount(f)
                self.tableExamen.setColumnCount(c)

                for i in range(f):
                    for j in range(c):
                        self.tableExamen.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))

                self.tableExamen.setHorizontalHeaderLabels(
                    ["Nombre Cliente", "Apellido", "Mascota", "Examen", "Hora", "Fecha", "Precio", "Estado"])
            except:
                pass
            examen = Examen


    def guardarExamen(self, MainWindow, row):
        global examen
        print(row)
        hora = self.tableExamen.item(row, 4)
        fecha = self.tableExamen.item(row, 5)
        examen = main.buscarExamen(hora.text(),fecha.text())

    def abrir(self,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
     
# No tocar


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.tit_labcvi.setText(_translate("MainWindow", "Borrar Examen"))
        self.botonConfirmar.setText(_translate("MainWindow", "Confirmar"))