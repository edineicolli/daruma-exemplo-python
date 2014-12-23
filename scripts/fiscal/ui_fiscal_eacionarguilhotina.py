# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_eacionarguilhotina.ui'
#
# Created: Mon Nov 24 22:25:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import eAcionarGuilhotina_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_eAcionarGuilhotina(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eAcionarGuilhotina, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        if (self.radioButtonCParcial.isChecked()):
            StrTipoCorte = "1"
            tratarRetornoFiscal(eAcionarGuilhotina_ECF_Daruma(StrTipoCorte), self)

        if (self.radioButtonCTotal.isChecked()):
            StrTipoCorte = "0"
            tratarRetornoFiscal(eAcionarGuilhotina_ECF_Daruma(StrTipoCorte), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_eAcionarGuilhotina):
        ui_FISCAL_eAcionarGuilhotina.setObjectName("ui_FISCAL_eAcionarGuilhotina")
        ui_FISCAL_eAcionarGuilhotina.resize(225, 126)
        ui_FISCAL_eAcionarGuilhotina.setMinimumSize(QtCore.QSize(225, 126))
        ui_FISCAL_eAcionarGuilhotina.setMaximumSize(QtCore.QSize(225, 126))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_eAcionarGuilhotina)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_eAcionarGuilhotina)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonCParcial = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCParcial.setObjectName("radioButtonCParcial")
        self.verticalLayout.addWidget(self.radioButtonCParcial)
        self.radioButtonCTotal = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCTotal.setObjectName("radioButtonCTotal")
        self.verticalLayout.addWidget(self.radioButtonCTotal)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eAcionarGuilhotina)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_3.addWidget(self.pushButtonEnviar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eAcionarGuilhotina)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_3.addWidget(self.pushButtonCancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ui_FISCAL_eAcionarGuilhotina)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eAcionarGuilhotina)

    def retranslateUi(self, ui_FISCAL_eAcionarGuilhotina):
        ui_FISCAL_eAcionarGuilhotina.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eAcionarGuilhotina", "Método eAcionarGuilhotina_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_eAcionarGuilhotina", "Configuração Guilhotina:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCParcial.setText(QtGui.QApplication.translate("ui_FISCAL_eAcionarGuilhotina", "Corte Parcial", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCTotal.setText(QtGui.QApplication.translate("ui_FISCAL_eAcionarGuilhotina", "Corte Total", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eAcionarGuilhotina", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eAcionarGuilhotina", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

