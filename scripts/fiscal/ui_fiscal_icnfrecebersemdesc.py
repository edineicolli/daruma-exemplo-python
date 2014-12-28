# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfrecebersemdesc.ui'
#
# Created: Mon Nov 24 22:26:00 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import iCNFReceberSemDesc_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCNFReceberSemDesc(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFReceberSemDesc, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrIndice =  self.comboBoxIndiceTotalizador.currentText()
        StrValorRecebimento = self.lineEditValorRecebimento.text()

        if((StrIndice == "Selecione...") and (StrValorRecebimento == "")):
            QMessageBox.information(self,"DarumaFramework - Python/Qt","Preencha todos os Campos")
        else:
            # Chamada do Método
            tratarRetornoFiscal(iCNFReceberSemDesc_ECF_Daruma(StrIndice,StrValorRecebimento), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCNFReceberSemDesc):
        ui_FISCAL_iCNFReceberSemDesc.setObjectName("ui_FISCAL_iCNFReceberSemDesc")
        ui_FISCAL_iCNFReceberSemDesc.resize(211, 97)
        ui_FISCAL_iCNFReceberSemDesc.setMinimumSize(QtCore.QSize(211, 97))
        ui_FISCAL_iCNFReceberSemDesc.setMaximumSize(QtCore.QSize(211, 97))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCNFReceberSemDesc)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCNFReceberSemDesc)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxIndiceTotalizador = QtGui.QComboBox(ui_FISCAL_iCNFReceberSemDesc)
        self.comboBoxIndiceTotalizador.setObjectName("comboBoxIndiceTotalizador")
        self.comboBoxIndiceTotalizador.addItem("")
        self.comboBoxIndiceTotalizador.addItem("")
        self.comboBoxIndiceTotalizador.addItem("")
        self.comboBoxIndiceTotalizador.addItem("")
        self.gridLayout.addWidget(self.comboBoxIndiceTotalizador, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCNFReceberSemDesc)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditValorRecebimento = QtGui.QLineEdit(ui_FISCAL_iCNFReceberSemDesc)
        self.lineEditValorRecebimento.setObjectName("lineEditValorRecebimento")
        self.gridLayout.addWidget(self.lineEditValorRecebimento, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCNFReceberSemDesc)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCNFReceberSemDesc)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFReceberSemDesc)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFReceberSemDesc)

    def retranslateUi(self, ui_FISCAL_iCNFReceberSemDesc):
        ui_FISCAL_iCNFReceberSemDesc.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "Método iCNFReceberSemDesc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "Indice do Totalizador:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "03", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "04", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "05", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceberSemDesc", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

