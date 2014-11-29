# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_rretornarimei.ui'
#
# Created: Mon Nov 24 22:26:50 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_rRetornarIMEI(object):
    def setupUi(self, ui_MODEM_rRetornarIMEI):
        ui_MODEM_rRetornarIMEI.setObjectName("ui_MODEM_rRetornarIMEI")
        ui_MODEM_rRetornarIMEI.resize(213, 123)
        self.lineEditIMEI = QtGui.QLineEdit(ui_MODEM_rRetornarIMEI)
        self.lineEditIMEI.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.lineEditIMEI.setObjectName("lineEditIMEI")
        self.label = QtGui.QLabel(ui_MODEM_rRetornarIMEI)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_rRetornarIMEI)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_rRetornarIMEI)
        self.pushButtonFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_rRetornarIMEI)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_rRetornarIMEI)

    def retranslateUi(self, ui_MODEM_rRetornarIMEI):
        ui_MODEM_rRetornarIMEI.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_rRetornarIMEI", "Método rRetornarIMEI_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_rRetornarIMEI", "IMEI Retornado:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_rRetornarIMEI", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_rRetornarIMEI", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

