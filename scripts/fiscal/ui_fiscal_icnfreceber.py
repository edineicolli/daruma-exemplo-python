# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfreceber.ui'
#
# Created: Mon Nov 24 22:25:59 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCNFReceber(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFReceber, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCNFReceber):
        ui_FISCAL_iCNFReceber.setObjectName("ui_FISCAL_iCNFReceber")
        ui_FISCAL_iCNFReceber.resize(318, 158)
        ui_FISCAL_iCNFReceber.setMinimumSize(QtCore.QSize(318, 158))
        ui_FISCAL_iCNFReceber.setMaximumSize(QtCore.QSize(318, 158))
        self.widget = QtGui.QWidget(ui_FISCAL_iCNFReceber)
        self.widget.setGeometry(QtCore.QRect(20, 10, 289, 100))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxIndiceTotalizador = QtGui.QComboBox(self.widget)
        self.comboBoxIndiceTotalizador.setObjectName("comboBoxIndiceTotalizador")
        self.comboBoxIndiceTotalizador.addItem("")
        self.comboBoxIndiceTotalizador.addItem("")
        self.comboBoxIndiceTotalizador.addItem("")
        self.comboBoxIndiceTotalizador.addItem("")
        self.gridLayout.addWidget(self.comboBoxIndiceTotalizador, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditValorRecebimento = QtGui.QLineEdit(self.widget)
        self.lineEditValorRecebimento.setObjectName("lineEditValorRecebimento")
        self.gridLayout.addWidget(self.lineEditValorRecebimento, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditValorAcresDesc = QtGui.QLineEdit(self.widget)
        self.lineEditValorAcresDesc.setObjectName("lineEditValorAcresDesc")
        self.gridLayout.addWidget(self.lineEditValorAcresDesc, 3, 1, 1, 1)
        self.comboBoxTipoAcresDesc = QtGui.QComboBox(self.widget)
        self.comboBoxTipoAcresDesc.setObjectName("comboBoxTipoAcresDesc")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.gridLayout.addWidget(self.comboBoxTipoAcresDesc, 2, 1, 1, 1)
        self.widget1 = QtGui.QWidget(ui_FISCAL_iCNFReceber)
        self.widget1.setGeometry(QtCore.QRect(10, 120, 296, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(self.widget1)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(self.widget1)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(ui_FISCAL_iCNFReceber)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFReceber)
        ui_FISCAL_iCNFReceber.setTabOrder(self.comboBoxIndiceTotalizador, self.lineEditValorRecebimento)
        ui_FISCAL_iCNFReceber.setTabOrder(self.lineEditValorRecebimento, self.comboBoxTipoAcresDesc)
        ui_FISCAL_iCNFReceber.setTabOrder(self.comboBoxTipoAcresDesc, self.lineEditValorAcresDesc)
        ui_FISCAL_iCNFReceber.setTabOrder(self.lineEditValorAcresDesc, self.pushButtonEnviar)
        ui_FISCAL_iCNFReceber.setTabOrder(self.pushButtonEnviar, self.pushButtonCancelar)

    def retranslateUi(self, ui_FISCAL_iCNFReceber):
        ui_FISCAL_iCNFReceber.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Método iCNFReceber_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Indice do Totalizador:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "03", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "04", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxIndiceTotalizador.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "05", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Tipo de Acréscimo / Desconto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Valor do Acréscimo / Desconto:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "A$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "A%", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "D$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(4, QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "D%", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFReceber", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

