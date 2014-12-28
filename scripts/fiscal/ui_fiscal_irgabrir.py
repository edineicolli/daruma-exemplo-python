# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_irgabrir.ui'
#
# Created: Mon Nov 24 22:26:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iRGAbrir_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iRGAbrir(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iRGAbrir, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrNome= self.lineEditNome.text()

        # Chamada do Método
        tratarRetornoFiscal(iRGAbrir_ECF_Daruma(StrNome), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iRGAbrir):
        ui_FISCAL_iRGAbrir.setObjectName("ui_FISCAL_iRGAbrir")
        ui_FISCAL_iRGAbrir.resize(194, 96)
        ui_FISCAL_iRGAbrir.setMinimumSize(QtCore.QSize(194, 96))
        ui_FISCAL_iRGAbrir.setMaximumSize(QtCore.QSize(194, 96))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iRGAbrir)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_iRGAbrir)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditNome = QtGui.QLineEdit(ui_FISCAL_iRGAbrir)
        self.lineEditNome.setObjectName("lineEditNome")
        self.verticalLayout.addWidget(self.lineEditNome)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iRGAbrir)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iRGAbrir)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iRGAbrir)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iRGAbrir)

    def retranslateUi(self, ui_FISCAL_iRGAbrir):
        ui_FISCAL_iRGAbrir.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iRGAbrir", "Método iRGAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrir", "Nome do Relatório:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNome.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrir", "Gerencial X", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrir", "Abrir RG", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iRGAbrir", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

