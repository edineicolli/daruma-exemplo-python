# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnftotalizarcomprovante.ui'
#
# Created: Mon Nov 24 22:26:00 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCNFTotalizarComprovante_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCNFTotalizarComprovante(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFTotalizarComprovante, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrTipoAcresDesc = self.comboBoxTipoAcresDesc.currentText()
        StrValor = self.lineEditValor.text()
        tratarRetornoFiscal(iCNFTotalizarComprovante_ECF_Daruma(StrTipoAcresDesc, StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCNFTotalizarComprovante):
        ui_FISCAL_iCNFTotalizarComprovante.setObjectName("ui_FISCAL_iCNFTotalizarComprovante")
        ui_FISCAL_iCNFTotalizarComprovante.resize(196, 103)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCNFTotalizarComprovante)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.labelTipoAcresDesc = QtGui.QLabel(ui_FISCAL_iCNFTotalizarComprovante)
        self.labelTipoAcresDesc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTipoAcresDesc.setObjectName("labelTipoAcresDesc")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelTipoAcresDesc)
        self.comboBoxTipoAcresDesc = QtGui.QComboBox(ui_FISCAL_iCNFTotalizarComprovante)
        self.comboBoxTipoAcresDesc.setMinimumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoAcresDesc.setMaximumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoAcresDesc.setObjectName("comboBoxTipoAcresDesc")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.comboBoxTipoAcresDesc.addItem("")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxTipoAcresDesc)
        self.labelValor = QtGui.QLabel(ui_FISCAL_iCNFTotalizarComprovante)
        self.labelValor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValor.setObjectName("labelValor")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelValor)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_iCNFTotalizarComprovante)
        self.lineEditValor.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditValor.setMaxLength(10)
        self.lineEditValor.setObjectName("lineEditValor")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditValor)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCNFTotalizarComprovante)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCNFTotalizarComprovante)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFTotalizarComprovante)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFTotalizarComprovante)

    def retranslateUi(self, ui_FISCAL_iCNFTotalizarComprovante):
        ui_FISCAL_iCNFTotalizarComprovante.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "Método iCNFTotalizarComprovante_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTipoAcresDesc.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "Tipo Acresc/Desc: ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "A$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "A%", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "D$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcresDesc.setItemText(4, QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "D%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFTotalizarComprovante", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

