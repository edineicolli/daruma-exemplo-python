# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icflancardescontoultimoitem.ui'
#
# Created: Mon Nov 24 22:25:49 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFLancarDescontoUltimoItem_ECF_Daruma

from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFLancarDescontoUltimoItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFLancarDescontoUltimoItem, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrValorDesc = self.lineEditValorDesconto.text()
        StrTipoDesc = self.comboBoxTipoDesconto.currentText()
        tratarRetornoFiscal(iCFLancarDescontoUltimoItem_ECF_Daruma(StrTipoDesc,StrValorDesc), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFLancarDescontoUltimoItem):
        ui_FISCAL_iCFLancarDescontoUltimoItem.setObjectName("ui_FISCAL_iCFLancarDescontoUltimoItem")
        ui_FISCAL_iCFLancarDescontoUltimoItem.resize(244, 117)
        ui_FISCAL_iCFLancarDescontoUltimoItem.setMinimumSize(QtCore.QSize(244, 117))
        ui_FISCAL_iCFLancarDescontoUltimoItem.setMaximumSize(QtCore.QSize(244, 117))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.labelTipoDesconto = QtGui.QLabel(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.labelTipoDesconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTipoDesconto.setObjectName("labelTipoDesconto")
        self.gridLayout.addWidget(self.labelTipoDesconto, 0, 1, 1, 1)
        self.comboBoxTipoDesconto = QtGui.QComboBox(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.comboBoxTipoDesconto.setMinimumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoDesconto.setMaximumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoDesconto.setObjectName("comboBoxTipoDesconto")
        self.comboBoxTipoDesconto.addItem("")
        self.comboBoxTipoDesconto.addItem("")
        self.comboBoxTipoDesconto.addItem("")
        self.gridLayout.addWidget(self.comboBoxTipoDesconto, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.labelValorDesconto = QtGui.QLabel(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.labelValorDesconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorDesconto.setObjectName("labelValorDesconto")
        self.gridLayout.addWidget(self.labelValorDesconto, 1, 1, 1, 1)
        self.lineEditValorDesconto = QtGui.QLineEdit(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.lineEditValorDesconto.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditValorDesconto.setMaxLength(10)
        self.lineEditValorDesconto.setObjectName("lineEditValorDesconto")
        self.gridLayout.addWidget(self.lineEditValorDesconto, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFLancarDescontoUltimoItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFLancarDescontoUltimoItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFLancarDescontoUltimoItem)

    def retranslateUi(self, ui_FISCAL_iCFLancarDescontoUltimoItem):
        ui_FISCAL_iCFLancarDescontoUltimoItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "Método iCFLancarDescontoUltimoItem", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTipoDesconto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "Tipo Desconto: ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDesconto.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDesconto.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "D$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDesconto.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "D%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorDesconto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "Valor Desconto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorDesconto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoUltimoItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

