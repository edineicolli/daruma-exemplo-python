# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_regporta.ui'
#
# Created: Mon Nov 24 22:26:45 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_regPorta(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_regPorta, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_regPorta):
        ui_MODEM_regPorta.setObjectName("ui_MODEM_regPorta")
        ui_MODEM_regPorta.resize(212, 120)
        self.label = QtGui.QLabel(ui_MODEM_regPorta)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.lineEditPortaCOM = QtGui.QLineEdit(ui_MODEM_regPorta)
        self.lineEditPortaCOM.setGeometry(QtCore.QRect(20, 40, 171, 20))
        self.lineEditPortaCOM.setObjectName("lineEditPortaCOM")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_regPorta)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_regPorta)
        self.pushButtonFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_regPorta)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_regPorta)

    def retranslateUi(self, ui_MODEM_regPorta):
        ui_MODEM_regPorta.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_regPorta", "Método regPorta_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_regPorta", "Porta COM:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_regPorta", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_regPorta", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

