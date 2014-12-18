# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_confcadastrarpadrao.ui'
#
# Created: Mon Nov 24 22:25:20 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import confCadastrarPadrao_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_confCadastrarPadrao(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_confCadastrarPadrao, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        if ((self.comboBoxTipo.currentIndex()== 0 ) and (self.lineEditValor.text()=="")):
            QMessageBox.warning(self, "DarumaFramework - Qt/Python","Preencha todos os Campos!")
        else:
            StrTipo = self.comboBoxTipo.currentText()
            StrValor = self.lineEditValor.text()

            tratarRetornoFiscal(confCadastrarPadrao_ECF_Daruma(StrTipo, StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_confCadastrarPadrao):
        ui_FISCAL_confCadastrarPadrao.setObjectName("ui_FISCAL_confCadastrarPadrao")
        ui_FISCAL_confCadastrarPadrao.resize(194, 155)
        ui_FISCAL_confCadastrarPadrao.setMinimumSize(QtCore.QSize(194, 155))
        ui_FISCAL_confCadastrarPadrao.setMaximumSize(QtCore.QSize(194, 155))
        self.verticalLayout_4 = QtGui.QVBoxLayout(ui_FISCAL_confCadastrarPadrao)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(ui_FISCAL_confCadastrarPadrao)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBoxTipo = QtGui.QComboBox(ui_FISCAL_confCadastrarPadrao)
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.verticalLayout_3.addWidget(self.comboBoxTipo)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_confCadastrarPadrao)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_confCadastrarPadrao)
        self.lineEditValor.setObjectName("lineEditValor")
        self.verticalLayout.addWidget(self.lineEditValor)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_confCadastrarPadrao)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_4.addWidget(self.pushButtonEnviar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_confCadastrarPadrao)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_4.addWidget(self.pushButtonCancelar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(ui_FISCAL_confCadastrarPadrao)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_confCadastrarPadrao)

    def retranslateUi(self, ui_FISCAL_confCadastrarPadrao):
        ui_FISCAL_confCadastrarPadrao.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "Método confCadastrarPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "Tipo Cadastro:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "ALIQUOTA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "GERENCIAL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "TNF", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(4, QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "FPGTO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "Valor para Cadastro:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "07,00;12,00;17,00;25,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "Cadastrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrarPadrao", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

