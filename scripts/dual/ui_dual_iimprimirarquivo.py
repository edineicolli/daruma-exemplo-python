# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_iimprimirarquivo.ui'
#
# Created: Mon Nov 24 22:25:10 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_iimprimirarquivo(object):
    def setupUi(self, ui_dual_iimprimirarquivo):
        ui_dual_iimprimirarquivo.setObjectName("ui_dual_iimprimirarquivo")
        ui_dual_iimprimirarquivo.resize(271, 108)
        self.lineEditPath = QtGui.QLineEdit(ui_dual_iimprimirarquivo)
        self.lineEditPath.setGeometry(QtCore.QRect(10, 30, 251, 20))
        self.lineEditPath.setObjectName("lineEditPath")
        self.label = QtGui.QLabel(ui_dual_iimprimirarquivo)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.label.setObjectName("label")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_iimprimirarquivo)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(70, 70, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_iimprimirarquivo)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(140, 70, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")

        self.retranslateUi(ui_dual_iimprimirarquivo)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_iimprimirarquivo)

    def retranslateUi(self, ui_dual_iimprimirarquivo):
        ui_dual_iimprimirarquivo.setWindowTitle(QtGui.QApplication.translate("ui_dual_iimprimirarquivo", "Método iImprimirArquivo_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPath.setText(QtGui.QApplication.translate("ui_dual_iimprimirarquivo", "C:\\\\DarumaDLLFramework.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_iimprimirarquivo", "Entre com o nome do arquivo a ser impresso:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_iimprimirarquivo", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_iimprimirarquivo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

