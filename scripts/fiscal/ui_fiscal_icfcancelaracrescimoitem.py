# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfcancelaracrescimoitem.ui'
#
# Created: Mon Nov 24 22:25:38 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFCancelarAcrescimoItem_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFCancelarAcrescimoItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFCancelarAcrescimoItem, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrItem = self.lineEditiCFCancelarAcrescimoItem_NumeroItem.text()
        tratarRetornoFiscal(iCFCancelarAcrescimoItem_ECF_Daruma(StrItem), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFCancelarAcrescimoItem):
        ui_FISCAL_iCFCancelarAcrescimoItem.setObjectName("ui_FISCAL_iCFCancelarAcrescimoItem")
        ui_FISCAL_iCFCancelarAcrescimoItem.resize(233, 126)
        ui_FISCAL_iCFCancelarAcrescimoItem.setMinimumSize(QtCore.QSize(233, 126))
        ui_FISCAL_iCFCancelarAcrescimoItem.setMaximumSize(QtCore.QSize(233, 126))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iCFCancelarAcrescimoItem)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
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
        self.labelItem = QtGui.QLabel(ui_FISCAL_iCFCancelarAcrescimoItem)
        self.labelItem.setObjectName("labelItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelItem)
        self.lineEditiCFCancelarAcrescimoItem_NumeroItem = QtGui.QLineEdit(ui_FISCAL_iCFCancelarAcrescimoItem)
        self.lineEditiCFCancelarAcrescimoItem_NumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditiCFCancelarAcrescimoItem_NumeroItem.setMaxLength(14)
        self.lineEditiCFCancelarAcrescimoItem_NumeroItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditiCFCancelarAcrescimoItem_NumeroItem.setObjectName("lineEditiCFCancelarAcrescimoItem_NumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditiCFCancelarAcrescimoItem_NumeroItem)
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
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFCancelarAcrescimoItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFCancelarAcrescimoItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ui_FISCAL_iCFCancelarAcrescimoItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFCancelarAcrescimoItem)

    def retranslateUi(self, ui_FISCAL_iCFCancelarAcrescimoItem):
        ui_FISCAL_iCFCancelarAcrescimoItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarAcrescimoItem", "Método iCFCancelarAcrescimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarAcrescimoItem", "Número Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditiCFCancelarAcrescimoItem_NumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarAcrescimoItem", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarAcrescimoItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarAcrescimoItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

