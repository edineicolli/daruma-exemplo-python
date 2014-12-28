# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iccdabrirsimplificado.ui'
#
# Created: Mon Nov 24 22:25:32 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCCDAbrirSimplificado_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCCDAbrirSimplificado(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCCDAbrirSimplificado, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrFPGTO = self.lineEditFormaPagamento.text()
        StrParcelas = self.lineEditParcelas.text()
        StrValor = self.lineEditValor.text()
        StrDocOrigem = self.lineEditDocOrigem.text()

        # Chamada do Método
        tratarRetornoFiscal(iCCDAbrirSimplificado_ECF_Daruma(StrFPGTO,StrParcelas,StrDocOrigem,StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCCDAbrirSimplificado):
        ui_FISCAL_iCCDAbrirSimplificado.setObjectName("ui_FISCAL_iCCDAbrirSimplificado")
        ui_FISCAL_iCCDAbrirSimplificado.resize(275, 149)
        ui_FISCAL_iCCDAbrirSimplificado.setMinimumSize(QtCore.QSize(275, 149))
        ui_FISCAL_iCCDAbrirSimplificado.setMaximumSize(QtCore.QSize(275, 149))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCCDAbrirSimplificado)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCCDAbrirSimplificado)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditFormaPagamento = QtGui.QLineEdit(ui_FISCAL_iCCDAbrirSimplificado)
        self.lineEditFormaPagamento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditFormaPagamento.setObjectName("lineEditFormaPagamento")
        self.gridLayout.addWidget(self.lineEditFormaPagamento, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCCDAbrirSimplificado)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditParcelas = QtGui.QLineEdit(ui_FISCAL_iCCDAbrirSimplificado)
        self.lineEditParcelas.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditParcelas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditParcelas.setObjectName("lineEditParcelas")
        self.gridLayout.addWidget(self.lineEditParcelas, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ui_FISCAL_iCCDAbrirSimplificado)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditDocOrigem = QtGui.QLineEdit(ui_FISCAL_iCCDAbrirSimplificado)
        self.lineEditDocOrigem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDocOrigem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditDocOrigem.setObjectName("lineEditDocOrigem")
        self.gridLayout.addWidget(self.lineEditDocOrigem, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ui_FISCAL_iCCDAbrirSimplificado)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCCDAbrirSimplificado)
        self.lineEditValor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditValor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCCDAbrirSimplificado)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCCDAbrirSimplificado)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCCDAbrirSimplificado)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCCDAbrirSimplificado)

    def retranslateUi(self, ui_FISCAL_iCCDAbrirSimplificado):
        ui_FISCAL_iCCDAbrirSimplificado.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Método iCCDAbrirSimplificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Forma de Pagamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFormaPagamento.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Cartão de Credito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Parcelas:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditParcelas.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Doc. Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDocOrigem.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "000987", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Abrir CCD", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrirSimplificado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

