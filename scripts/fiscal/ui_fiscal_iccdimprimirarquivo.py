# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iccdimprimirarquivo.ui'
#
# Created: Mon Nov 24 22:25:34 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCCDImprimirArquivo_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCCDImprimirArquivo(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCCDImprimirArquivo, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrCaminho =  self.lineEditCaminho.text()
        tratarRetornoFiscal(iCCDImprimirArquivo_ECF_Daruma(StrCaminho), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCCDImprimirArquivo):
        ui_FISCAL_iCCDImprimirArquivo.setObjectName("ui_FISCAL_iCCDImprimirArquivo")
        ui_FISCAL_iCCDImprimirArquivo.resize(271, 94)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCCDImprimirArquivo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCCDImprimirArquivo)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditCaminho = QtGui.QLineEdit(ui_FISCAL_iCCDImprimirArquivo)
        self.lineEditCaminho.setObjectName("lineEditCaminho")
        self.verticalLayout.addWidget(self.lineEditCaminho)
        spacerItem = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCCDImprimirArquivo)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCCDImprimirArquivo)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCCDImprimirArquivo)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCCDImprimirArquivo)

    def retranslateUi(self, ui_FISCAL_iCCDImprimirArquivo):
        ui_FISCAL_iCCDImprimirArquivo.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirArquivo", "Método iCCDImprimirArquivo_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirArquivo", "Caminho do Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminho.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirArquivo", "C:\\DARUMA.TXT", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirArquivo", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDImprimirArquivo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

