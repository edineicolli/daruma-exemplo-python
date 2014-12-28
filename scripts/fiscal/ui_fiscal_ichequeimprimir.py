# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_ichequeimprimir.ui'
#
# Created: Mon Nov 24 22:25:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iChequeImprimir(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iChequeImprimir, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrBanco =  self.lineEditBanco.text()
        StrCidade= self.lineEditCidade.text()
        StrFavorecido =  self.lineEditFavorecido.text()
        StrTextoLivre =  self.lineEditLivre.text()
        StrValor =  self.lineEditValor.text()
        StrData =  self.dateEdit.text()

        # Chamada do Método
        #pydaruma
        #tratarRetornoFiscal(iChequeImprimir_FS2100_Daruma(StrBanco,StrCidade,StrData,StrFavorecido,StrTextoLivre,StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iChequeImprimir):
        ui_FISCAL_iChequeImprimir.setObjectName("ui_FISCAL_iChequeImprimir")
        ui_FISCAL_iChequeImprimir.resize(232, 201)
        ui_FISCAL_iChequeImprimir.setMaximumSize(QtCore.QSize(373, 201))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iChequeImprimir)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iChequeImprimir)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditBanco = QtGui.QLineEdit(ui_FISCAL_iChequeImprimir)
        self.lineEditBanco.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEditBanco.setObjectName("lineEditBanco")
        self.gridLayout.addWidget(self.lineEditBanco, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iChequeImprimir)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditCidade = QtGui.QLineEdit(ui_FISCAL_iChequeImprimir)
        self.lineEditCidade.setMaximumSize(QtCore.QSize(211, 20))
        self.lineEditCidade.setObjectName("lineEditCidade")
        self.gridLayout.addWidget(self.lineEditCidade, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ui_FISCAL_iChequeImprimir)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(ui_FISCAL_iChequeImprimir)
        self.dateEdit.setMaximumSize(QtCore.QSize(75, 20))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ui_FISCAL_iChequeImprimir)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditFavorecido = QtGui.QLineEdit(ui_FISCAL_iChequeImprimir)
        self.lineEditFavorecido.setMaximumSize(QtCore.QSize(211, 20))
        self.lineEditFavorecido.setObjectName("lineEditFavorecido")
        self.gridLayout.addWidget(self.lineEditFavorecido, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(ui_FISCAL_iChequeImprimir)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEditLivre = QtGui.QLineEdit(ui_FISCAL_iChequeImprimir)
        self.lineEditLivre.setObjectName("lineEditLivre")
        self.gridLayout.addWidget(self.lineEditLivre, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(ui_FISCAL_iChequeImprimir)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iChequeImprimir)
        self.lineEditValor.setMaximumSize(QtCore.QSize(71, 20))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iChequeImprimir)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iChequeImprimir)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iChequeImprimir)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iChequeImprimir)

    def retranslateUi(self, ui_FISCAL_iChequeImprimir):
        ui_FISCAL_iChequeImprimir.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "N. Banco:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Cidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Favorecido:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Texto Livre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iChequeImprimir", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

