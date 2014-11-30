# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_rretornaroperadora.ui'
#
# Created: Mon Nov 24 22:26:51 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_rRetornarOperadora(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_rRetornarOperadora, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_rRetornarOperadora):
        ui_MODEM_rRetornarOperadora.setObjectName("ui_MODEM_rRetornarOperadora")
        ui_MODEM_rRetornarOperadora.resize(209, 116)
        self.label = QtGui.QLabel(ui_MODEM_rRetornarOperadora)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label.setObjectName("label")
        self.lineEditOperadora = QtGui.QLineEdit(ui_MODEM_rRetornarOperadora)
        self.lineEditOperadora.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.lineEditOperadora.setObjectName("lineEditOperadora")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_rRetornarOperadora)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_rRetornarOperadora)
        self.pushButtonFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_rRetornarOperadora)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_rRetornarOperadora)

    def retranslateUi(self, ui_MODEM_rRetornarOperadora):
        ui_MODEM_rRetornarOperadora.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_rRetornarOperadora", "Método rRetornarOperadora_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_rRetornarOperadora", "Operadora Retornada:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_rRetornarOperadora", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_rRetornarOperadora", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

