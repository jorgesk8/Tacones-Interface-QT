# Form implementation generated from reading ui file 'TaconMain.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Tacoinador(object):
    def setupUi(self, Tacoinador):
        Tacoinador.setObjectName("Tacoinador")
        Tacoinador.resize(1920, 1080)
        Tacoinador.setMinimumSize(QtCore.QSize(1920, 1080))
        Tacoinador.setStyleSheet("\n"
"background-color: rgb(176, 155, 101);")
        self.centralwidget = QtWidgets.QWidget(parent=Tacoinador)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1921, 120))
        self.frame_4.setStyleSheet("background-color: rgb(153, 148, 137);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tituloLabel = QtWidgets.QLabel(parent=self.frame_4)
        self.tituloLabel.setGeometry(QtCore.QRect(240, 20, 721, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setObjectName("tituloLabel")
        self.frame_8 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(0, 480, 311, 361))
        self.frame_8.setStyleSheet("\n"
"background-color: rgb(214, 198, 156);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.RegistrarParametrosBtn = QtWidgets.QPushButton(parent=self.frame_8)
        self.RegistrarParametrosBtn.setGeometry(QtCore.QRect(0, 240, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.RegistrarParametrosBtn.setFont(font)
        self.RegistrarParametrosBtn.setStyleSheet("background-color: rgb(229, 190, 88);")
        self.RegistrarParametrosBtn.setObjectName("RegistrarParametrosBtn")
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_11.setGeometry(QtCore.QRect(0, 0, 311, 111))
        self.frame_11.setStyleSheet("background-color: rgb(153, 148, 137);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.inspeccionLabel_3 = QtWidgets.QLabel(parent=self.frame_11)
        self.inspeccionLabel_3.setGeometry(QtCore.QRect(10, 10, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.inspeccionLabel_3.setFont(font)
        self.inspeccionLabel_3.setObjectName("inspeccionLabel_3")
        self.RegistrarModeloBtn = QtWidgets.QPushButton(parent=self.frame_8)
        self.RegistrarModeloBtn.setGeometry(QtCore.QRect(0, 120, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.RegistrarModeloBtn.setFont(font)
        self.RegistrarModeloBtn.setStyleSheet("background-color: rgb(229, 190, 88);")
        self.RegistrarModeloBtn.setObjectName("RegistrarModeloBtn")
        self.frame_9 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(0, 1050, 1921, 31))
        self.frame_9.setStyleSheet("\n"
"background-color: rgb(153, 148, 137);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(320, 190, 1601, 861))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.visionPage = QtWidgets.QWidget()
        self.visionPage.setObjectName("visionPage")
        self.seleccionTaconFrame = QtWidgets.QFrame(parent=self.visionPage)
        self.seleccionTaconFrame.setGeometry(QtCore.QRect(1280, 20, 311, 271))
        self.seleccionTaconFrame.setStyleSheet("background-color: rgb(214, 198, 156);")
        self.seleccionTaconFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.seleccionTaconFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.seleccionTaconFrame.setObjectName("seleccionTaconFrame")
        self.frame_10 = QtWidgets.QFrame(parent=self.seleccionTaconFrame)
        self.frame_10.setGeometry(QtCore.QRect(0, 0, 311, 121))
        self.frame_10.setStyleSheet("\n"
"background-color: rgb(153, 148, 137);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.inspeccionLabel_2 = QtWidgets.QLabel(parent=self.frame_10)
        self.inspeccionLabel_2.setGeometry(QtCore.QRect(20, 0, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.inspeccionLabel_2.setFont(font)
        self.inspeccionLabel_2.setObjectName("inspeccionLabel_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.seleccionTaconFrame)
        self.comboBox.setGeometry(QtCore.QRect(130, 140, 161, 51))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(parent=self.seleccionTaconFrame)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(176, 155, 101);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.seleccionTaconFrame)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(176, 155, 101);")
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.seleccionTaconFrame)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 200, 161, 51))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.iniciarMonitoreoFrame = QtWidgets.QFrame(parent=self.visionPage)
        self.iniciarMonitoreoFrame.setGeometry(QtCore.QRect(1280, 290, 311, 591))
        self.iniciarMonitoreoFrame.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.iniciarMonitoreoFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.iniciarMonitoreoFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.iniciarMonitoreoFrame.setObjectName("iniciarMonitoreoFrame")
        self.estadisticasFrame = QtWidgets.QFrame(parent=self.iniciarMonitoreoFrame)
        self.estadisticasFrame.setGeometry(QtCore.QRect(10, 210, 311, 241))
        self.estadisticasFrame.setStyleSheet("background-color: rgb(153, 148, 137);")
        self.estadisticasFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.estadisticasFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.estadisticasFrame.setObjectName("estadisticasFrame")
        self.TaconesLabel = QtWidgets.QLabel(parent=self.estadisticasFrame)
        self.TaconesLabel.setGeometry(QtCore.QRect(80, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.TaconesLabel.setFont(font)
        self.TaconesLabel.setObjectName("TaconesLabel")
        self.TotalLabel = QtWidgets.QLabel(parent=self.estadisticasFrame)
        self.TotalLabel.setGeometry(QtCore.QRect(10, 50, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.TotalLabel.setFont(font)
        self.TotalLabel.setObjectName("TotalLabel")
        self.BuenosLabel = QtWidgets.QLabel(parent=self.estadisticasFrame)
        self.BuenosLabel.setGeometry(QtCore.QRect(10, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.BuenosLabel.setFont(font)
        self.BuenosLabel.setObjectName("BuenosLabel")
        self.MermaLabel = QtWidgets.QLabel(parent=self.estadisticasFrame)
        self.MermaLabel.setGeometry(QtCore.QRect(10, 170, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.MermaLabel.setFont(font)
        self.MermaLabel.setObjectName("MermaLabel")
        self.IniciarMonitoreo_Btn = QtWidgets.QPushButton(parent=self.iniciarMonitoreoFrame)
        self.IniciarMonitoreo_Btn.setGeometry(QtCore.QRect(10, 110, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.IniciarMonitoreo_Btn.setFont(font)
        self.IniciarMonitoreo_Btn.setStyleSheet("background-color: rgb(73, 195, 73);")
        self.IniciarMonitoreo_Btn.setObjectName("IniciarMonitoreo_Btn")
        self.RegistrarModeloBtn_3 = QtWidgets.QPushButton(parent=self.iniciarMonitoreoFrame)
        self.RegistrarModeloBtn_3.setGeometry(QtCore.QRect(10, 470, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.RegistrarModeloBtn_3.setFont(font)
        self.RegistrarModeloBtn_3.setStyleSheet("background-color: rgb(252, 67, 67);")
        self.RegistrarModeloBtn_3.setObjectName("RegistrarModeloBtn_3")
        self.IniciarIA_Btn = QtWidgets.QPushButton(parent=self.iniciarMonitoreoFrame)
        self.IniciarIA_Btn.setGeometry(QtCore.QRect(10, 20, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.IniciarIA_Btn.setFont(font)
        self.IniciarIA_Btn.setStyleSheet("background-color: rgb(73, 195, 73);")
        self.IniciarIA_Btn.setObjectName("IniciarIA_Btn")
        self.stackedWidget.addWidget(self.visionPage)
        self.datosPage = QtWidgets.QWidget()
        self.datosPage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.datosPage.setObjectName("datosPage")
        self.widget = QtWidgets.QWidget(parent=self.datosPage)
        self.widget.setGeometry(QtCore.QRect(390, 210, 481, 71))
        self.widget.setStyleSheet("background-color: rgb(176, 155, 101);")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 61, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.datosPage)
        self.estadisticasPage = QtWidgets.QWidget()
        self.estadisticasPage.setObjectName("estadisticasPage")
        self.widget_2 = QtWidgets.QWidget(parent=self.estadisticasPage)
        self.widget_2.setGeometry(QtCore.QRect(520, 300, 371, 101))
        self.widget_2.setStyleSheet("background-color: rgb(176, 155, 101);")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 101, 31))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.estadisticasPage)
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 170, 311, 291))
        self.frame_5.setStyleSheet("background-color: rgb(214, 198, 156);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame = QtWidgets.QFrame(parent=self.frame_5)
        self.frame.setGeometry(QtCore.QRect(0, 0, 311, 111))
        self.frame.setStyleSheet("background-color: rgb(153, 148, 137);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.inspeccionLabel = QtWidgets.QLabel(parent=self.frame)
        self.inspeccionLabel.setGeometry(QtCore.QRect(10, 0, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.inspeccionLabel.setFont(font)
        self.inspeccionLabel.setObjectName("inspeccionLabel")
        self.modeloLabel = QtWidgets.QLabel(parent=self.frame_5)
        self.modeloLabel.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.modeloLabel.setFont(font)
        self.modeloLabel.setObjectName("modeloLabel")
        self.puntoLabel = QtWidgets.QLabel(parent=self.frame_5)
        self.puntoLabel.setGeometry(QtCore.QRect(20, 190, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.puntoLabel.setFont(font)
        self.puntoLabel.setObjectName("puntoLabel")
        self.frame_12 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_12.setGeometry(QtCore.QRect(0, 860, 311, 101))
        self.frame_12.setStyleSheet("\n"
"background-color: rgb(214, 198, 156);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.Configuraciones_Btn = QtWidgets.QPushButton(parent=self.frame_12)
        self.Configuraciones_Btn.setGeometry(QtCore.QRect(0, 10, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Configuraciones_Btn.setFont(font)
        self.Configuraciones_Btn.setStyleSheet("background-color: rgb(229, 190, 88);")
        self.Configuraciones_Btn.setObjectName("Configuraciones_Btn")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 161, 151))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 120, 1211, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.botonesMainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.botonesMainLayout.setContentsMargins(0, 0, 0, 0)
        self.botonesMainLayout.setObjectName("botonesMainLayout")
        self.MostrarVision_Btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.MostrarVision_Btn.setObjectName("MostrarVision_Btn")
        self.botonesMainLayout.addWidget(self.MostrarVision_Btn)
        Tacoinador.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tacoinador)
        self.stackedWidget.setCurrentIndex(0)
        self.RegistrarParametrosBtn.clicked.connect(Tacoinador.showRegistrarParametros) # type: ignore
        self.RegistrarModeloBtn.clicked.connect(Tacoinador.showRegistrarModelo) # type: ignore
        self.MostrarVision_Btn.clicked.connect(Tacoinador.showVisionPage) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Tacoinador)

    def retranslateUi(self, Tacoinador):
        _translate = QtCore.QCoreApplication.translate
        Tacoinador.setWindowTitle(_translate("Tacoinador", "Principal"))
        self.tituloLabel.setText(_translate("Tacoinador", "Inspector de Tacones"))
        self.RegistrarParametrosBtn.setText(_translate("Tacoinador", "Registrar \n"
"Parametros"))
        self.inspeccionLabel_3.setText(_translate("Tacoinador", "<html><head/><body><p>Registrar<br/>Datos de Tacón</p></body></html>"))
        self.RegistrarModeloBtn.setText(_translate("Tacoinador", "Registrar \n"
"Modelo"))
        self.inspeccionLabel_2.setText(_translate("Tacoinador", "<html><head/><body><p>Seleccionar </p><p>Modelo de Tacón</p></body></html>"))
        self.label_4.setText(_translate("Tacoinador", "Modelo:"))
        self.label_5.setText(_translate("Tacoinador", "Punto:"))
        self.TaconesLabel.setText(_translate("Tacoinador", "Tacones"))
        self.TotalLabel.setText(_translate("Tacoinador", "Total:"))
        self.BuenosLabel.setText(_translate("Tacoinador", "Buenos:"))
        self.MermaLabel.setText(_translate("Tacoinador", "Merma:"))
        self.IniciarMonitoreo_Btn.setText(_translate("Tacoinador", "Iniciar \n"
"Monitoreo"))
        self.RegistrarModeloBtn_3.setText(_translate("Tacoinador", "Terminar \n"
"Monitoreo"))
        self.IniciarIA_Btn.setText(_translate("Tacoinador", "Iniciar \n"
"IA"))
        self.label_2.setText(_translate("Tacoinador", "datos page"))
        self.label_3.setText(_translate("Tacoinador", "estadisticas page"))
        self.inspeccionLabel.setText(_translate("Tacoinador", "<html><head/><body><p align=\"center\">Tacón en </p><p align=\"center\">Inspección</p></body></html>"))
        self.modeloLabel.setText(_translate("Tacoinador", "Modelo:"))
        self.puntoLabel.setText(_translate("Tacoinador", "Punto:"))
        self.Configuraciones_Btn.setText(_translate("Tacoinador", "Configuraciones"))
        self.label.setText(_translate("Tacoinador", "TextLabel"))
        self.MostrarVision_Btn.setText(_translate("Tacoinador", "Vision"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tacoinador = QtWidgets.QMainWindow()
    ui = Ui_Tacoinador()
    ui.setupUi(Tacoinador)
    Tacoinador.show()
    sys.exit(app.exec())
