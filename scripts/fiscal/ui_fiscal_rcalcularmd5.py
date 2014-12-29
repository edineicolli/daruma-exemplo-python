# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rcalcularmd5.ui'
#
# Created: Mon Nov 24 22:26:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
from ctypes import create_string_buffer

from PySide import QtCore, QtGui
from pydaruma.pydaruma import rCalcularMD5_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_rCalcularMD5(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rCalcularMD5, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):

        cMD5Hexa = create_string_buffer(1000)
        cMD5Ascii = create_string_buffer(1000)

        StrCaminhoArq = self.lineEditCaminhoArq.text()

        tratarRetornoFiscal(rCalcularMD5_ECF_Daruma(StrCaminhoArq,cMD5Hexa,cMD5Ascii), self)

        StrMD5Hexa = cMD5Hexa
        StrMD5Ascii = cMD5Ascii

        self.textEditMD5Hexa.setText(StrMD5Hexa)
        self.textEditMD5Ascii.setText(StrMD5Ascii)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rCalcularMD5):
        ui_FISCAL_rCalcularMD5.setObjectName("ui_FISCAL_rCalcularMD5")
        ui_FISCAL_rCalcularMD5.resize(308, 307)
        self.gridLayout = QtGui.QGridLayout(ui_FISCAL_rCalcularMD5)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rCalcularMD5)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEditCaminhoArq = QtGui.QLineEdit(ui_FISCAL_rCalcularMD5)
        self.lineEditCaminhoArq.setObjectName("lineEditCaminhoArq")
        self.gridLayout.addWidget(self.lineEditCaminhoArq, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rCalcularMD5)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.gridLayout.addWidget(self.pushButtonEnviar, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_rCalcularMD5)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.textEditMD5Hexa = QtGui.QTextEdit(ui_FISCAL_rCalcularMD5)
        self.textEditMD5Hexa.setObjectName("textEditMD5Hexa")
        self.gridLayout.addWidget(self.textEditMD5Hexa, 4, 0, 1, 3)
        self.label_3 = QtGui.QLabel(ui_FISCAL_rCalcularMD5)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.textEditMD5Ascii = QtGui.QTextEdit(ui_FISCAL_rCalcularMD5)
        self.textEditMD5Ascii.setObjectName("textEditMD5Ascii")
        self.gridLayout.addWidget(self.textEditMD5Ascii, 6, 0, 1, 3)
        self.pushButtonFechar = QtGui.QPushButton(ui_FISCAL_rCalcularMD5)
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.gridLayout.addWidget(self.pushButtonFechar, 7, 2, 1, 1)

        self.retranslateUi(ui_FISCAL_rCalcularMD5)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rCalcularMD5)

    def retranslateUi(self, ui_FISCAL_rCalcularMD5):
        ui_FISCAL_rCalcularMD5.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "Método rCalcularMD5_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "Caminho do Arquivo com Nome e Extensão:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminhoArq.setText(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "C:\\Daruma.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "Gerar MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "MD5 Gerado - Hexadecimal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "MD5 Gerado - ASCII", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_FISCAL_rCalcularMD5", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

