from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QDialog, QMainWindow
from PyQt6.QtGui import QImage, QPixmap, QFont, QFontMetrics
from PyQt6.QtCore import Qt, QTimer, QRect, pyqtSlot
from PyQt6 import QtWidgets
import pyqtgraph as pg

#imports de librerias locales
import sys

#imports de librerias locales
from Capa_Presentacion.dialogs.TaconMain import Ui_Tacoinador
from Capa_Presentacion.dialogs.RegistrarDatosModeloWidget import Ui_RegistrarDatosModeloWidget
from Capa_Presentacion.dialogs.RegistrarModeloWidget import Ui_RegistrarModeloWidget

#Clase Principal
class Tacoinador(QMainWindow, Ui_Tacoinador):

    def __init__(self):
        super(Tacoinador, self).__init__()
        self.setupUi(self)
        self.registrarParametros_Widget = None
        self.registrarModelo_Widget = None

    def showRegistrarModelo(self):
        if self.registrarModelo_Widget is None:
            self.registrarModelo_Widget = RegistrarModeloWidget()
        self.registrarModelo_Widget.show()


    def showRegistrarParametros(self):
        if self.registrarParametros_Widget is None:
            # Crear una instancia de la clase IngresarModeloWidget
            self.registrarParametros_Widget = RegistrarDatosModeloWidget()  # Utilizamos la clase personalizada
        self.registrarParametros_Widget.show()  # Mostrar el widget

# Clase personalizada que hereda de QWidget y gestiona los eventos
class RegistrarDatosModeloWidget(QWidget):
    def __init__(self):
        super(RegistrarDatosModeloWidget, self).__init__()
        self.ui_RegistrarDatos = Ui_RegistrarDatosModeloWidget()  # Instanciar la interfaz generada
        self.ui_RegistrarDatos.setupUi(self)  # Configurar la interfaz en este widget

        self.move(430, 303)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(self.size())

        # Conectar los botones a los métodos (slots)
        self.ui_RegistrarDatos.ConfirmarRegistrodatos_Btn.clicked.connect(self.confirmarParametros)
        self.ui_RegistrarDatos.CancelarRegistroDatos_Btn.clicked.connect(self.cerrarRegistrarParametrosWidget)

    def confirmarParametros(self):
        print("Parametros confirmado")

    def cerrarRegistrarParametrosWidget(self):
        self.close()  

class RegistrarModeloWidget(QWidget):
    def __init__(self):
        super(RegistrarModeloWidget, self).__init__()
        self.ui_RegistrarModelo = Ui_RegistrarModeloWidget()
        self.ui_RegistrarModelo.setupUi(self)
        self.move(430, 303)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(self.size())

        self.ui_RegistrarModelo.IngresarModelo_Btn.clicked.connect(self.confirmarModelo) # type: ignore
        self.ui_RegistrarModelo.CancelarRegistroModelo_Btn.clicked.connect(self.cerrarRegistrarModeloWidget) # type: ignore

    def confirmarModelo(self):
        # Lógica para confirmar el modelo
        print("Modelo confirmado")

    def cerrarRegistrarModeloWidget(self):
        # Lógica para cerrar el widget
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Tacoinador()
    window.show()
    sys.exit(app.exec())