from PyQt5 import QtCore, QtGui, QtWidgets

import InterfazEditar
import main

class EditarCliente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(991, 521)
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
        self.Marco = QtWidgets.QLabel(self.centralwidget)
        self.Marco.setGeometry(QtCore.QRect(90, 140, 781, 271))
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
        self.text_7.setGeometry(QtCore.QRect(120, 170, 61, 21))
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
        self.text_8 = QtWidgets.QLabel(self.centralwidget)
        self.text_8.setGeometry(QtCore.QRect(580, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_8.setFont(font)
        self.text_8.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_8.setObjectName("text_8")
        self.text_9 = QtWidgets.QLabel(self.centralwidget)
        self.text_9.setGeometry(QtCore.QRect(120, 290, 41, 21))
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
        self.text_10 = QtWidgets.QLabel(self.centralwidget)
        self.text_10.setGeometry(QtCore.QRect(390, 230, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text_10.setFont(font)
        self.text_10.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text_10.setObjectName("text_10")
        self.text_6 = QtWidgets.QLabel(self.centralwidget)
        self.text_6.setGeometry(QtCore.QRect(470, 170, 101, 21))
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
        self.text_5 = QtWidgets.QLabel(self.centralwidget)
        self.text_5.setGeometry(QtCore.QRect(600, 290, 61, 21))
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
        self.text_3 = QtWidgets.QLabel(self.centralwidget)
        self.text_3.setGeometry(QtCore.QRect(120, 230, 101, 21))
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
        self.text_4.setGeometry(QtCore.QRect(340, 290, 41, 21))
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
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(470, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.text.setFont(font)
        self.text.setStyleSheet("background-color: white;\n"
        "border-style: solid;\n"
        "border-color: black;\n"
        "border-width: 2px;")
        self.text.setObjectName("text")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(120, 350, 61, 21))
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
        self.Nombres = QtWidgets.QLineEdit(self.centralwidget)
        self.Nombres.setGeometry(QtCore.QRect(190, 170, 261, 20))
        self.Nombres.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.Nombres.setText("")
        self.Nombres.setObjectName("Nombres")
        self.ApellidoP = QtWidgets.QLineEdit(self.centralwidget)
        self.ApellidoP.setGeometry(QtCore.QRect(580, 170, 261, 20))
        self.ApellidoP.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ApellidoP.setObjectName("ApellidoP")
        self.ApellidoM = QtWidgets.QLineEdit(self.centralwidget)
        self.ApellidoM.setGeometry(QtCore.QRect(230, 230, 141, 20))
        self.ApellidoM.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ApellidoM.setObjectName("ApellidoM")
        self.Domicilio = QtWidgets.QLineEdit(self.centralwidget)
        self.Domicilio.setGeometry(QtCore.QRect(190, 350, 261, 20))
        self.Domicilio.setStyleSheet("")
        self.Domicilio.setObjectName("Domicilio")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(390, 290, 191, 20))
        self.Email.setStyleSheet("")
        self.Email.setObjectName("Email")
        self.Rut = QtWidgets.QLineEdit(self.centralwidget)
        self.Rut.setGeometry(QtCore.QRect(170, 290, 151, 20))
        self.Rut.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.Rut.setObjectName("Rut")
        self.Telefono = QtWidgets.QLineEdit(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(670, 290, 171, 20))
        self.Telefono.setStyleSheet("")
        self.Telefono.setObjectName("Telefono")
        self.FechaNacimiento = QtWidgets.QLineEdit(self.centralwidget)
        self.FechaNacimiento.setGeometry(QtCore.QRect(710, 230, 131, 20))
        self.FechaNacimiento.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.FechaNacimiento.setObjectName("FechaNacimiento")
        self.Genero = QtWidgets.QLineEdit(self.centralwidget)
        self.Genero.setGeometry(QtCore.QRect(460, 230, 101, 20))
        self.Genero.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.Genero.setObjectName("Genero")
        self.DerivadoDe = QtWidgets.QComboBox(self.centralwidget)
        self.DerivadoDe.setGeometry(QtCore.QRect(550, 350, 281, 22))
        self.DerivadoDe.setObjectName("DerivadoDe_2")
        self.DerivadoDe.addItem("")
        self.DerivadoDe.setItemText(0, "")
        self.DerivadoDe.addItem("")
        self.DerivadoDe.addItem("")
        self.Fondo.raise_()
        self.Titulo.raise_()
        self.BotonAtras.raise_()
        self.Marco.raise_()
        self.text_7.raise_()
        self.text_8.raise_()
        self.text_9.raise_()
        self.text_10.raise_()
        self.text_6.raise_()
        self.text_5.raise_()
        self.text_3.raise_()
        self.text_4.raise_()
        self.text.raise_()
        self.text_2.raise_()
        self.Nombres.raise_()
        self.ApellidoP.raise_()
        self.ApellidoM.raise_()
        self.Domicilio.raise_()
        self.Email.raise_()
        self.Rut.raise_()
        self.Telefono.raise_()
        self.FechaNacimiento.raise_()
        self.Genero.raise_()
        self.DerivadoDe.raise_()
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
        self.Nombres.setReadOnly(True)
        self.ApellidoP.setReadOnly(True)
        self.ApellidoM.setReadOnly(True)
        self.Genero.setReadOnly(True)
        self.FechaNacimiento.setReadOnly(True)
        self.Rut.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Nombres.setText(f"{main.cliente.nombres}")
        self.ApellidoP.setText(f"{main.cliente.apellido_paterno}")
        self.ApellidoM.setText(f"{main.cliente.apellido_materno}")
        self.Genero.setText(f"{main.cliente.genero}")
        self.FechaNacimiento.setText(f"{main.cliente.fecha_nacimiento}")
        self.Rut.setText(f"{main.cliente.rut}")

        self.BotonAtras.clicked.connect(lambda: self.cambio(MainWindow, InterfazEditar.Editar))
        self.BotonGuardar.clicked.connect(lambda: self.guardar(MainWindow))

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def guardar(self, MainWindow):
        if self.Email.text() == "" or self.Telefono.text() == "" or self.Domicilio.text() == "" or self.DerivadoDe.currentText() == "":
            self.TxtNoEncontrado.show()
            datos = [self.Email, self.Telefono, self.Domicilio, self.DerivadoDe]
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
            main.cliente.cambiarEmail(self.Email.text())
            main.cliente.cambiarTelefono(self.Telefono.text())
            main.cliente.cambiarDomicilio(self.Domicilio.text())
            main.cliente.cambiarDerivado(self.DerivadoDe.currentText())
            main.borrarCliente()
            main.guardarDatos('Clientes.csv', main.cliente.toStringCliente())
            self.cambio(MainWindow, InterfazEditar.Editar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Editar Cliente"))
        self.Titulo.setText(_translate("MainWindow", "EDITAR CLIENTE"))
        self.text_7.setText(_translate("MainWindow", "Nombres:"))
        self.text_8.setText(_translate("MainWindow", "Fecha De Nacimiento:"))
        self.text_9.setText(_translate("MainWindow", "Rut:"))
        self.text_10.setText(_translate("MainWindow", "Genero:"))
        self.text_6.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.text_5.setText(_translate("MainWindow", "Telefono:"))
        self.text_3.setText(_translate("MainWindow", "Apellido Materno:"))
        self.text_4.setText(_translate("MainWindow", "Email:"))
        self.text.setText(_translate("MainWindow", "Derivado De:"))
        self.text_2.setText(_translate("MainWindow", "Domicilio:"))
        self.DerivadoDe.setItemText(1, _translate("MainWindow", "Clinica CVI"))
        self.DerivadoDe.setItemText(2, _translate("MainWindow", "Otro"))
        self.BotonGuardar.setText(_translate("MainWindow", "GUARDAR"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Complete Los Datos Para Continuar."))
