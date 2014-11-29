# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_generico_eabrirserial.ui'
#
# Created: Mon Nov 24 22:26:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_GENERICO_eAbrirSerial(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_GENERICO_eAbrirSerial, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_GENERICO_eAbrirSerial):
        ui_GENERICO_eAbrirSerial.setObjectName("ui_GENERICO_eAbrirSerial")
        ui_GENERICO_eAbrirSerial.resize(181, 160)
        ui_GENERICO_eAbrirSerial.setMinimumSize(QtCore.QSize(181, 160))
        ui_GENERICO_eAbrirSerial.setMaximumSize(QtCore.QSize(181, 160))
        self.verticalLayout = QtGui.QVBoxLayout(ui_GENERICO_eAbrirSerial)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_GENERICO_eAbrirSerial)
        self.label.setMaximumSize(QtCore.QSize(163, 13))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditPorta = QtGui.QLineEdit(ui_GENERICO_eAbrirSerial)
        self.lineEditPorta.setObjectName("lineEditPorta")
        self.verticalLayout.addWidget(self.lineEditPorta)
        self.label_2 = QtGui.QLabel(ui_GENERICO_eAbrirSerial)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditVelocidade = QtGui.QLineEdit(ui_GENERICO_eAbrirSerial)
        self.lineEditVelocidade.setObjectName("lineEditVelocidade")
        self.verticalLayout.addWidget(self.lineEditVelocidade)
        self.pushButtonEnviar = QtGui.QPushButton(ui_GENERICO_eAbrirSerial)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.verticalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(ui_GENERICO_eAbrirSerial)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.verticalLayout.addWidget(self.pushButtonCancelar)

        self.retranslateUi(ui_GENERICO_eAbrirSerial)
        QtCore.QMetaObject.connectSlotsByName(ui_GENERICO_eAbrirSerial)

    def retranslateUi(self, ui_GENERICO_eAbrirSerial):
        ui_GENERICO_eAbrirSerial.setWindowTitle(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "Método eAbrirSerial_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "Porta Serial:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPorta.setText(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "COM1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "Velocidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditVelocidade.setText(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_GENERICO_eAbrirSerial", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

