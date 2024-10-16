from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(329, 528)

        # Etiqueta para Usuario
        self.UsuarioLabel = QtWidgets.QLabel(parent=LoginDialog)
        self.UsuarioLabel.setGeometry(QtCore.QRect(140, 70, 47, 13))
        self.UsuarioLabel.setObjectName("UsuarioLabel")
        
        # Campo de texto para ingresar Usuario
        self.Usuario_textEdit = QtWidgets.QLineEdit(parent=LoginDialog)  # Cambié a QLineEdit
        self.Usuario_textEdit.setGeometry(QtCore.QRect(80, 100, 151, 31))
        self.Usuario_textEdit.setObjectName("Usuario_textEdit")
        
        # Etiqueta para Contraseña
        self.PasswordLabel = QtWidgets.QLabel(parent=LoginDialog)
        self.PasswordLabel.setGeometry(QtCore.QRect(140, 190, 47, 13))
        self.PasswordLabel.setObjectName("PasswordLabel")
        
        # Campo de texto para ingresar la Contraseña
        self.Password_textEdit = QtWidgets.QLineEdit(parent=LoginDialog)  # Cambié a QLineEdit
        self.Password_textEdit.setGeometry(QtCore.QRect(80, 230, 151, 31))
        self.Password_textEdit.setObjectName("Password_textEdit")
        self.Password_textEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Ocultar el texto
        
        # Botón de login
        self.LoginBtn = QtWidgets.QPushButton(parent=LoginDialog)
        self.LoginBtn.setGeometry(QtCore.QRect(120, 320, 75, 23))
        self.LoginBtn.setObjectName("LoginBtn")

        self.retranslateUi(LoginDialog)
        # Conectar el botón a la función validate_login y pasar el QDialog como argumento
        self.LoginBtn.clicked.connect(lambda: self.validate_login(LoginDialog))  # Pasar LoginDialog
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Iniciar Sesión"))
        self.UsuarioLabel.setText(_translate("LoginDialog", "Usuario"))
        self.PasswordLabel.setText(_translate("LoginDialog", "Contraseña"))
        self.LoginBtn.setText(_translate("LoginDialog", "Entrar"))

    def validate_login(self, dialog):
        # Aquí podrías agregar validaciones reales, por ejemplo:
        usuario = self.Usuario_textEdit.text()
        password = self.Password_textEdit.text()

        # Simulando que el usuario y contraseña son correctos si ambos no están vacíos
        if usuario == "" and password == "":  # Solo un ejemplo simple
            dialog.accept()  # Aceptar el diálogo si el login es correcto
        else:
            # Mostrar un mensaje de error o simplemente no aceptar el diálogo
            QtWidgets.QMessageBox.warning(None, "Error", "Usuario o contraseña incorrectos")
