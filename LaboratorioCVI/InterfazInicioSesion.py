import InterfazMenu
import main
import resSesion
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class InicioSesion(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 827)


        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)




        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.principal = QtWidgets.QWidget(self.centralwidget)
        self.principal.setGeometry(QtCore.QRect(60, 60, 481, 671))
        self.principal.setObjectName("principal")
        self.fondo = QtWidgets.QLabel(self.principal)
        self.fondo.setGeometry(QtCore.QRect(30, 10, 431, 641))
        self.fondo.setStyleSheet("border-radius: 15px;\n"
"border-image: url(:/image/fondo.jpg);")
        self.fondo.setText("")
        self.fondo.setObjectName("fondo")
        self.icn_user = QtWidgets.QLabel(self.principal)
        self.icn_user.setGeometry(QtCore.QRect(190, 90, 111, 111))
        self.icn_user.setStyleSheet("border-image: url(:/image/Usuario.png);")
        self.icn_user.setText("")
        self.icn_user.setObjectName("icn_user")
        self.label_sesion = QtWidgets.QLabel(self.principal)
        self.label_sesion.setGeometry(QtCore.QRect(150, 210, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_sesion.setFont(font)
        self.label_sesion.setStyleSheet("QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 20pt;\n"
"}\n"
"")
        self.label_sesion.setObjectName("label_sesion")
        self.icn_correo = QtWidgets.QLabel(self.principal)
        self.icn_correo.setGeometry(QtCore.QRect(130, 300, 41, 41))
        self.icn_correo.setStyleSheet("border-image: url(:/image/correo.png);")
        self.icn_correo.setText("")
        self.icn_correo.setObjectName("icn_correo")
        self.icn_pass = QtWidgets.QLabel(self.principal)
        self.icn_pass.setGeometry(QtCore.QRect(140, 380, 21, 21))
        self.icn_pass.setStyleSheet("border-image: url(:/image/candado.png);")
        self.icn_pass.setText("")
        self.icn_pass.setObjectName("icn_pass")
        self.line_mail = QtWidgets.QFrame(self.principal)
        self.line_mail.setGeometry(QtCore.QRect(170, 320, 171, 16))
        self.line_mail.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_mail.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_mail.setObjectName("line_mail")
        self.line_pass = QtWidgets.QFrame(self.principal)
        self.line_pass.setGeometry(QtCore.QRect(170, 390, 171, 16))
        self.line_pass.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_pass.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_pass.setObjectName("line_pass")
        self.botonIngresar = QtWidgets.QPushButton(self.principal)
        self.botonIngresar.setGeometry(QtCore.QRect(120, 460, 261, 51))
        self.botonIngresar.setStyleSheet("QPushButton {\n"
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
        self.botonIngresar.setObjectName("botonIngresar")
        self.edit_email = QtWidgets.QLineEdit(self.principal)
        self.edit_email.setGeometry(QtCore.QRect(180, 300, 161, 31))
        self.edit_email.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #ffffff;\n"
"    border: none;\n"
"}")
        self.edit_email.setText("")
        self.edit_email.setObjectName("edit_email")


        #este es mi pass_edit
        self.edit_pass = QtWidgets.QLineEdit(self.principal)
        self.edit_pass.setGeometry(QtCore.QRect(180, 370, 161, 31))


        self.edit_pass.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    color: #ffffff;\n"
"}")
        self.edit_pass.setText("")
        self.edit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_pass.setObjectName("edit_pass")
        self.frame_superior = QtWidgets.QFrame(self.principal)
        self.frame_superior.setGeometry(QtCore.QRect(29, 9, 431, 41))
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.boton_minimize = QtWidgets.QPushButton(self.frame_superior)
        self.boton_minimize.setGeometry(QtCore.QRect(370, 10, 21, 21))
        self.boton_minimize.setStyleSheet("QPushButton {\n"
"    border: 0;\n"
"    background: #7EC6FF;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-family: Helvetica Neue;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #9500ff, stop:1 #00DDFF);\n"
"}\n"
"")
        self.boton_minimize.setObjectName("boton_minimize")
        self.botonExit = QtWidgets.QPushButton(self.frame_superior)
        self.botonExit.setGeometry(QtCore.QRect(400, 10, 21, 21))
        self.botonExit.setStyleSheet("QPushButton {\n"
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
        self.botonExit.setObjectName("botonExit")


        #este es mi boton ver_pass
        self.boton_verpass = QtWidgets.QPushButton(self.principal)
        self.boton_verpass.setGeometry(QtCore.QRect(350, 370, 31, 21))
        self.boton_verpass.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"    border: 0;\n"
"    background: #7EC6FF;\n"
"    border-radius: 7px;\n"
" \n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/ver1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_verpass.setIcon(icon)
        self.boton_verpass.setIconSize(QtCore.QSize(20, 20))

      
  
        self.boton_verpass.setObjectName("boton_verpass")
        self.TxtNoEncontrado = QtWidgets.QLabel(self.centralwidget)
        self.TxtNoEncontrado.setGeometry(QtCore.QRect(120, 470, 371, 21))
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
                                           "color:white;")
        self.TxtNoEncontrado.setTextFormat(QtCore.Qt.AutoText)
        self.TxtNoEncontrado.setAlignment(QtCore.Qt.AlignCenter)
        self.TxtNoEncontrado.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.TxtNoEncontrado.setObjectName("TxtNoEncontrado")
        self.TxtNoEncontrado.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.botonIngresar.clicked.connect(lambda: self.guardar(MainWindow))


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
        #poner boton aqui
        self.boton_verpass.clicked.connect(self.cambiar_mod_pass)

       

    def cerrar_ventana(self):
        QtCore.QCoreApplication.quit()


         
    def cambiar_icono_pass(self):
        size_pass_visible = QtCore.QSize(43, 43)  
        size_pass_hidden = QtCore.QSize(20, 20)      

        if self.is_pass_visible:
                icon = QtGui.QIcon(":/image/OculatarContraseñaBlanco.png")
                icon_actual = icon.pixmap(size_pass_visible)
        else:
                icon = QtGui.QIcon(":/image/ver1.png")
                icon_actual = icon.pixmap(size_pass_hidden)

        self.boton_verpass.setIcon(QtGui.QIcon(icon_actual))
        self.boton_verpass.setIconSize(icon_actual.size())


        #Esta funcion se utiliza para cambiar el modo del qline edit del password

    def cambiar_mod_pass(self):

        if self.edit_pass.echoMode() == QtWidgets.QLineEdit.Password:
            self.edit_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.is_pass_visible = True


        else:
            self.edit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.is_pass_visible = False
        
        self.cambiar_icono_pass()
 # No tocar

    def mostrar(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = InicioSesion()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def cambio(self, MainWindow,Interfaz):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Interfaz()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.close()

    def guardar(self,MainWindow):
        usuario = main.cargarDatosUsuario(self.edit_email.text(),self.edit_pass.text())
        if usuario == False:
            self.TxtNoEncontrado.show()
        else:
            self.cambio(MainWindow,InterfazMenu.Menu)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sesion.setText(_translate("MainWindow", "Inicio de Sesion"))
        self.botonIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.edit_email.setPlaceholderText(_translate("MainWindow", "Email ID"))
        self.edit_pass.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.boton_minimize.setText(_translate("MainWindow", "-"))
        self.botonExit.setText(_translate("MainWindow", "X"))
        self.TxtNoEncontrado.setText(_translate("MainWindow", "Ingrese Usuario Valido."))