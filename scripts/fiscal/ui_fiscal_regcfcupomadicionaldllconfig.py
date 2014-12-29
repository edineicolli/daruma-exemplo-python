# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_regcfcupomadicionaldllconfig.ui'
#
# Created: Mon Nov 24 22:26:19 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import regCFCupomAdicionalDllConfig_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_regCFCupomAdicionalDllConfig(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_regCFCupomAdicionalDllConfig, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrValor = self.lineEditValor.text()

        tratarRetornoFiscal(regCFCupomAdicionalDllConfig_ECF_Daruma(StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_regCFCupomAdicionalDllConfig):
        ui_FISCAL_regCFCupomAdicionalDllConfig.setObjectName("ui_FISCAL_regCFCupomAdicionalDllConfig")
        ui_FISCAL_regCFCupomAdicionalDllConfig.resize(248, 133)
        ui_FISCAL_regCFCupomAdicionalDllConfig.setMaximumSize(QtCore.QSize(248, 133))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_regCFCupomAdicionalDllConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(ui_FISCAL_regCFCupomAdicionalDllConfig)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_regCFCupomAdicionalDllConfig)
        self.lineEditValor.setMaximumSize(QtCore.QSize(141, 20))
        self.lineEditValor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditValor.setAutoFillBackground(False)
        self.lineEditValor.setMaxLength(21)
        self.lineEditValor.setFrame(True)
        self.lineEditValor.setCursorPosition(1)
        self.lineEditValor.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditValor.setDragEnabled(False)
        self.lineEditValor.setReadOnly(False)
        self.lineEditValor.setObjectName("lineEditValor")
        self.gridLayout.addWidget(self.lineEditValor, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_regCFCupomAdicionalDllConfig)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_regCFCupomAdicionalDllConfig)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_regCFCupomAdicionalDllConfig)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_regCFCupomAdicionalDllConfig)

    def retranslateUi(self, ui_FISCAL_regCFCupomAdicionalDllConfig):
        ui_FISCAL_regCFCupomAdicionalDllConfig.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_regCFCupomAdicionalDllConfig", "Método regCFCupomAdicionalDllConfig_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_regCFCupomAdicionalDllConfig", "Entre com os valores das configurações:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_regCFCupomAdicionalDllConfig", "111111111111111111111", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_regCFCupomAdicionalDllConfig", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_regCFCupomAdicionalDllConfig", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

