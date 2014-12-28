# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfcancelardescontoitem.ui'
#
# Created: Mon Nov 24 22:25:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFCancelarDescontoItem_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFCancelarDescontoItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFCancelarDescontoItem, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrItem = self.lineEditiCFCancelarDescontoItem_NumeroItem.text()

        tratarRetornoFiscal(iCFCancelarDescontoItem_ECF_Daruma(StrItem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFCancelarDescontoItem):
        ui_FISCAL_iCFCancelarDescontoItem.setObjectName("ui_FISCAL_iCFCancelarDescontoItem")
        ui_FISCAL_iCFCancelarDescontoItem.resize(233, 100)
        ui_FISCAL_iCFCancelarDescontoItem.setMinimumSize(QtCore.QSize(233, 100))
        ui_FISCAL_iCFCancelarDescontoItem.setMaximumSize(QtCore.QSize(233, 100))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFCancelarDescontoItem)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.labelItem = QtGui.QLabel(ui_FISCAL_iCFCancelarDescontoItem)
        self.labelItem.setObjectName("labelItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelItem)
        self.lineEditiCFCancelarDescontoItem_NumeroItem = QtGui.QLineEdit(ui_FISCAL_iCFCancelarDescontoItem)
        self.lineEditiCFCancelarDescontoItem_NumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditiCFCancelarDescontoItem_NumeroItem.setMaxLength(14)
        self.lineEditiCFCancelarDescontoItem_NumeroItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditiCFCancelarDescontoItem_NumeroItem.setObjectName("lineEditiCFCancelarDescontoItem_NumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditiCFCancelarDescontoItem_NumeroItem)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFCancelarDescontoItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFCancelarDescontoItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFCancelarDescontoItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFCancelarDescontoItem)

    def retranslateUi(self, ui_FISCAL_iCFCancelarDescontoItem):
        ui_FISCAL_iCFCancelarDescontoItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarDescontoItem", "Método iCFCancelarDescontoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarDescontoItem", "Número Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditiCFCancelarDescontoItem_NumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarDescontoItem", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarDescontoItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarDescontoItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

