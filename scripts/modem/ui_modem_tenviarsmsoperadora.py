# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_tenviarsmsoperadora.ui'
#
# Created: Mon Nov 24 22:26:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import tEnviarSmsOperadora_MODEM_DarumaFramework
from scripts.modem.retornomodem import tratarRetornoModem


class Ui_ui_MODEM_tEnviarSmsOperadora(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_tEnviarSmsOperadora, self).__init__()

        self.setupUi(self)
        self.pushButtonLimpar.clicked.connect(self.on_Limpar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Limpar_clicked(self):
        self.lineEditNumeroTelefone.setText('')
        self.lineEditBandeja.setText('')
        self.textEditMensagemTexto.setText('')

    def on_Enviar_clicked(self):
        StrNumeroTelefone = self.lineEditNumeroTelefone.text()
        StrBandeja = self.lineEditBandeja.text()
        StrMensagemTexto = self.textEditMensagemTexto.toPlainText()
        tratarRetornoModem(tEnviarSmsOperadora_MODEM_DarumaFramework(StrNumeroTelefone, StrBandeja, StrMensagemTexto), self)

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_tEnviarSmsOperadora):
        ui_MODEM_tEnviarSmsOperadora.setObjectName("ui_MODEM_tEnviarSmsOperadora")
        ui_MODEM_tEnviarSmsOperadora.resize(284, 292)
        self.label = QtGui.QLabel(ui_MODEM_tEnviarSmsOperadora)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_MODEM_tEnviarSmsOperadora)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(ui_MODEM_tEnviarSmsOperadora)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditNumeroTelefone = QtGui.QLineEdit(ui_MODEM_tEnviarSmsOperadora)
        self.lineEditNumeroTelefone.setGeometry(QtCore.QRect(20, 40, 171, 20))
        self.lineEditNumeroTelefone.setObjectName("lineEditNumeroTelefone")
        self.lineEditBandeja = QtGui.QLineEdit(ui_MODEM_tEnviarSmsOperadora)
        self.lineEditBandeja.setGeometry(QtCore.QRect(20, 90, 171, 20))
        self.lineEditBandeja.setObjectName("lineEditBandeja")
        self.textEditMensagemTexto = QtGui.QTextEdit(ui_MODEM_tEnviarSmsOperadora)
        self.textEditMensagemTexto.setGeometry(QtCore.QRect(20, 140, 171, 91))
        self.textEditMensagemTexto.setObjectName("textEditMensagemTexto")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_tEnviarSmsOperadora)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_tEnviarSmsOperadora)
        self.pushButtonFechar.setGeometry(QtCore.QRect(100, 240, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.pushButtonLimpar = QtGui.QPushButton(ui_MODEM_tEnviarSmsOperadora)
        self.pushButtonLimpar.setGeometry(QtCore.QRect(180, 240, 75, 23))
        self.pushButtonLimpar.setObjectName("pushButtonLimpar")

        self.retranslateUi(ui_MODEM_tEnviarSmsOperadora)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_tEnviarSmsOperadora)

    def retranslateUi(self, ui_MODEM_tEnviarSmsOperadora):
        ui_MODEM_tEnviarSmsOperadora.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Método tEnviarSmsOperadora_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Numero do Telefone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Bendeja (SIM1 ou SIM2):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Mensagem de Texto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroTelefone.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "0xxTelefone", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditBandeja.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "SIM1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLimpar.setText(QtGui.QApplication.translate("ui_MODEM_tEnviarSmsOperadora", "Limpar", None, QtGui.QApplication.UnicodeUTF8))

