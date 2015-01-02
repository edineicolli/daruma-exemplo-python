# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_ienviarbmp.ui'
#
# Created: Mon Nov 24 22:25:09 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iEnviarBMP_DUAL_DarumaFramework
from scripts.dual.retornodual import tratarRetornoDUAL


class Ui_ui_dual_ienviarbmp(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_ienviarbmp, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.lineEditPath.setText("C:\\logo.bmp")
        
    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrPath = self.lineEditPath.text()
    
        # Chamada do Método
        tratarRetornoDUAL(iEnviarBMP_DUAL_DarumaFramework(StrPath), self)
    
    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_dual_ienviarbmp):
        ui_dual_ienviarbmp.setObjectName("ui_dual_ienviarbmp")
        ui_dual_ienviarbmp.resize(280, 100)
        self.label = QtGui.QLabel(ui_dual_ienviarbmp)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 21))
        self.label.setObjectName("label")
        self.lineEditPath = QtGui.QLineEdit(ui_dual_ienviarbmp)
        self.lineEditPath.setGeometry(QtCore.QRect(10, 30, 261, 20))
        self.lineEditPath.setObjectName("lineEditPath")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_ienviarbmp)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(150, 60, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_ienviarbmp)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(80, 60, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")

        self.retranslateUi(ui_dual_ienviarbmp)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_ienviarbmp)

    def retranslateUi(self, ui_dual_ienviarbmp):
        ui_dual_ienviarbmp.setWindowTitle(QtGui.QApplication.translate("ui_dual_ienviarbmp", "Método iEnviarBMP_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_ienviarbmp", "Entre com o nome do logotipo a ser enviado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPath.setText(QtGui.QApplication.translate("ui_dual_ienviarbmp", "C:\\\\logo.bmp", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_ienviarbmp", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_ienviarbmp", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

