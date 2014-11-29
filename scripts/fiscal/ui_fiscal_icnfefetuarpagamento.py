# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfefetuarpagamento.ui'
#
# Created: Mon Nov 24 22:25:57 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCNFEfetuarPagamento(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFEfetuarPagamento, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCNFEfetuarPagamento):
        ui_FISCAL_iCNFEfetuarPagamento.setObjectName("ui_FISCAL_iCNFEfetuarPagamento")
        ui_FISCAL_iCNFEfetuarPagamento.resize(531, 123)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCNFEfetuarPagamento)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditForma = QtGui.QLineEdit(ui_FISCAL_iCNFEfetuarPagamento)
        self.lineEditForma.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditForma.setObjectName("lineEditForma")
        self.gridLayout.addWidget(self.lineEditForma, 0, 1, 1, 1)
        self.labelValor = QtGui.QLabel(ui_FISCAL_iCNFEfetuarPagamento)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 1, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCNFEfetuarPagamento)
        self.lineEditValor.setMaximumSize(QtCore.QSize(70, 25))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 1, 1, 1, 1)
        self.labelInformacao = QtGui.QLabel(ui_FISCAL_iCNFEfetuarPagamento)
        self.labelInformacao.setObjectName("labelInformacao")
        self.gridLayout.addWidget(self.labelInformacao, 2, 0, 1, 1)
        self.lineEditInfo = QtGui.QLineEdit(ui_FISCAL_iCNFEfetuarPagamento)
        self.lineEditInfo.setMinimumSize(QtCore.QSize(401, 20))
        self.lineEditInfo.setObjectName("lineEditInfo")
        self.gridLayout.addWidget(self.lineEditInfo, 2, 1, 1, 1)
        self.labelForma = QtGui.QLabel(ui_FISCAL_iCNFEfetuarPagamento)
        self.labelForma.setObjectName("labelForma")
        self.gridLayout.addWidget(self.labelForma, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCNFEfetuarPagamento)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCNFEfetuarPagamento)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFEfetuarPagamento)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFEfetuarPagamento)

    def retranslateUi(self, ui_FISCAL_iCNFEfetuarPagamento):
        ui_FISCAL_iCNFEfetuarPagamento.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Método iCNFEfetuarPagamento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditForma.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Dinheiro", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInformacao.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Informação Adicional:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditInfo.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Obrigado Volte Sempre! DFW Efetua Forma pagamento com mensagem adicional.", None, QtGui.QApplication.UnicodeUTF8))
        self.labelForma.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Forma Pagto:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamento", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

