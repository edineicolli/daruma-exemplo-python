# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_itef_imprimirrespostacartao.ui'
#
# Created: Mon Nov 24 22:26:09 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFAbrirPadrao_ECF_Daruma, iCFVenderResumido_ECF_Daruma, \
    iCFTotalizarCupomPadrao_ECF_Daruma, iCFEfetuarPagamentoFormatado_ECF_Daruma, iCFEncerrarPadrao_ECF_Daruma, \
    iTEF_Fechar_ECF_Daruma, iTEF_ImprimirRespostaCartao_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iTEF_ImprimirRespostaCartao(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iTEF_ImprimirRespostaCartao, self).__init__()

        self.setupUi(self)
        self.pushButtonFecharDocumento.clicked.connect(self.on_pushButtonFecharDocumento_clicked)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButtonImprimirRespostaTEF.clicked.connect(self.on_pushButtonImprimirRespostaTEF_clicked)
        self.pushButtonImprimirCF.clicked.connect(self.on_pushButtonImprimirCF_clicked)

    def on_pushButtonImprimirCF_clicked(self):
        StrValorPagamento = self.lineEditValorPgto.text()
        StrFormaPagamento = self.lineEditFormaPgto.text()

        iRetorno = iCFAbrirPadrao_ECF_Daruma()
        if(iRetorno != 1):
            tratarRetornoFiscal(iRetorno, self)

        iCFVenderResumido_ECF_Daruma("F1","2,00","123456789","ITEM DE TESTE")
        iCFVenderResumido_ECF_Daruma("F1","2,00","123456789","ITEM DE TESTE")
        iCFVenderResumido_ECF_Daruma("F1","2,00","123456789","ITEM DE TESTE")
        iCFVenderResumido_ECF_Daruma("F1","2,00","123456789","ITEM DE TESTE")
        iRetorno = iCFVenderResumido_ECF_Daruma("F1","2,00","123456789","ITEM DE TESTE")
        if(iRetorno != 1):
            tratarRetornoFiscal(iRetorno, self)

        iRetorno = iCFTotalizarCupomPadrao_ECF_Daruma()
        if(iRetorno != 1):
            tratarRetornoFiscal(iRetorno, self)

        iRetorno = iCFEfetuarPagamentoFormatado_ECF_Daruma(StrFormaPagamento,StrValorPagamento)
        if(iRetorno != 1):
            tratarRetornoFiscal(iRetorno, self)

        iRetorno = iCFEncerrarPadrao_ECF_Daruma()
        tratarRetornoFiscal(iRetorno, self)

    def on_pushButtonImprimirRespostaTEF_clicked(self):
        StrLocalArquivo = self.lineEditCaminhoArq.text()
        StrFormaPagamento = self.lineEditFormaPgto.text()
        StrValorPagamento = self.lineEditValorPgto.text()

        if(self.radioButtonTravarNAO.isChecked()):
            bTravarTeclado = False
            tratarRetornoFiscal(iTEF_ImprimirRespostaCartao_ECF_Daruma(StrLocalArquivo,bTravarTeclado,StrFormaPagamento,StrValorPagamento), self)

        if(self.radioButtonTravarSIM.isChecked()):
            bTravarTeclado = True
            tratarRetornoFiscal(iTEF_ImprimirRespostaCartao_ECF_Daruma(StrLocalArquivo,bTravarTeclado,StrFormaPagamento,StrValorPagamento),self)

    def on_pushButtonFecharDocumento_clicked(self):
        tratarRetornoFiscal(iTEF_Fechar_ECF_Daruma(), self)

    def on_pushButton_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iTEF_ImprimirRespostaCartao):
        ui_FISCAL_iTEF_ImprimirRespostaCartao.setObjectName("ui_FISCAL_iTEF_ImprimirRespostaCartao")
        ui_FISCAL_iTEF_ImprimirRespostaCartao.resize(293, 506)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditCaminhoArq = QtGui.QLineEdit(self.groupBox)
        self.lineEditCaminhoArq.setObjectName("lineEditCaminhoArq")
        self.gridLayout.addWidget(self.lineEditCaminhoArq, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(61, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(76, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 2)
        self.radioButtonTravarSIM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonTravarSIM.setObjectName("radioButtonTravarSIM")
        self.gridLayout_2.addWidget(self.radioButtonTravarSIM, 1, 2, 1, 1)
        self.radioButtonTravarNAO = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonTravarNAO.setObjectName("radioButtonTravarNAO")
        self.gridLayout_2.addWidget(self.radioButtonTravarNAO, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(76, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 4, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEditValorPgto = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditValorPgto.setObjectName("lineEditValorPgto")
        self.gridLayout_3.addWidget(self.lineEditValorPgto, 4, 0, 1, 1)
        self.lineEditFormaPgto = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditFormaPgto.setObjectName("lineEditFormaPgto")
        self.gridLayout_3.addWidget(self.lineEditFormaPgto, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButtonImprimirCF = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonImprimirCF.setObjectName("pushButtonImprimirCF")
        self.gridLayout_4.addWidget(self.pushButtonImprimirCF, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)
        self.pushButtonImprimirRespostaTEF = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonImprimirRespostaTEF.setObjectName("pushButtonImprimirRespostaTEF")
        self.gridLayout_4.addWidget(self.pushButtonImprimirRespostaTEF, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.pushButtonFecharDocumento = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonFecharDocumento.setObjectName("pushButtonFecharDocumento")
        self.gridLayout_4.addWidget(self.pushButtonFecharDocumento, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtGui.QPushButton(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iTEF_ImprimirRespostaCartao)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iTEF_ImprimirRespostaCartao)

    def retranslateUi(self, ui_FISCAL_iTEF_ImprimirRespostaCartao):
        ui_FISCAL_iTEF_ImprimirRespostaCartao.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Método iTEF_ImprimirRespostaCartao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Digite o Diretório e o nome do arquivo com extensão:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminhoArq.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "C:\\Tef_Dial\\Resp\\Intpos.001", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Teclado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Deseja travar o teclado?", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTravarSIM.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Sim", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTravarNAO.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Não", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Pagamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Forma de Pagamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Valor do Pagamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorPgto.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFormaPgto.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "CARTAO", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Cupom Fiscal e TEF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Impressão de Cupom Fiscal:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImprimirCF.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Impressão de Resposta:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImprimirRespostaTEF.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Impressão TEF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Encerrar CCD ou Gerencial:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFecharDocumento.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Fechar Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ui_FISCAL_iTEF_ImprimirRespostaCartao", "Fechar Janela", None, QtGui.QApplication.UnicodeUTF8))

