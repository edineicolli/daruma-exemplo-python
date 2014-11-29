# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfcancelaritem.ui'
#
# Created: Mon Nov 24 22:25:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFCancelarItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFCancelarItem, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFCancelarItem):
        ui_FISCAL_iCFCancelarItem.setObjectName("ui_FISCAL_iCFCancelarItem")
        ui_FISCAL_iCFCancelarItem.resize(226, 105)
        ui_FISCAL_iCFCancelarItem.setMinimumSize(QtCore.QSize(226, 105))
        ui_FISCAL_iCFCancelarItem.setMaximumSize(QtCore.QSize(226, 105))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFCancelarItem)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelItem = QtGui.QLabel(ui_FISCAL_iCFCancelarItem)
        self.labelItem.setObjectName("labelItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelItem)
        self.lineEditNumeroItem = QtGui.QLineEdit(ui_FISCAL_iCFCancelarItem)
        self.lineEditNumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditNumeroItem.setMaxLength(3)
        self.lineEditNumeroItem.setObjectName("lineEditNumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNumeroItem)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFCancelarItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFCancelarItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFCancelarItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFCancelarItem)

    def retranslateUi(self, ui_FISCAL_iCFCancelarItem):
        ui_FISCAL_iCFCancelarItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItem", "Método iCFCancelarItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItem", "Número Item: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItem", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

