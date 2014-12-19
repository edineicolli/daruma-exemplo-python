# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_configuracaocupommania.ui'
#
# Created: Mon Nov 24 22:25:22 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import regAlterarValor_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_ConfiguracaoCupomMania(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_ConfiguracaoCupomMania, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        iIndice = self.comboBoxValor.currentIndex()

        if(iIndice == 0 ):
            StrValor = "0"
            tratarRetornoFiscal(regAlterarValor_Daruma("ECF\\CF\\CupomMania",StrValor), self)

        if(iIndice == 1 ):
            StrValor = "1"
            tratarRetornoFiscal(regAlterarValor_Daruma("ECF\\CF\\CupomMania",StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_ConfiguracaoCupomMania):
        ui_FISCAL_ConfiguracaoCupomMania.setObjectName("ui_FISCAL_ConfiguracaoCupomMania")
        ui_FISCAL_ConfiguracaoCupomMania.resize(291, 117)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_ConfiguracaoCupomMania)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelChave = QtGui.QLabel(ui_FISCAL_ConfiguracaoCupomMania)
        self.labelChave.setObjectName("labelChave")
        self.gridLayout.addWidget(self.labelChave, 0, 0, 1, 1)
        self.lineEditChave = QtGui.QLineEdit(ui_FISCAL_ConfiguracaoCupomMania)
        self.lineEditChave.setObjectName("lineEditChave")
        self.gridLayout.addWidget(self.lineEditChave, 0, 1, 1, 1)
        self.labelValor = QtGui.QLabel(ui_FISCAL_ConfiguracaoCupomMania)
        self.labelValor.setObjectName("labelValor")
        self.gridLayout.addWidget(self.labelValor, 1, 0, 1, 1)
        self.comboBoxValor = QtGui.QComboBox(ui_FISCAL_ConfiguracaoCupomMania)
        self.comboBoxValor.setObjectName("comboBoxValor")
        self.comboBoxValor.addItem("")
        self.comboBoxValor.addItem("")
        self.gridLayout.addWidget(self.comboBoxValor, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_ConfiguracaoCupomMania)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_ConfiguracaoCupomMania)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(ui_FISCAL_ConfiguracaoCupomMania)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_ConfiguracaoCupomMania)

    def retranslateUi(self, ui_FISCAL_ConfiguracaoCupomMania):
        ui_FISCAL_ConfiguracaoCupomMania.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "Configuraçao de Cupom Mania", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChave.setText(QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "Chave:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditChave.setText(QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "ECF\\CF\\CupomMania", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxValor.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "0 - Desabilitado", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxValor.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "1 - Habilitado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_ConfiguracaoCupomMania", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

