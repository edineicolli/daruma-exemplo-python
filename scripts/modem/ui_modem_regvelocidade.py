# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_regvelocidade.ui'
#
# Created: Mon Nov 24 22:26:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_regVelocidade(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_regVelocidade, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_regVelocidade):
        ui_MODEM_regVelocidade.setObjectName("ui_MODEM_regVelocidade")
        ui_MODEM_regVelocidade.resize(213, 116)
        self.label = QtGui.QLabel(ui_MODEM_regVelocidade)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.lineEditVelocidade = QtGui.QLineEdit(ui_MODEM_regVelocidade)
        self.lineEditVelocidade.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.lineEditVelocidade.setObjectName("lineEditVelocidade")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_regVelocidade)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_regVelocidade)
        self.pushButtonFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_regVelocidade)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_regVelocidade)

    def retranslateUi(self, ui_MODEM_regVelocidade):
        ui_MODEM_regVelocidade.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_regVelocidade", "Método regVelocidade_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_regVelocidade", "Velocidade desejada:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_regVelocidade", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_regVelocidade", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

