# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfcancelaritem.ui'
#
# Created: Mon Nov 24 22:25:56 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import iCNFCancelarItem_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCNFCancelarItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFCancelarItem, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrNumItem =  self.lineEditNumeroItem.text()

        if(StrNumItem ==""):
            QMessageBox.information(self,"DarumaFramework - Python/Qt","Preencha todos os Campos")
        else:
            # Chamada do Método
            tratarRetornoFiscal(iCNFCancelarItem_ECF_Daruma(StrNumItem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCNFCancelarItem):
        ui_FISCAL_iCNFCancelarItem.setObjectName("ui_FISCAL_iCNFCancelarItem")
        ui_FISCAL_iCNFCancelarItem.resize(194, 104)
        ui_FISCAL_iCNFCancelarItem.setMinimumSize(QtCore.QSize(194, 104))
        ui_FISCAL_iCNFCancelarItem.setMaximumSize(QtCore.QSize(194, 104))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iCNFCancelarItem)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCNFCancelarItem)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEditNumeroItem = QtGui.QLineEdit(ui_FISCAL_iCNFCancelarItem)
        self.lineEditNumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditNumeroItem.setMaxLength(3)
        self.lineEditNumeroItem.setObjectName("lineEditNumeroItem")
        self.horizontalLayout_2.addWidget(self.lineEditNumeroItem)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCNFCancelarItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCNFCancelarItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFCancelarItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFCancelarItem)

    def retranslateUi(self, ui_FISCAL_iCNFCancelarItem):
        ui_FISCAL_iCNFCancelarItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFCancelarItem", "Método iCNFCancelarItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFCancelarItem", "Número do Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFCancelarItem", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFCancelarItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFCancelarItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

