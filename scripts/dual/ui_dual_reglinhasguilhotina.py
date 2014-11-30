# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_reglinhasguilhotina.ui'
#
# Created: Mon Nov 24 22:25:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_reglinhasguilhotina(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_reglinhasguilhotina, self).__init__()

        self.setupUi(self)
        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):
        pass

    def setupUi(self, ui_dual_reglinhasguilhotina):
        ui_dual_reglinhasguilhotina.setObjectName("ui_dual_reglinhasguilhotina")
        ui_dual_reglinhasguilhotina.resize(279, 96)
        self.lineEditValor = QtGui.QLineEdit(ui_dual_reglinhasguilhotina)
        self.lineEditValor.setGeometry(QtCore.QRect(10, 30, 261, 20))
        self.lineEditValor.setObjectName("lineEditValor")
        self.label = QtGui.QLabel(ui_dual_reglinhasguilhotina)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.label.setObjectName("label")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_reglinhasguilhotina)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(140, 60, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_reglinhasguilhotina)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(210, 60, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")

        self.retranslateUi(ui_dual_reglinhasguilhotina)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_reglinhasguilhotina)

    def retranslateUi(self, ui_dual_reglinhasguilhotina):
        ui_dual_reglinhasguilhotina.setWindowTitle(QtGui.QApplication.translate("ui_dual_reglinhasguilhotina", "Método regLinhasGuilhotina_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_reglinhasguilhotina", "Número de linhas para habilitar a guilhotina (0 a 20):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_reglinhasguilhotina", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_reglinhasguilhotina", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

