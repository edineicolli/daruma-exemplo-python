# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rassinarrsa.ui'
#
# Created: Mon Nov 24 22:26:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rAssinarRSA(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_ui_FISCAL_rAssinarRSA, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_rAssinarRSA):
        ui_FISCAL_rAssinarRSA.setObjectName("ui_FISCAL_rAssinarRSA")
        ui_FISCAL_rAssinarRSA.resize(338, 262)
        self.gridLayout = QtGui.QGridLayout(ui_FISCAL_rAssinarRSA)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rAssinarRSA)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditCaminhoArq = QtGui.QLineEdit(ui_FISCAL_rAssinarRSA)
        self.lineEditCaminhoArq.setObjectName("lineEditCaminhoArq")
        self.gridLayout.addWidget(self.lineEditCaminhoArq, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_rAssinarRSA)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEditCaminhoKey = QtGui.QLineEdit(ui_FISCAL_rAssinarRSA)
        self.lineEditCaminhoKey.setObjectName("lineEditCaminhoKey")
        self.gridLayout.addWidget(self.lineEditCaminhoKey, 3, 0, 1, 1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rAssinarRSA)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.gridLayout.addWidget(self.pushButtonEnviar, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(ui_FISCAL_rAssinarRSA)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.textEditAssinaturaRSA = QtGui.QTextEdit(ui_FISCAL_rAssinarRSA)
        self.textEditAssinaturaRSA.setObjectName("textEditAssinaturaRSA")
        self.gridLayout.addWidget(self.textEditAssinaturaRSA, 7, 0, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rAssinarRSA)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.gridLayout.addWidget(self.pushButtonCancelar, 8, 0, 1, 1)

        self.retranslateUi(ui_FISCAL_rAssinarRSA)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rAssinarRSA)

    def retranslateUi(self, ui_FISCAL_rAssinarRSA):
        ui_FISCAL_rAssinarRSA.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "Caminho Completo do Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminhoArq.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "C:\\Daruma.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "Caminho Completo da Chave .key", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminhoKey.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "C:\\Chave.Key", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "Gerar Assinatura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "Retorno da Assinatura Gerada:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rAssinarRSA", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

