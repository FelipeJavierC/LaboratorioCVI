from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazCrearCliente
import InterfazEditar
import InterfazMenuCliente
import InterfazNumeroMascotas
import main

class CrearMascota(object):

    def setupUi(self, MainWindow,Bandera):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 521)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Fondo.setFont(font)
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
        self.BotonGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonGuardar.setGeometry(QtCore.QRect(430, 430, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.BotonGuardar.setFont(font)
        self.BotonGuardar.setTabletTracking(True)
        self.BotonGuardar.setAcceptDrops(True)
        self.BotonGuardar.setStyleSheet("background-color: #00A2FF;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 3px;\n"
        "border-radius: 20px;")
        self.BotonGuardar.setAutoRepeatDelay(300)
        self.BotonGuardar.setObjectName("BotonGuardar")
        self.Marco = QtWidgets.QLabel(self.centralwidget)
        self.Marco.setGeometry(QtCore.QRect(90, 150, 781, 231))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.Marco.setFont(font)
        self.Marco.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.Marco.setText("")
        self.Marco.setObjectName("Marco")
        self.text_7 = QtWidgets.QLabel(self.centralwidget)
        self.text_7.setGeometry(QtCore.QRect(120, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_7.setFont(font)
        self.text_7.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_7.setObjectName("text_7")
        self.text_9 = QtWidgets.QLabel(self.centralwidget)
        self.text_9.setGeometry(QtCore.QRect(120, 330, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_9.setFont(font)
        self.text_9.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_9.setObjectName("text_9")
        self.text_6 = QtWidgets.QLabel(self.centralwidget)
        self.text_6.setGeometry(QtCore.QRect(470, 180, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_6.setObjectName("text_6")
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(120, 260, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_3.setFont(font)
        self.text_3.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(self.centralwidget)
        self.text_4.setGeometry(QtCore.QRect(380, 330, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_4.setObjectName("text_4")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(600, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_2.setObjectName("text_2")
        self.Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(200, 180, 241, 20))
        self.Nombre.setObjectName("Nombres")
        self.Especie = QtWidgets.QLineEdit(self.centralwidget)
        self.Especie.setGeometry(QtCore.QRect(560, 180, 281, 20))
        self.Especie.setObjectName("Especie")
        self.Raza = QtWidgets.QLineEdit(self.centralwidget)
        self.Raza.setGeometry(QtCore.QRect(190, 260, 211, 20))
        self.Raza.setObjectName("Raza")
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(550, 260, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_5.setFont(font)
        self.text_5.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_5.setObjectName("text_5")
        self.Sexo = QtWidgets.QComboBox(self.centralwidget)
        self.Sexo.setGeometry(QtCore.QRect(180, 330, 151, 22))
        self.Sexo.setObjectName("Sexo")
        self.Sexo.addItem("")
        self.Sexo.setItemText(0, "")
        self.Sexo.addItem("")
        self.Sexo.addItem("")
        self.FechaNacimiento = QtWidgets.QDateEdit(self.centralwidget)
        self.FechaNacimiento.setGeometry(QtCore.QRect(700, 260, 141, 22))
        self.FechaNacimiento.setObjectName("FechaNacimiento")
        self.Peso = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Peso.setGeometry(QtCore.QRect(450, 330, 121, 22))
        self.Peso.setObjectName("Peso")
        self.Peso.setMaximum(500)
        self.text_10 = QtWidgets.QLabel(self.centralwidget)
        self.text_10.setGeometry(QtCore.QRect(540, 330, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_10.setFont(font)
        self.text_10.setStyleSheet("background-color: no color;")
        self.text_10.setObjectName("text_10")
        self.Tamano = QtWidgets.QComboBox(self.centralwidget)
        self.Tamano.setGeometry(QtCore.QRect(680, 330, 161, 22))
        self.Tamano.setObjectName("Tamano")
        self.Tamano.addItem("")
        self.Tamano.setItemText(0, "")
        self.Tamano.addItem("")
        self.Tamano.addItem("")
        self.Tamano.addItem("")
        self.Fondo.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.BotonGuardar.raise_()
        self.Marco.raise_()
        self.text_7.raise_()
        self.text_9.raise_()
        self.text_6.raise_()
        self.text_3.raise_()
        self.text_4.raise_()
        self.text_2.raise_()
        self.Nombre.raise_()
        self.Especie.raise_()
        self.Raza.raise_()
        self.text_5.raise_()
        self.Sexo.raise_()
        self.FechaNacimiento.raise_()
        self.Peso.raise_()
        self.text_10.raise_()
        self.Tamano.raise_()
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(300, 380, 371, 21))
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

        self.BotonGuardar.clicked.connect(lambda: self.guardar(Bandera,MainWindow))
        if Bandera == True:
            self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazNumeroMascotas.NumeroMascotas))

        else:
            self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazEditar.Editar))


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

    def guardar(self,Bandera,MainWindow):
        if self.Nombre.text() == "" or self.Especie.text() == "" or self.Raza.text() == "" or self.FechaNacimiento.text() == "" or self.Sexo.currentText() == "" or \
                self.Peso.text() == "" or self.Tamano.currentText() == "":
            self.TxtNoEncontrado.show()
            datos = [self.Nombre, self.Especie, self.Raza, self.FechaNacimiento, self.Sexo,
                     self.Peso, self.Tamano]
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
            nombre = self.Nombre.text()
            especie = self.Especie.text()
            raza = self.Raza.text()
            fechaNacimiento = self.FechaNacimiento.text()
            sexo = self.Sexo.currentText()
            peso = self.Peso.text()
            tamaño = self.Tamano.currentText()
            main.crearMascota(nombre,especie,raza,fechaNacimiento,sexo,peso,tamaño)
            print(main.cliente.nombreCompleto, main.cliente.mascotas)
            if Bandera == True:
                if InterfazNumeroMascotas.numeroMascotas == 1:
                    self.cambio(MainWindow, InterfazMenuCliente.MenuCliente)
                elif InterfazNumeroMascotas.numeroMascotas > 1:
                    InterfazNumeroMascotas.numeroMascotas -= 1
                    self.cambio2(MainWindow, CrearMascota, True)
            else:
                self.cambio(MainWindow, InterfazEditar.Editar)

    def cambio2(self, MainWindow,Interfaz,Bandera):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana,Bandera)
        self.ventana.show()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Crear Mascota"))
        self.Titulo.setText(_translate("MainWindow", "CREAR MASCOTA"))
        self.BotonGuardar.setText(_translate("MainWindow", "GUARDAR"))
        self.text_7.setText(_translate("MainWindow", "Nombre:"))
        self.text_9.setText(_translate("MainWindow", "Sexo:"))
        self.text_6.setText(_translate("MainWindow", "Especie:"))
        self.text_3.setText(_translate("MainWindow", "Raza:"))
        self.text_4.setText(_translate("MainWindow", "Peso:"))
        self.text_2.setText(_translate("MainWindow", "Tamaño:"))
        self.text_5.setText(_translate("MainWindow", "Fecha De Nacimiento:"))
        self.Sexo.setItemText(1, _translate("MainWindow", "Macho"))
        self.Sexo.setItemText(2, _translate("MainWindow", "Hembra"))
        self.text_10.setText(_translate("MainWindow", "kg"))
        self.Tamano.setItemText(1, _translate("MainWindow", "Pequeño"))
        self.Tamano.setItemText(2, _translate("MainWindow", "Mediano"))
        self.Tamano.setItemText(3, _translate("MainWindow", "Grande"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Complete Los Datos Para Continuar."))