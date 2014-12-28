# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iimprimircodigobarras.ui'
#
# Created: Mon Nov 24 22:26:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iImprimirCodigoBarras_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iImprimirCodigoBarras(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iImprimirCodigoBarras, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)
        # insere valores na combobox dos Tipos de Cod de Barras
        self.comboBoxTipo.addItem("Veja lista completa ao lado")
        self.comboBoxTipo.addItem("EAN-13")
        self.comboBoxTipo.addItem("EAN-8")
        self.comboBoxTipo.addItem("STANDARD 2 OF 5")
        self.comboBoxTipo.addItem("INTERVEALED 2 OF 5")
        self.comboBoxTipo.addItem("CODE128")
        self.comboBoxTipo.addItem("CODE39")
        self.comboBoxTipo.addItem("CODE93")
        self.comboBoxTipo.addItem("UPC-A")
        self.comboBoxTipo.addItem("CODABAR")
        self.comboBoxTipo.addItem("MSI")
        self.comboBoxTipo.addItem("CODE11")

        #Insere valores na Altura e Largura
        add = ""
        for a in range(2,5):
            add += str(a)
            self.comboBoxAltura.addItem(add)
        for b in (50,200):
            add += str(b)
            self.comboBoxLargura.addItem(add)

        self.lineEditCodBarras.setText("0123456789012")
        self.textEditTextoLivre.setText("Texto com até 600 caracteres!")

    def on_pushButtonEnviar_clicked(self):
        iTipo = self.comboBoxTipo.currentIndex()
        StrLargura = self.comboBoxLargura.currentText()
        StrAltura = self.comboBoxAltura.currentText()
        StrTextoLivre = self.textEditTextoLivre.toPlainText()
        StrCodBarras = self.lineEditCodBarras.text()

        #convertendo o Inteiro do Tipo do Codigo de barras para QString, e de QString para string.
        StrTipo = iTipo.toString()

        StrTextAbaixo = "0"
        StrVertical = "h"
        if ((self.checkBoxTextAbaixo.isChecked()) and (self.checkBoxVertical.isChecked())):
            StrTextAbaixo = "1"
            StrVertical = "v"
            tratarRetornoFiscal(iImprimirCodigoBarras_ECF_Daruma(StrTipo,StrLargura,StrAltura,StrTextAbaixo,StrCodBarras,StrVertical,StrTextoLivre), self)
        elif ((self.checkBoxTextAbaixo.isChecked())):
            StrTextAbaixo = "1"
            StrVertical = "h"
            tratarRetornoFiscal(iImprimirCodigoBarras_ECF_Daruma(StrTipo,StrLargura,StrAltura,StrTextAbaixo,StrCodBarras,StrVertical,StrTextoLivre), self)
        elif ((self.checkBoxVertical.isChecked())):
            StrTextAbaixo = "0"
            StrVertical = "v"
            tratarRetornoFiscal(iImprimirCodigoBarras_ECF_Daruma(StrTipo,StrLargura,StrAltura,StrTextAbaixo,StrCodBarras,StrVertical,StrTextoLivre), self)
        else:
            tratarRetornoFiscal(iImprimirCodigoBarras_ECF_Daruma(StrTipo,StrLargura,StrAltura,StrTextAbaixo,StrCodBarras,StrVertical,StrTextoLivre),this);

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iImprimirCodigoBarras):
        ui_FISCAL_iImprimirCodigoBarras.setObjectName("ui_FISCAL_iImprimirCodigoBarras")
        ui_FISCAL_iImprimirCodigoBarras.resize(554, 331)
        ui_FISCAL_iImprimirCodigoBarras.setMinimumSize(QtCore.QSize(554, 331))
        ui_FISCAL_iImprimirCodigoBarras.setMaximumSize(QtCore.QSize(554, 331))
        self.layoutWidget3 = QtGui.QWidget(ui_FISCAL_iImprimirCodigoBarras)
        self.layoutWidget3.setGeometry(QtCore.QRect(120, 300, 296, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(self.layoutWidget3)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_5.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(self.layoutWidget3)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_5.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.layoutWidget4 = QtGui.QWidget(ui_FISCAL_iImprimirCodigoBarras)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 10, 534, 282))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtGui.QGroupBox(self.layoutWidget4)
        self.groupBox.setMaximumSize(QtCore.QSize(161, 281))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setMaximumSize(QtCore.QSize(118, 17))
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setMaximumSize(QtCore.QSize(141, 17))
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget4)
        self.groupBox_2.setMinimumSize(QtCore.QSize(369, 280))
        self.groupBox_2.setMaximumSize(QtCore.QSize(369, 280))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 351, 132))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.comboBoxTipo = QtGui.QComboBox(self.groupBox_4)
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.horizontalLayout_6.addWidget(self.comboBoxTipo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.lineEditCodBarras = QtGui.QLineEdit(self.groupBox_4)
        self.lineEditCodBarras.setObjectName("lineEditCodBarras")
        self.horizontalLayout_3.addWidget(self.lineEditCodBarras)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.textEditTextoLivre = QtGui.QTextEdit(self.groupBox_4)
        self.textEditTextoLivre.setObjectName("textEditTextoLivre")
        self.horizontalLayout_4.addWidget(self.textEditTextoLivre)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 161, 101))
        self.groupBox_3.setMinimumSize(QtCore.QSize(161, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.comboBoxLargura = QtGui.QComboBox(self.groupBox_3)
        self.comboBoxLargura.setObjectName("comboBoxLargura")
        self.horizontalLayout.addWidget(self.comboBoxLargura)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBoxAltura = QtGui.QComboBox(self.groupBox_3)
        self.comboBoxAltura.setObjectName("comboBoxAltura")
        self.horizontalLayout_2.addWidget(self.comboBoxAltura)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(180, 160, 181, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBoxVertical = QtGui.QCheckBox(self.groupBox_5)
        self.checkBoxVertical.setObjectName("checkBoxVertical")
        self.verticalLayout_4.addWidget(self.checkBoxVertical)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.checkBoxTextAbaixo = QtGui.QCheckBox(self.groupBox_5)
        self.checkBoxTextAbaixo.setObjectName("checkBoxTextAbaixo")
        self.verticalLayout_4.addWidget(self.checkBoxTextAbaixo)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.retranslateUi(ui_FISCAL_iImprimirCodigoBarras)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iImprimirCodigoBarras)

    def retranslateUi(self, ui_FISCAL_iImprimirCodigoBarras):
        ui_FISCAL_iImprimirCodigoBarras.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Códigos de Barra Disponíveis", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "1 - EAN-13", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "2 - EAN-8", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "3 -  STANDARD 2 OF 5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "4 - INTERVEALED 2 OF 5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "5 - CODE128", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "6 - CODE39", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "7 - CODE93", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "8 - UPC-A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "9 - CODABAR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "10 - MSI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "11 - CODE11", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Formatações do Codigo de Barras", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Tipo, Código e Texto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Tipo de Codigo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Código:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Texto Livre:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Tamanho do Código de Barras", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Largura:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Altura:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Outras Configurações", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxVertical.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Impressão na Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxTextAbaixo.setText(QtGui.QApplication.translate("ui_FISCAL_iImprimirCodigoBarras", "Impressão do Código", None, QtGui.QApplication.UnicodeUTF8))

