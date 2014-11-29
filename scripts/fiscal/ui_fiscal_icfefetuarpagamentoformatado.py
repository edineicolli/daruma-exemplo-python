# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfefetuarpagamentoformatado.ui'
#
# Created: Mon Nov 24 22:25:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFEfetuarPagamentoFormatado(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFEfetuarPagamentoFormatado, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFEfetuarPagamentoFormatado):
        ui_FISCAL_iCFEfetuarPagamentoFormatado.setObjectName("ui_FISCAL_iCFEfetuarPagamentoFormatado")
        ui_FISCAL_iCFEfetuarPagamentoFormatado.resize(309, 132)
        ui_FISCAL_iCFEfetuarPagamentoFormatado.setMinimumSize(QtCore.QSize(309, 132))
        ui_FISCAL_iCFEfetuarPagamentoFormatado.setMaximumSize(QtCore.QSize(309, 132))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelForma = QtGui.QLabel(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.labelForma.setObjectName("labelForma")
        self.gridLayout.addWidget(self.labelForma, 0, 0, 1, 1)
        self.lineEditFormaPGTO = QtGui.QLineEdit(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.lineEditFormaPGTO.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditFormaPGTO.setObjectName("lineEditFormaPGTO")
        self.gridLayout.addWidget(self.lineEditFormaPGTO, 0, 1, 1, 1)
        self.labelValor = QtGui.QLabel(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 1, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.lineEditValor.setMaximumSize(QtCore.QSize(70, 25))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFEfetuarPagamentoFormatado)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFEfetuarPagamentoFormatado)

    def retranslateUi(self, ui_FISCAL_iCFEfetuarPagamentoFormatado):
        ui_FISCAL_iCFEfetuarPagamentoFormatado.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamentoFormatado", "iCFEfetuarPagamentoFormatado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelForma.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamentoFormatado", "Forma Pagto:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamentoFormatado", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamentoFormatado", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEfetuarPagamentoFormatado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

