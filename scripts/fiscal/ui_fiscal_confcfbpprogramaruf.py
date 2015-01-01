# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_confcfbpprogramaruf.ui'
#
# Created: Mon Nov 24 22:25:21 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import confCFBPProgramarUF_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_confCFBPProgramarUF(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_confCFBPProgramarUF, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Recebe valor em QString do LineEdit
        StrUF = self.lineEditUF.text()

        # Chamada do Método
        tratarRetornoFiscal(confCFBPProgramarUF_ECF_Daruma(StrUF), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_confCFBPProgramarUF):
        ui_FISCAL_confCFBPProgramarUF.setObjectName("ui_FISCAL_confCFBPProgramarUF")
        ui_FISCAL_confCFBPProgramarUF.resize(211, 114)
        ui_FISCAL_confCFBPProgramarUF.setMinimumSize(QtCore.QSize(211, 114))
        ui_FISCAL_confCFBPProgramarUF.setMaximumSize(QtCore.QSize(211, 114))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_confCFBPProgramarUF)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_confCFBPProgramarUF)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditUF = QtGui.QLineEdit(ui_FISCAL_confCFBPProgramarUF)
        self.lineEditUF.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lineEditUF.setObjectName("lineEditUF")
        self.horizontalLayout_2.addWidget(self.lineEditUF)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_confCFBPProgramarUF)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_confCFBPProgramarUF)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_confCFBPProgramarUF)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_confCFBPProgramarUF)

    def retranslateUi(self, ui_FISCAL_confCFBPProgramarUF):
        ui_FISCAL_confCFBPProgramarUF.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_confCFBPProgramarUF", "Método confCFBPProgramarUF_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_confCFBPProgramarUF", "UF Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditUF.setText(QtGui.QApplication.translate("ui_FISCAL_confCFBPProgramarUF", "SP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_confCFBPProgramarUF", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_confCFBPProgramarUF", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

