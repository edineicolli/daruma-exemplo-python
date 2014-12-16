# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_confcadastrar.ui'
#
# Created: Mon Nov 24 22:25:19 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import confCadastrar_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_confCadastrar(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_confCadastrar, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)


    def on_pushButtonEnviar_clicked(self):
        if ((self.comboBoxTipo.currentIndex() == 0 ) and (self.lineEditValor.text() == "") and (self.lineEditSeparador.text() == "")):
            QMessageBox.warning(self, "DarumaFramework - Qt/Python","Preencha todos os Campos!")
        else:
            StrTipo = self.comboBoxTipo.currentText()
            StrValor = self.lineEditValor.text()
            StrSeparador = self.lineEditSeparador.text()
            tratarRetornoFiscal(confCadastrar_ECF_Daruma(StrTipo,StrValor,StrSeparador), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_confCadastrar):
        ui_FISCAL_confCadastrar.setObjectName("ui_FISCAL_confCadastrar")
        ui_FISCAL_confCadastrar.resize(194, 221)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_FISCAL_confCadastrar.sizePolicy().hasHeightForWidth())
        ui_FISCAL_confCadastrar.setSizePolicy(sizePolicy)
        ui_FISCAL_confCadastrar.setMinimumSize(QtCore.QSize(194, 221))
        ui_FISCAL_confCadastrar.setMaximumSize(QtCore.QSize(194, 221))
        self.verticalLayout_4 = QtGui.QVBoxLayout(ui_FISCAL_confCadastrar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(ui_FISCAL_confCadastrar)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBoxTipo = QtGui.QComboBox(ui_FISCAL_confCadastrar)
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.verticalLayout_3.addWidget(self.comboBoxTipo)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 4, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(ui_FISCAL_confCadastrar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_confCadastrar)
        self.lineEditValor.setObjectName("lineEditValor")
        self.verticalLayout.addWidget(self.lineEditValor)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_3 = QtGui.QLabel(ui_FISCAL_confCadastrar)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.lineEditSeparador = QtGui.QLineEdit(ui_FISCAL_confCadastrar)
        self.lineEditSeparador.setMaximumSize(QtCore.QSize(31, 20))
        self.lineEditSeparador.setMaxLength(1)
        self.lineEditSeparador.setObjectName("lineEditSeparador")
        self.horizontalLayout_2.addWidget(self.lineEditSeparador)
        spacerItem8 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_confCadastrar)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_4.addWidget(self.pushButtonEnviar)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_confCadastrar)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_4.addWidget(self.pushButtonCancelar)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(ui_FISCAL_confCadastrar)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_confCadastrar)

    def retranslateUi(self, ui_FISCAL_confCadastrar):
        ui_FISCAL_confCadastrar.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Método confCadastrar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Tipo Cadastro:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "ALIQUOTA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "GERENCIAL", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "TNF", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipo.setItemText(4, QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "FPGTO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Valor para Cadastro:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValor.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "07,00;12,00;17,00;25,00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Separador:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSeparador.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", ";", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Cadastrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_confCadastrar", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

