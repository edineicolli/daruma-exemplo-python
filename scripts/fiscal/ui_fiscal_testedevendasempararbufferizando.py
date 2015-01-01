# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_testedevendasempararbufferizando.ui'
#
# Created: Mon Nov 24 22:26:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import regAlterarValor_Daruma, iCFAbrirPadrao_ECF_Daruma, iCFCancelar_ECF_Daruma, \
    iCFEncerrar_ECF_Daruma, iCFEfetuarPagamentoPadrao_ECF_Daruma, iCFTotalizarCupomPadrao_ECF_Daruma, \
    iCFVender_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_TesteDeVendaSemPararBufferizando(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_TesteDeVendaSemPararBufferizando, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):

        sCF = self.lineEditQtdCF.text() # recebe Quantidade de Cupom Fiscal do LineEdit
        sItem = self.lineEditQtdItem.text() # recebe Quantidade de Item do LineEdit

        regAlterarValor_Daruma("ECF\\RetornarAvisoErro","1")
        iRetornoAbrir = iCFAbrirPadrao_ECF_Daruma()

        if (iRetornoAbrir == 1):
            for cf in range(1,sCF):
                 iCFAbrirPadrao_ECF_Daruma()

                 for item in range(1,sItem):
                     #QMessageBox.information(self,"DarumaFramework - Python/Qt","Entrou no vender")
                     iRetorno = iCFVender_ECF_Daruma("I1","1,00","1,00","D$","0,00","123456789012","UN","ITEM")

                 iCFTotalizarCupomPadrao_ECF_Daruma()
                 iCFEfetuarPagamentoPadrao_ECF_Daruma()
                 iCFEncerrar_ECF_Daruma("0","Teste de Venda de Item Sem Parar. Mensagem Promocional com até 8 linhas!")
            QMessageBox.information(self,"DarumaFramework - Python/Qt","Processo Concluido.")

        if (iRetornoAbrir != 1):
            tratarRetornoFiscal(iRetornoAbrir, self)
            QMessageBox.warning(self,"DarumaFramework - Python/Qt","Erro  Primeira Venda. Cancelando Processo")
            iCFCancelar_ECF_Daruma()


        if ((sCF == "") and (sItem =="")):
            QMessageBox.information(self,"DarumaFramework - Python/Qt","Preencha todos os campos!")

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_TesteDeVendaSemPararBufferizando):
        ui_FISCAL_TesteDeVendaSemPararBufferizando.setObjectName("ui_FISCAL_TesteDeVendaSemPararBufferizando")
        ui_FISCAL_TesteDeVendaSemPararBufferizando.resize(230, 109)
        ui_FISCAL_TesteDeVendaSemPararBufferizando.setMinimumSize(QtCore.QSize(230, 109))
        ui_FISCAL_TesteDeVendaSemPararBufferizando.setMaximumSize(QtCore.QSize(230, 109))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelCF = QtGui.QLabel(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.labelCF.setObjectName("labelCF")
        self.gridLayout.addWidget(self.labelCF, 0, 0, 1, 1)
        self.lineEditQtdCF = QtGui.QLineEdit(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.lineEditQtdCF.setObjectName("lineEditQtdCF")
        self.gridLayout.addWidget(self.lineEditQtdCF, 0, 1, 1, 1)
        self.labelItem = QtGui.QLabel(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.labelItem.setObjectName("labelItem")
        self.gridLayout.addWidget(self.labelItem, 1, 0, 1, 1)
        self.lineEditQtdItem = QtGui.QLineEdit(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.lineEditQtdItem.setObjectName("lineEditQtdItem")
        self.gridLayout.addWidget(self.lineEditQtdItem, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_TesteDeVendaSemPararBufferizando)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_TesteDeVendaSemPararBufferizando)

    def retranslateUi(self, ui_FISCAL_TesteDeVendaSemPararBufferizando):
        ui_FISCAL_TesteDeVendaSemPararBufferizando.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "Teste de Venda de Item Sem Parar", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCF.setText(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "Quantidade de Cupons:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditQtdCF.setText(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.labelItem.setText(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "Quantidade de Itens no Cupom:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditQtdItem.setText(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_TesteDeVendaSemPararBufferizando", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

