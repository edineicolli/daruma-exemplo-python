# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_confprogramaridloja.ui'
#
# Created: Mon Nov 24 22:25:23 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import confProgramarIDLoja_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_confProgramarIDLoja(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_confProgramarIDLoja, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrID =  self.lineEditID.text()

        # Chamada do Método
        tratarRetornoFiscal(confProgramarIDLoja_ECF_Daruma(StrID), self)
        self.close();

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_confProgramarIDLoja):
        ui_FISCAL_confProgramarIDLoja.setObjectName("ui_FISCAL_confProgramarIDLoja")
        ui_FISCAL_confProgramarIDLoja.resize(194, 79)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_confProgramarIDLoja)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_confProgramarIDLoja)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditID = QtGui.QLineEdit(ui_FISCAL_confProgramarIDLoja)
        self.lineEditID.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEditID.setMaxLength(4)
        self.lineEditID.setObjectName("lineEditID")
        self.horizontalLayout_2.addWidget(self.lineEditID)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_confProgramarIDLoja)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_confProgramarIDLoja)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_confProgramarIDLoja)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_confProgramarIDLoja)

    def retranslateUi(self, ui_FISCAL_confProgramarIDLoja):
        ui_FISCAL_confProgramarIDLoja.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_confProgramarIDLoja", "Método confProgramarIDLoja", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarIDLoja", "ID Loja:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditID.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarIDLoja", "A1B2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarIDLoja", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarIDLoja", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

