# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfcancelaritemparcial.ui'
#
# Created: Mon Nov 24 22:25:40 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFCancelarItemParcial_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFCancelarItemParcial(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFCancelarItemParcial, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrNumeroItem = self.lineEditNumeroItem.text()
        StrQuantidade = self.lineEditQuantidade.text()
        tratarRetornoFiscal(iCFCancelarItemParcial_ECF_Daruma(StrNumeroItem,StrQuantidade), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFCancelarItemParcial):
        ui_FISCAL_iCFCancelarItemParcial.setObjectName("ui_FISCAL_iCFCancelarItemParcial")
        ui_FISCAL_iCFCancelarItemParcial.resize(233, 126)
        ui_FISCAL_iCFCancelarItemParcial.setMinimumSize(QtCore.QSize(233, 126))
        ui_FISCAL_iCFCancelarItemParcial.setMaximumSize(QtCore.QSize(233, 126))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFCancelarItemParcial)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 4, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelItem = QtGui.QLabel(ui_FISCAL_iCFCancelarItemParcial)
        self.labelItem.setObjectName("labelItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelItem)
        self.lineEditNumeroItem = QtGui.QLineEdit(ui_FISCAL_iCFCancelarItemParcial)
        self.lineEditNumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditNumeroItem.setMaxLength(3)
        self.lineEditNumeroItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditNumeroItem.setObjectName("lineEditNumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNumeroItem)
        self.labelQuantidade = QtGui.QLabel(ui_FISCAL_iCFCancelarItemParcial)
        self.labelQuantidade.setObjectName("labelQuantidade")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelQuantidade)
        self.lineEditQuantidade = QtGui.QLineEdit(ui_FISCAL_iCFCancelarItemParcial)
        self.lineEditQuantidade.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditQuantidade.setMaxLength(14)
        self.lineEditQuantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditQuantidade)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFCancelarItemParcial)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFCancelarItemParcial)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFCancelarItemParcial)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFCancelarItemParcial)

    def retranslateUi(self, ui_FISCAL_iCFCancelarItemParcial):
        ui_FISCAL_iCFCancelarItemParcial.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "Método iCFCancelarItemParcial_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "Número Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.labelQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "Quantidade Item: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItemParcial", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

