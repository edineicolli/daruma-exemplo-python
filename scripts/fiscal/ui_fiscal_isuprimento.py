# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_isuprimento.ui'
#
# Created: Mon Nov 24 22:26:08 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iSuprimento_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iSuprimento(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iSuprimento, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrValor =  self.lineEditValor.text()
        StrMensagem = self.lineEditMensagem.text()

        # Chamada do Método
        tratarRetornoFiscal(iSuprimento_ECF_Daruma(StrValor,StrMensagem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iSuprimento):
        ui_FISCAL_iSuprimento.setObjectName("ui_FISCAL_iSuprimento")
        ui_FISCAL_iSuprimento.resize(241, 105)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iSuprimento)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelValor = QtGui.QLabel(ui_FISCAL_iSuprimento)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 0, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iSuprimento)
        self.lineEditValor.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 0, 1, 1, 1)
        self.labelMensagem = QtGui.QLabel(ui_FISCAL_iSuprimento)
        self.labelMensagem.setObjectName("labelMensagem")
        self.gridLayout.addWidget(self.labelMensagem, 1, 0, 1, 1)
        self.lineEditMensagem = QtGui.QLineEdit(ui_FISCAL_iSuprimento)
        self.lineEditMensagem.setObjectName("lineEditMensagem")
        self.gridLayout.addWidget(self.lineEditMensagem, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iSuprimento)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iSuprimento)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iSuprimento)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iSuprimento)

    def retranslateUi(self, ui_FISCAL_iSuprimento):
        ui_FISCAL_iSuprimento.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "Método iSuprimento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "100,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "Mensagem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "Abertura de Caixa", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iSuprimento", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

