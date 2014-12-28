# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfefetuarpagamento.ui'
#
# Created: Mon Nov 24 22:25:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFEfetuarPagamento_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFEfetuarPagamento(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFEfetuarPagamento, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrFPGTO = self.lineEditFormaPGTO.text()
        StrValor = self.lineEditValor.text()
        StrInfo = self.lineEditInfo.text()
        tratarRetornoFiscal(iCFEfetuarPagamento_ECF_Daruma(StrFPGTO,StrValor,StrInfo), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFEfetuarPagamento):
        ui_FISCAL_iCFEfetuarPagamento.setObjectName("ui_FISCAL_iCFEfetuarPagamento")
        ui_FISCAL_iCFEfetuarPagamento.resize(569, 168)
        ui_FISCAL_iCFEfetuarPagamento.setMinimumSize(QtCore.QSize(569, 168))
        ui_FISCAL_iCFEfetuarPagamento.setMaximumSize(QtCore.QSize(569, 168))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFEfetuarPagamento)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelForma = QtGui.QLabel(ui_FISCAL_iCFEfetuarPagamento)
        self.labelForma.setObjectName("labelForma")
        self.gridLayout.addWidget(self.labelForma, 0, 0, 1, 1)
        self.lineEditFormaPGTO = QtGui.QLineEdit(ui_FISCAL_iCFEfetuarPagamento)
        self.lineEditFormaPGTO.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditFormaPGTO.setObjectName("lineEditFormaPGTO")
        self.gridLayout.addWidget(self.lineEditFormaPGTO, 0, 1, 1, 1)
        self.labelValor = QtGui.QLabel(ui_FISCAL_iCFEfetuarPagamento)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 1, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCFEfetuarPagamento)
        self.lineEditValor.setMaximumSize(QtCore.QSize(70, 25))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 1, 1, 1, 1)
        self.labelInformacao = QtGui.QLabel(ui_FISCAL_iCFEfetuarPagamento)
        self.labelInformacao.setObjectName("labelInformacao")
        self.gridLayout.addWidget(self.labelInformacao, 2, 0, 1, 1)
        self.lineEditInfo = QtGui.QLineEdit(ui_FISCAL_iCFEfetuarPagamento)
        self.lineEditInfo.setMinimumSize(QtCore.QSize(401, 20))
        self.lineEditInfo.setObjectName("lineEditInfo")
        self.gridLayout.addWidget(self.lineEditInfo, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFEfetuarPagamento)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFEfetuarPagamento)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFEfetuarPagamento)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFEfetuarPagamento)

    def retranslateUi(self, ui_FISCAL_iCFEfetuarPagamento):
        ui_FISCAL_iCFEfetuarPagamento.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Método iCFEfetuarPagamento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelForma.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Forma Pagto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFormaPGTO.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Dinheiro", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInformacao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Informação Adicional:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditInfo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Obrigado Volte Sempre! DFW Efetua Forma pagamento com mensagem adicional.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamento", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

