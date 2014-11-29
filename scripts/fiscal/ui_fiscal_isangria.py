# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_isangria.ui'
#
# Created: Mon Nov 24 22:26:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iSangria(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iSangria, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iSangria):
        ui_FISCAL_iSangria.setObjectName("ui_FISCAL_iSangria")
        ui_FISCAL_iSangria.resize(245, 105)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iSangria)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelValor = QtGui.QLabel(ui_FISCAL_iSangria)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 0, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iSangria)
        self.lineEditValor.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 0, 1, 1, 1)
        self.labelMensagem = QtGui.QLabel(ui_FISCAL_iSangria)
        self.labelMensagem.setObjectName("labelMensagem")
        self.gridLayout.addWidget(self.labelMensagem, 1, 0, 1, 1)
        self.lineEditMensagem = QtGui.QLineEdit(ui_FISCAL_iSangria)
        self.lineEditMensagem.setObjectName("lineEditMensagem")
        self.gridLayout.addWidget(self.lineEditMensagem, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iSangria)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iSangria)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iSangria)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iSangria)

    def retranslateUi(self, ui_FISCAL_iSangria):
        ui_FISCAL_iSangria.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iSangria", "Método iSangria_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iSangria", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iSangria", "10,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iSangria", "Mensagem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iSangria", "Retirada para Banco", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iSangria", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iSangria", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

