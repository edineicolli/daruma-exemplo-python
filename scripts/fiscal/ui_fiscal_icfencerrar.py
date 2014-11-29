# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfencerrar.ui'
#
# Created: Mon Nov 24 22:25:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFEncerrar(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFEncerrar, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFEncerrar):
        ui_FISCAL_iCFEncerrar.setObjectName("ui_FISCAL_iCFEncerrar")
        ui_FISCAL_iCFEncerrar.resize(359, 300)
        ui_FISCAL_iCFEncerrar.setMinimumSize(QtCore.QSize(359, 300))
        ui_FISCAL_iCFEncerrar.setMaximumSize(QtCore.QSize(359, 300))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFEncerrar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_iCFEncerrar)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBoxAdicional = QtGui.QComboBox(ui_FISCAL_iCFEncerrar)
        self.comboBoxAdicional.setObjectName("comboBoxAdicional")
        self.comboBoxAdicional.addItem("")
        self.comboBoxAdicional.addItem("")
        self.comboBoxAdicional.addItem("")
        self.comboBoxAdicional.addItem("")
        self.comboBoxAdicional.addItem("")
        self.verticalLayout.addWidget(self.comboBoxAdicional)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCFEncerrar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditMensagem = QtGui.QLineEdit(ui_FISCAL_iCFEncerrar)
        self.lineEditMensagem.setMinimumSize(QtCore.QSize(341, 141))
        self.lineEditMensagem.setMaximumSize(QtCore.QSize(341, 141))
        self.lineEditMensagem.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEditMensagem.setObjectName("lineEditMensagem")
        self.verticalLayout.addWidget(self.lineEditMensagem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFEncerrar)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFEncerrar)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFEncerrar)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFEncerrar)

    def retranslateUi(self, ui_FISCAL_iCFEncerrar):
        ui_FISCAL_iCFEncerrar.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "Método iCFEncerrar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "Tipo de Cupom Adicional:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxAdicional.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "Escolha a opção abaixo...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxAdicional.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "0 - Não Imprime Cupom Adicional", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxAdicional.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "1 - Imprime Cupom Adicional Simples", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxAdicional.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "2 - Imprime Cupom Adicional Detalhado", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxAdicional.setItemText(4, QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "3 - Imprime Cupom Adicional DLL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "Mensagem Promocional:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMensagem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "DarumaFramework com Mensagem no Encerramento com até 8 linhas!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFEncerrar", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

