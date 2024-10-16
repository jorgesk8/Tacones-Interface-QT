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
        pass


    def showRegistrarParametros(self):
        pass

    def showVisionPage(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Tacoinador()
    window.show()
    sys.exit(app.exec())