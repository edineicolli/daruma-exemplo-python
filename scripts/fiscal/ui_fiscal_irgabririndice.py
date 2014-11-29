# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_irgabririndice.ui'
#
# Created: Mon Nov 24 22:26:05 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iRGAbrirIndice(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iRGAbrirIndice, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iRGAbrirIndice):
        ui_FISCAL_iRGAbrirIndice.setObjectName("ui_FISCAL_iRGAbrirIndice")
        ui_FISCAL_iRGAbrirIndice.resize(194, 98)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iRGAbrirIndice)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_iRGAbrirIndice)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEditIndice = QtGui.QLineEdit(ui_FISCAL_iRGAbrirIndice)
        self.lineEditIndice.setMinimumSize(QtCore.QSize(41, 20))
        self.lineEditIndice.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEditIndice.setObjectName("lineEditIndice")
        self.horizontalLayout_2.addWidget(self.lineEditIndice)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iRGAbrirIndice)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iRGAbrirIndice)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iRGAbrirIndice)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iRGAbrirIndice)

    def retranslateUi(self, ui_FISCAL_iRGAbrirIndice):
        ui_FISCAL_iRGAbrirIndice.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iRGAbrirIndice", "Método iRGAbrirIndice_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrirIndice", "Indice do Relatório:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditIndice.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrirIndice", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrirIndice", "Abrir RG", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrirIndice", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

