# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfefetuarpagamentoformatado.ui'
#
# Created: Mon Nov 24 22:25:57 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCNFEfetuarPagamentoFormatado(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFEfetuarPagamentoFormatado, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCNFEfetuarPagamentoFormatado):
        ui_FISCAL_iCNFEfetuarPagamentoFormatado.setObjectName("ui_FISCAL_iCNFEfetuarPagamentoFormatado")
        ui_FISCAL_iCNFEfetuarPagamentoFormatado.resize(210, 123)
        ui_FISCAL_iCNFEfetuarPagamentoFormatado.setMinimumSize(QtCore.QSize(210, 123))
        ui_FISCAL_iCNFEfetuarPagamentoFormatado.setMaximumSize(QtCore.QSize(210, 123))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditForma = QtGui.QLineEdit(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.lineEditForma.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditForma.setObjectName("lineEditForma")
        self.gridLayout.addWidget(self.lineEditForma, 0, 1, 1, 1)
        self.labelValor = QtGui.QLabel(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 1, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.lineEditValor.setMaximumSize(QtCore.QSize(70, 25))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 1, 1, 1, 1)
        self.labelForma = QtGui.QLabel(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.labelForma.setObjectName("labelForma")
        self.gridLayout.addWidget(self.labelForma, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFEfetuarPagamentoFormatado)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFEfetuarPagamentoFormatado)

    def retranslateUi(self, ui_FISCAL_iCNFEfetuarPagamentoFormatado):
        ui_FISCAL_iCNFEfetuarPagamentoFormatado.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "Método iCNFEfetuarPagamentoFormatado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditForma.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "Dinheiro", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelForma.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "Forma Pagto:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFEfetuarPagamentoFormatado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

