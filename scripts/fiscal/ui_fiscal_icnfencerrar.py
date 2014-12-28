# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfencerrar.ui'
#
# Created: Mon Nov 24 22:25:58 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCNFEncerrar_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCNFEncerrar(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFEncerrar, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Pega o texto do TextEdit
        StrMensagem = self.textEditMensagem.toPlainText()
        tratarRetornoFiscal(iCNFEncerrar_ECF_Daruma(StrMensagem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCNFEncerrar):
        ui_FISCAL_iCNFEncerrar.setObjectName("ui_FISCAL_iCNFEncerrar")
        ui_FISCAL_iCNFEncerrar.resize(309, 167)
        ui_FISCAL_iCNFEncerrar.setMinimumSize(QtCore.QSize(309, 167))
        ui_FISCAL_iCNFEncerrar.setMaximumSize(QtCore.QSize(309, 167))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCNFEncerrar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCNFEncerrar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEditMensagem = QtGui.QTextEdit(ui_FISCAL_iCNFEncerrar)
        self.textEditMensagem.setMinimumSize(QtCore.QSize(291, 91))
        self.textEditMensagem.setMaximumSize(QtCore.QSize(291, 91))
        self.textEditMensagem.setObjectName("textEditMensagem")
        self.verticalLayout.addWidget(self.textEditMensagem)
        spacerItem = QtGui.QSpacerItem(17, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCNFEncerrar)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCNFEncerrar)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFEncerrar)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFEncerrar)

    def retranslateUi(self, ui_FISCAL_iCNFEncerrar):
        ui_FISCAL_iCNFEncerrar.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFEncerrar", "Método iCNFEncerrar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEncerrar", "Mensagem Promocional:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditMensagem.setHtml(QtGui.QApplication.translate("ui_FISCAL_iCNFEncerrar", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">DarumaFramework com Mensagem no Encerramento com </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">até 8 linhas!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEncerrar", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEncerrar", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

