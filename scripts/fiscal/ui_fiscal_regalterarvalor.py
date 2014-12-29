# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_regalterarvalor.ui'
#
# Created: Mon Nov 24 22:26:18 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import regAlterarValor_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_regAlterarValor(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_regAlterarValor, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.lineEditProdutoChave.setText("ECF\\Auditoria")
        self.lineEditValor.setText("1")

    def on_pushButtonEnviar_clicked(self):
        StrProdutoChave = self.lineEditProdutoChave.text()
        StrValor = self.lineEditValor.text()

        tratarRetornoFiscal(regAlterarValor_Daruma(StrProdutoChave, StrValor), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_regAlterarValor):
        ui_FISCAL_regAlterarValor.setObjectName("ui_FISCAL_regAlterarValor")
        ui_FISCAL_regAlterarValor.resize(307, 125)
        ui_FISCAL_regAlterarValor.setMaximumSize(QtCore.QSize(307, 125))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_regAlterarValor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(ui_FISCAL_regAlterarValor)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEditProdutoChave = QtGui.QLineEdit(ui_FISCAL_regAlterarValor)
        self.lineEditProdutoChave.setObjectName("lineEditProdutoChave")
        self.horizontalLayout_4.addWidget(self.lineEditProdutoChave)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(ui_FISCAL_regAlterarValor)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEditValor = QtGui.QLineEdit(ui_FISCAL_regAlterarValor)
        self.lineEditValor.setObjectName("lineEditValor")
        self.horizontalLayout_3.addWidget(self.lineEditValor)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_regAlterarValor)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_regAlterarValor)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_regAlterarValor)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_regAlterarValor)

    def retranslateUi(self, ui_FISCAL_regAlterarValor):
        ui_FISCAL_regAlterarValor.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_regAlterarValor", "Método regAlterarValor_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_regAlterarValor", "Produto \\ Chave:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_regAlterarValor", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_regAlterarValor", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_regAlterarValor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

