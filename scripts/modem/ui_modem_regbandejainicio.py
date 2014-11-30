# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_regbandejainicio.ui'
#
# Created: Mon Nov 24 22:26:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_regBandejaInicio(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_regBandejaInicio, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_fechar_clicked)

    def on_Enviar_clicked(self):
       pass

    def on_fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_regBandejaInicio):
        ui_MODEM_regBandejaInicio.setObjectName("ui_MODEM_regBandejaInicio")
        ui_MODEM_regBandejaInicio.resize(212, 109)
        self.label = QtGui.QLabel(ui_MODEM_regBandejaInicio)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.label.setObjectName("label")
        self.lineEditBandejaInicio = QtGui.QLineEdit(ui_MODEM_regBandejaInicio)
        self.lineEditBandejaInicio.setGeometry(QtCore.QRect(20, 40, 171, 20))
        self.lineEditBandejaInicio.setObjectName("lineEditBandejaInicio")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_regBandejaInicio)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_regBandejaInicio)
        self.pushButtonFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_regBandejaInicio)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_regBandejaInicio)

    def retranslateUi(self, ui_MODEM_regBandejaInicio):
        ui_MODEM_regBandejaInicio.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_regBandejaInicio", "Método regBandejaInicio_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_regBandejaInicio", "Bandeja Inicial (SIM1 ou SIM2):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_regBandejaInicio", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_regBandejaInicio", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

