# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_regtempoalertar.ui'
#
# Created: Mon Nov 24 22:26:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_regTempoAlertar(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_regTempoAlertar, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_regTempoAlertar):
        ui_MODEM_regTempoAlertar.setObjectName("ui_MODEM_regTempoAlertar")
        ui_MODEM_regTempoAlertar.resize(226, 119)
        self.label = QtGui.QLabel(ui_MODEM_regTempoAlertar)
        self.label.setGeometry(QtCore.QRect(20, 20, 191, 16))
        self.label.setObjectName("label")
        self.lineEditTempoAlertar = QtGui.QLineEdit(ui_MODEM_regTempoAlertar)
        self.lineEditTempoAlertar.setGeometry(QtCore.QRect(20, 40, 171, 20))
        self.lineEditTempoAlertar.setObjectName("lineEditTempoAlertar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_regTempoAlertar)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_regTempoAlertar)
        self.pushButtonFechar.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_regTempoAlertar)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_regTempoAlertar)

    def retranslateUi(self, ui_MODEM_regTempoAlertar):
        ui_MODEM_regTempoAlertar.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_regTempoAlertar", "Método regTempoAlertar_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_regTempoAlertar", "Tempo Thread(Milisegundos):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_regTempoAlertar", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_regTempoAlertar", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

