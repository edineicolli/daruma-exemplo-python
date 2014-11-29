# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icflancaracrescimoitem.ui'
#
# Created: Mon Nov 24 22:25:46 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFLancarAcrescimoItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFLancarAcrescimoItem, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFLancarAcrescimoItem):
        ui_FISCAL_iCFLancarAcrescimoItem.setObjectName("ui_FISCAL_iCFLancarAcrescimoItem")
        ui_FISCAL_iCFLancarAcrescimoItem.resize(306, 167)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFLancarAcrescimoItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelNumeroItem = QtGui.QLabel(ui_FISCAL_iCFLancarAcrescimoItem)
        self.labelNumeroItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNumeroItem.setObjectName("labelNumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelNumeroItem)
        self.lineEditNumeroItem = QtGui.QLineEdit(ui_FISCAL_iCFLancarAcrescimoItem)
        self.lineEditNumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditNumeroItem.setMaxLength(3)
        self.lineEditNumeroItem.setObjectName("lineEditNumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNumeroItem)
        self.labelTipoAcrescimo = QtGui.QLabel(ui_FISCAL_iCFLancarAcrescimoItem)
        self.labelTipoAcrescimo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTipoAcrescimo.setObjectName("labelTipoAcrescimo")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelTipoAcrescimo)
        self.comboBoxTipoAcrescimo = QtGui.QComboBox(ui_FISCAL_iCFLancarAcrescimoItem)
        self.comboBoxTipoAcrescimo.setMinimumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoAcrescimo.setMaximumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoAcrescimo.setObjectName("comboBoxTipoAcrescimo")
        self.comboBoxTipoAcrescimo.addItem("")
        self.comboBoxTipoAcrescimo.addItem("")
        self.comboBoxTipoAcrescimo.addItem("")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxTipoAcrescimo)
        self.labelValorAcrescimo = QtGui.QLabel(ui_FISCAL_iCFLancarAcrescimoItem)
        self.labelValorAcrescimo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorAcrescimo.setObjectName("labelValorAcrescimo")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelValorAcrescimo)
        self.lineEditValorAcrescimo = QtGui.QLineEdit(ui_FISCAL_iCFLancarAcrescimoItem)
        self.lineEditValorAcrescimo.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditValorAcrescimo.setMaxLength(10)
        self.lineEditValorAcrescimo.setObjectName("lineEditValorAcrescimo")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditValorAcrescimo)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFLancarAcrescimoItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFLancarAcrescimoItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFLancarAcrescimoItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFLancarAcrescimoItem)

    def retranslateUi(self, ui_FISCAL_iCFLancarAcrescimoItem):
        ui_FISCAL_iCFLancarAcrescimoItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Método iCFLancarAcrescimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Número Item: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTipoAcrescimo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Tipo Acréscimo: ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcrescimo.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcrescimo.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "A$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcrescimo.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "A%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorAcrescimo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Valor Acréscimo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorAcrescimo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

