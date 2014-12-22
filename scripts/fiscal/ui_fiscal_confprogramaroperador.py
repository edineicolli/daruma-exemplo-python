# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_confprogramaroperador.ui'
#
# Created: Mon Nov 24 22:25:24 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import confProgramarOperador_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_confProgramarOperador(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_confProgramarOperador, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrOperador = self.lineEditOperador.text()

        # Chamada do Método
        tratarRetornoFiscal(confProgramarOperador_ECF_Daruma(StrOperador), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_confProgramarOperador):
        ui_FISCAL_confProgramarOperador.setObjectName("ui_FISCAL_confProgramarOperador")
        ui_FISCAL_confProgramarOperador.resize(270, 88)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_confProgramarOperador)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelOperador = QtGui.QLabel(ui_FISCAL_confProgramarOperador)
        self.labelOperador.setObjectName("labelOperador")
        self.verticalLayout.addWidget(self.labelOperador)
        self.lineEditOperador = QtGui.QLineEdit(ui_FISCAL_confProgramarOperador)
        self.lineEditOperador.setMaxLength(20)
        self.lineEditOperador.setCursorPosition(1)
        self.lineEditOperador.setObjectName("lineEditOperador")
        self.verticalLayout.addWidget(self.lineEditOperador)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_confProgramarOperador)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_confProgramarOperador)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_confProgramarOperador)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_confProgramarOperador)

    def retranslateUi(self, ui_FISCAL_confProgramarOperador):
        ui_FISCAL_confProgramarOperador.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_confProgramarOperador", "Método confProgramarOperador_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOperador.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarOperador", "Digite o Operador:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditOperador.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarOperador", "Operador: A Turno: M", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarOperador", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarOperador", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

