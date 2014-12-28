# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iestornarpagamento.ui'
#
# Created: Mon Nov 24 22:26:01 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iEstornarPagamento_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iEstornarPagamento(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iEstornarPagamento, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaracao de variaveis de recebimento da UI
        StrEstornar = self.lineEditEstornar.text()
        StrEfetivar = self.lineEditEfetivar.text()
        StrValor = self.lineEditValor.text()
        StrMensagem = self.lineEditMensagem.text()

        # Chamada do Método / Tratamento de Retorno
        tratarRetornoFiscal(iEstornarPagamento_ECF_Daruma(StrEstornar,StrEfetivar,StrValor,StrMensagem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iEstornarPagamento):
        ui_FISCAL_iEstornarPagamento.setObjectName("ui_FISCAL_iEstornarPagamento")
        ui_FISCAL_iEstornarPagamento.resize(318, 168)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_FISCAL_iEstornarPagamento.sizePolicy().hasHeightForWidth())
        ui_FISCAL_iEstornarPagamento.setSizePolicy(sizePolicy)
        ui_FISCAL_iEstornarPagamento.setMinimumSize(QtCore.QSize(318, 168))
        ui_FISCAL_iEstornarPagamento.setMaximumSize(QtCore.QSize(318, 168))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iEstornarPagamento)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iEstornarPagamento)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditEstornar = QtGui.QLineEdit(ui_FISCAL_iEstornarPagamento)
        self.lineEditEstornar.setObjectName("lineEditEstornar")
        self.gridLayout.addWidget(self.lineEditEstornar, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iEstornarPagamento)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditEfetivar = QtGui.QLineEdit(ui_FISCAL_iEstornarPagamento)
        self.lineEditEfetivar.setObjectName("lineEditEfetivar")
        self.gridLayout.addWidget(self.lineEditEfetivar, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ui_FISCAL_iEstornarPagamento)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iEstornarPagamento)
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ui_FISCAL_iEstornarPagamento)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEditMensagem = QtGui.QLineEdit(ui_FISCAL_iEstornarPagamento)
        self.lineEditMensagem.setObjectName("lineEditMensagem")
        self.gridLayout.addWidget(self.lineEditMensagem, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iEstornarPagamento)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iEstornarPagamento)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iEstornarPagamento)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iEstornarPagamento)

    def retranslateUi(self, ui_FISCAL_iEstornarPagamento):
        ui_FISCAL_iEstornarPagamento.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Método iEstornarPagamento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Forma de Pagamento a Estornar:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEstornar.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Cartão Crédito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Forma de Pagamento a Efetivar:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEfetivar.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Cartão Débito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "                                          Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "                       Mensagem Livre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Estorno de Pagamento", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iEstornarPagamento", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

