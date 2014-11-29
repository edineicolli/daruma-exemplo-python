# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_menufiscal.ui'
#
# Created: Mon Nov 24 22:26:10 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_MenuFiscal(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_MenuFiscal, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_MenuFiscal):
        ui_FISCAL_MenuFiscal.setObjectName("ui_FISCAL_MenuFiscal")
        ui_FISCAL_MenuFiscal.resize(511, 251)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_MenuFiscal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtGui.QTextEdit(ui_FISCAL_MenuFiscal)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtGui.QPushButton(ui_FISCAL_MenuFiscal)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(ui_FISCAL_MenuFiscal)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_MenuFiscal)

    def retranslateUi(self, ui_FISCAL_MenuFiscal):
        ui_FISCAL_MenuFiscal.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal", "MENU FISCAL", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Olá, desenvolvedor!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Este item do Menu Fiscal deve ser gerado pelo seu aplicativo, obtendo as informações cadastradas em seu Banco de Dados.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Para maiores informaçoes, acesse o site http://www.desenvolvedoresdaruma.com.br e procure por PAF-ECF</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Ligação Gratuita: 0800 770 3320</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

