# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rretornarinformacaoseparador.ui'
#
# Created: Mon Nov 24 22:26:33 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
from ctypes import create_string_buffer

from PySide import QtCore, QtGui
from pydaruma.pydaruma import rRetornarInformacaoSeparador_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_rRetornarInformacaoSeparador(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rRetornarInformacaoSeparador, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrIndice =  self.lineEditIndice.text()
        StrValor = self.lineEditValorSig.text()

        # Definiçao do Tamanho do Vetor de Recebimento da informação
        cRetorno = create_string_buffer(1212)

        #Execuçao do Método de Retorno da Informação
        tratarRetornoFiscal(rRetornarInformacaoSeparador_ECF_Daruma(StrIndice, StrValor,cRetorno), self)

        # Converte o char Retorno para QString, para poder ser transferido para o TextEdit
        StrRetorno = cRetorno

        # Devolve o retorno da DLL para o campo de texto
        self.textEditRetorno.setText(StrRetorno)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rRetornarInformacaoSeparador):
        ui_FISCAL_rRetornarInformacaoSeparador.setObjectName("ui_FISCAL_rRetornarInformacaoSeparador")
        ui_FISCAL_rRetornarInformacaoSeparador.resize(624, 453)
        ui_FISCAL_rRetornarInformacaoSeparador.setMinimumSize(QtCore.QSize(624, 453))
        ui_FISCAL_rRetornarInformacaoSeparador.setMaximumSize(QtCore.QSize(624, 453))
        self.verticalLayout_6 = QtGui.QVBoxLayout(ui_FISCAL_rRetornarInformacaoSeparador)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxInformacoes = QtGui.QGroupBox(ui_FISCAL_rRetornarInformacaoSeparador)
        self.groupBoxInformacoes.setObjectName("groupBoxInformacoes")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBoxInformacoes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBoxInformacoes)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditIndice = QtGui.QLineEdit(self.groupBoxInformacoes)
        self.lineEditIndice.setMaximumSize(QtCore.QSize(51, 20))
        self.lineEditIndice.setObjectName("lineEditIndice")
        self.gridLayout.addWidget(self.lineEditIndice, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxInformacoes)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditValorSig = QtGui.QLineEdit(self.groupBoxInformacoes)
        self.lineEditValorSig.setMaximumSize(QtCore.QSize(51, 20))
        self.lineEditValorSig.setObjectName("lineEditValorSig")
        self.gridLayout.addWidget(self.lineEditValorSig, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(self.groupBoxInformacoes)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxInformacoes)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBoxInformacoes)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtGui.QSpacerItem(17, 27, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.groupBoxRetorno = QtGui.QGroupBox(ui_FISCAL_rRetornarInformacaoSeparador)
        self.groupBoxRetorno.setMaximumSize(QtCore.QSize(606, 301))
        self.groupBoxRetorno.setObjectName("groupBoxRetorno")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBoxRetorno)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.textEditRetorno = QtGui.QTextEdit(self.groupBoxRetorno)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditRetorno.sizePolicy().hasHeightForWidth())
        self.textEditRetorno.setSizePolicy(sizePolicy)
        self.textEditRetorno.setMinimumSize(QtCore.QSize(0, 0))
        self.textEditRetorno.setObjectName("textEditRetorno")
        self.verticalLayout.addWidget(self.textEditRetorno)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_6.addWidget(self.groupBoxRetorno)

        self.retranslateUi(ui_FISCAL_rRetornarInformacaoSeparador)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rRetornarInformacaoSeparador)

    def retranslateUi(self, ui_FISCAL_rRetornarInformacaoSeparador):
        ui_FISCAL_rRetornarInformacaoSeparador.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Método rRetornarInformacaoSeparador_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxInformacoes.setTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Informações:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Indice da Informação:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditIndice.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "78", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Valor Significativo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorSig.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxRetorno.setTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacaoSeparador", "Retorno:", None, QtGui.QApplication.UnicodeUTF8))

