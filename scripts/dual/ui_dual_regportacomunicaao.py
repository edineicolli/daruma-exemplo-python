# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_regportacomunicaao.ui'
#
# Created: Mon Nov 24 22:25:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_regportacomunicacao(object):
    def setupUi(self, ui_dual_regportacomunicacao):
        ui_dual_regportacomunicacao.setObjectName("ui_dual_regportacomunicacao")
        ui_dual_regportacomunicacao.resize(193, 101)
        self.label = QtGui.QLabel(ui_dual_regportacomunicacao)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        self.lineEditValor = QtGui.QLineEdit(ui_dual_regportacomunicacao)
        self.lineEditValor.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.lineEditValor.setObjectName("lineEditValor")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_regportacomunicacao)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(50, 60, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_regportacomunicacao)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(120, 60, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")

        self.retranslateUi(ui_dual_regportacomunicacao)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_regportacomunicacao)

    def retranslateUi(self, ui_dual_regportacomunicacao):
        ui_dual_regportacomunicacao.setWindowTitle(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Método regPortaComunicacao_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Digite a Porta de Comunicaçao:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

