# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iccdabrir.ui'
#
# Created: Mon Nov 24 22:25:32 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCCDAbrir_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCCDAbrir(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCCDAbrir, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrFPGTO = self.lineEditFormaPagamento.text()
        StrParcelas = self.lineEditParcelas.text()
        StrValor = self.lineEditValor.text()
        StrDocOrigem = self.lineEditDocOrigem.text()
        StrCPF =  self.lineEditCPF.text()
        StrNome = self.lineEditNome.text()
        StrEndereco =  self.lineEditEndereco.text()

        # Chamada do Método
        tratarRetornoFiscal(iCCDAbrir_ECF_Daruma(StrFPGTO,StrParcelas,StrDocOrigem,StrValor,StrCPF,StrNome,StrEndereco), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCCDAbrir):
        ui_FISCAL_iCCDAbrir.setObjectName("ui_FISCAL_iCCDAbrir")
        ui_FISCAL_iCCDAbrir.resize(299, 227)
        ui_FISCAL_iCCDAbrir.setMinimumSize(QtCore.QSize(299, 227))
        ui_FISCAL_iCCDAbrir.setMaximumSize(QtCore.QSize(299, 227))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCCDAbrir)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditFormaPagamento = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditFormaPagamento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditFormaPagamento.setObjectName("lineEditFormaPagamento")
        self.gridLayout.addWidget(self.lineEditFormaPagamento, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditParcelas = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditParcelas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditParcelas.setObjectName("lineEditParcelas")
        self.gridLayout.addWidget(self.lineEditParcelas, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditDocOrigem = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditDocOrigem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditDocOrigem.setObjectName("lineEditDocOrigem")
        self.gridLayout.addWidget(self.lineEditDocOrigem, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditValor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditValor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEditCPF = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditCPF.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.gridLayout.addWidget(self.lineEditCPF, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEditNome = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditNome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditNome.setObjectName("lineEditNome")
        self.gridLayout.addWidget(self.lineEditNome, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(ui_FISCAL_iCCDAbrir)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEditEndereco = QtGui.QLineEdit(ui_FISCAL_iCCDAbrir)
        self.lineEditEndereco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.gridLayout.addWidget(self.lineEditEndereco, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCCDAbrir)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCCDAbrir)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCCDAbrir)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCCDAbrir)

    def retranslateUi(self, ui_FISCAL_iCCDAbrir):
        ui_FISCAL_iCCDAbrir.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Método iCCDAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Forma de Pagamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFormaPagamento.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Cartão de Credito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Parcelas:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditParcelas.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Doc. Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDocOrigem.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "000987", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "CPF:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCPF.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "111.111.111-11", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNome.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Daruma Developers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Endereço", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEndereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Shishima Hifumi, 2910", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Abrir CCD", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDAbrir", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

