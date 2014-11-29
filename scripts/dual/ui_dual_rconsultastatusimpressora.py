# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_rconsultastatusimpressora.ui'
#
# Created: Mon Nov 24 22:25:13 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_rconsultastatusimpressora(object):
    def setupUi(self, ui_dual_rconsultastatusimpressora):
        ui_dual_rconsultastatusimpressora.setObjectName("ui_dual_rconsultastatusimpressora")
        ui_dual_rconsultastatusimpressora.resize(263, 167)
        self.label = QtGui.QLabel(ui_dual_rconsultastatusimpressora)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_dual_rconsultastatusimpressora)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 211, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(ui_dual_rconsultastatusimpressora)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(ui_dual_rconsultastatusimpressora)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditIndice = QtGui.QLineEdit(ui_dual_rconsultastatusimpressora)
        self.lineEditIndice.setGeometry(QtCore.QRect(10, 30, 241, 20))
        self.lineEditIndice.setObjectName("lineEditIndice")
        self.lineEditTipo = QtGui.QLineEdit(ui_dual_rconsultastatusimpressora)
        self.lineEditTipo.setGeometry(QtCore.QRect(10, 100, 241, 20))
        self.lineEditTipo.setObjectName("lineEditTipo")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_rconsultastatusimpressora)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(190, 130, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_rconsultastatusimpressora)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(120, 130, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")

        self.retranslateUi(ui_dual_rconsultastatusimpressora)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_rconsultastatusimpressora)

    def retranslateUi(self, ui_dual_rconsultastatusimpressora):
        ui_dual_rconsultastatusimpressora.setWindowTitle(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "Método rConsultaStatus_DUAL_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "Entre com o índice desejado: (1-8)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "Entre com o tipo da informaçao desejada:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "1 - para receber texto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "0 - para receber valores", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

