# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfbpvender.ui'
#
# Created: Mon Nov 24 22:25:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFBPVender_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFBPVender(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFBPVender, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrDescricao = self.lineEditDescricao.text()
        StrAliquota = self.lineEditAliquota.text()
        StrValorProd = self.lineEditValorProd.text()
        StrValorAcresDesc = self.lineEditValorAcrescDesc.text()
        StrTipoAcresDesc = self.comboBox.currentText()

        tratarRetornoFiscal(iCFBPVender_ECF_Daruma(StrAliquota,StrValorProd,StrTipoAcresDesc,StrValorAcresDesc,StrDescricao), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFBPVender):
        ui_FISCAL_iCFBPVender.setObjectName("ui_FISCAL_iCFBPVender")
        ui_FISCAL_iCFBPVender.setWindowModality(QtCore.Qt.NonModal)
        ui_FISCAL_iCFBPVender.resize(254, 222)
        ui_FISCAL_iCFBPVender.setMinimumSize(QtCore.QSize(254, 222))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFBPVender)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtGui.QLabel(ui_FISCAL_iCFBPVender)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditDescricao = QtGui.QLineEdit(ui_FISCAL_iCFBPVender)
        self.lineEditDescricao.setObjectName("lineEditDescricao")
        self.gridLayout_4.addWidget(self.lineEditDescricao, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCFBPVender)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditAliquota = QtGui.QLineEdit(ui_FISCAL_iCFBPVender)
        self.lineEditAliquota.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditAliquota.setObjectName("lineEditAliquota")
        self.gridLayout_4.addWidget(self.lineEditAliquota, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(ui_FISCAL_iCFBPVender)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditValorProd = QtGui.QLineEdit(ui_FISCAL_iCFBPVender)
        self.lineEditValorProd.setObjectName("lineEditValorProd")
        self.gridLayout.addWidget(self.lineEditValorProd, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(ui_FISCAL_iCFBPVender)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtGui.QComboBox(ui_FISCAL_iCFBPVender)
        self.comboBox.setMaximumSize(QtCore.QSize(41, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(ui_FISCAL_iCFBPVender)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditValorAcrescDesc = QtGui.QLineEdit(ui_FISCAL_iCFBPVender)
        self.lineEditValorAcrescDesc.setObjectName("lineEditValorAcrescDesc")
        self.gridLayout_2.addWidget(self.lineEditValorAcrescDesc, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFBPVender)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFBPVender)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFBPVender)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFBPVender)

    def retranslateUi(self, ui_FISCAL_iCFBPVender):
        ui_FISCAL_iCFBPVender.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Método iCFBPVender_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Descrição: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDescricao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Bagagem", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Alíquota:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "FF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Valor Produto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorProd.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Tipo Acres/Desc:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "A%", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "A$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "D%", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "D$", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Valor Desc/Acresc:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorAcrescDesc.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "0,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPVender", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

