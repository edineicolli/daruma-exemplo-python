# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_tenviarsms.ui'
#
# Created: Mon Nov 24 22:26:51 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_modem_tenviarsms(object):
    def setupUi(self, ui_modem_tenviarsms):
        ui_modem_tenviarsms.setObjectName("ui_modem_tenviarsms")
        ui_modem_tenviarsms.resize(280, 282)
        self.lineEditNumeroTelefone = QtGui.QLineEdit(ui_modem_tenviarsms)
        self.lineEditNumeroTelefone.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.lineEditNumeroTelefone.setObjectName("lineEditNumeroTelefone")
        self.label = QtGui.QLabel(ui_modem_tenviarsms)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_modem_tenviarsms)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        self.textEditMensagemTexto = QtGui.QTextEdit(ui_modem_tenviarsms)
        self.textEditMensagemTexto.setGeometry(QtCore.QRect(20, 90, 161, 121))
        self.textEditMensagemTexto.setObjectName("textEditMensagemTexto")
        self.pushButtonEnviar = QtGui.QPushButton(ui_modem_tenviarsms)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_modem_tenviarsms)
        self.pushButtonFechar.setGeometry(QtCore.QRect(100, 230, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.pushButtonLimpar = QtGui.QPushButton(ui_modem_tenviarsms)
        self.pushButtonLimpar.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.pushButtonLimpar.setObjectName("pushButtonLimpar")

        self.retranslateUi(ui_modem_tenviarsms)
        QtCore.QMetaObject.connectSlotsByName(ui_modem_tenviarsms)

    def retranslateUi(self, ui_modem_tenviarsms):
        ui_modem_tenviarsms.setWindowTitle(QtGui.QApplication.translate("ui_modem_tenviarsms", "Método tEnviarSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroTelefone.setText(QtGui.QApplication.translate("ui_modem_tenviarsms", "0xxTelefone", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_modem_tenviarsms", "Numero do Telefone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_modem_tenviarsms", "Mensagem:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditMensagemTexto.setHtml(QtGui.QApplication.translate("ui_modem_tenviarsms", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Teste Mensagem Modem Daruma.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_modem_tenviarsms", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_modem_tenviarsms", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLimpar.setText(QtGui.QApplication.translate("ui_modem_tenviarsms", "Limpar", None, QtGui.QApplication.UnicodeUTF8))

