# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfencerrarconfigmsg.ui'
#
# Created: Mon Nov 24 22:25:44 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFEncerrarConfigMsg(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFEncerrarConfigMsg, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFEncerrarConfigMsg):
        ui_FISCAL_iCFEncerrarConfigMsg.setObjectName("ui_FISCAL_iCFEncerrarConfigMsg")
        ui_FISCAL_iCFEncerrarConfigMsg.resize(535, 117)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFEncerrarConfigMsg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelInformacao = QtGui.QLabel(ui_FISCAL_iCFEncerrarConfigMsg)
        self.labelInformacao.setObjectName("labelInformacao")
        self.gridLayout.addWidget(self.labelInformacao, 0, 0, 1, 1)
        self.lineEditMensagem = QtGui.QLineEdit(ui_FISCAL_iCFEncerrarConfigMsg)
        self.lineEditMensagem.setMinimumSize(QtCore.QSize(401, 20))
        self.lineEditMensagem.setMaxLength(384)
        self.lineEditMensagem.setObjectName("lineEditMensagem")
        self.gridLayout.addWidget(self.lineEditMensagem, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFEncerrarConfigMsg)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFEncerrarConfigMsg)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFEncerrarConfigMsg)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFEncerrarConfigMsg)

    def retranslateUi(self, ui_FISCAL_iCFEncerrarConfigMsg):
        ui_FISCAL_iCFEncerrarConfigMsg.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrarConfigMsg", "Método iCFEncerrarConfigMsg_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInformacao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrarConfigMsg", "Informação Adicional:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrarConfigMsg", "Mensagem Promocial com até 384 caracteres com formatação!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrarConfigMsg", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrarConfigMsg", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

