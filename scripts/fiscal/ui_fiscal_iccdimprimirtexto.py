# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iccdimprimirtexto.ui'
#
# Created: Mon Nov 24 22:25:35 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCCDImprimirTexto_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCCDImprimirTexto(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCCDImprimirTexto, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrMensagem = self.textEditTextoImpressao.toPlainText()
        tratarRetornoFiscal(iCCDImprimirTexto_ECF_Daruma(StrMensagem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCCDImprimirTexto):
        ui_FISCAL_iCCDImprimirTexto.setObjectName("ui_FISCAL_iCCDImprimirTexto")
        ui_FISCAL_iCCDImprimirTexto.resize(266, 226)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iCCDImprimirTexto)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCCDImprimirTexto)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEditTextoImpressao = QtGui.QTextEdit(ui_FISCAL_iCCDImprimirTexto)
        self.textEditTextoImpressao.setObjectName("textEditTextoImpressao")
        self.verticalLayout.addWidget(self.textEditTextoImpressao)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCCDImprimirTexto)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCCDImprimirTexto)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCCDImprimirTexto)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCCDImprimirTexto)

    def retranslateUi(self, ui_FISCAL_iCCDImprimirTexto):
        ui_FISCAL_iCCDImprimirTexto.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirTexto", "Método iCCDImprimirTexto_ECF_Daruma ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirTexto", "Texto para Impressão:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditTextoImpressao.setHtml(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirTexto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Impressão de Texto em Comprovante de CCD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Impressão de Texto em Comprovante de CCD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Impressão de Texto em Comprovante de CCD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Impressão de Texto em Comprovante de CCD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Impressão de Texto em Comprovante de CCD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Impressão de Texto em Comprovante de CCD</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirTexto", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirTexto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

