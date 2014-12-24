# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_ecarregarbitmappromocional.ui'
#
# Created: Mon Nov 24 22:25:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import eCarregarBitmapPromocional_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_eCarregarBitmapPromocional(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eCarregarBitmapPromocional, self).__init__()

        self.setupUi(self)
        self.comboBoxIndice.addItem(" ")
        self.comboBoxIndice.addItem("1")
        self.comboBoxIndice.addItem("2")
        self.comboBoxIndice.addItem("3")
        self.comboBoxIndice.addItem("4")
        self.comboBoxIndice.addItem("5")
        self.lineEditOrientacao.setText("000")
        self.lineEditPath.setText("C:\\Logo.bmp")
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrIndice = self.comboBoxIndice.currentText()
        StrPath = self.lineEditPath.text()

        # Chamada do Método
        tratarRetornoFiscal(eCarregarBitmapPromocional_ECF_Daruma(StrPath,StrIndice,"000"), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_eCarregarBitmapPromocional):
        ui_FISCAL_eCarregarBitmapPromocional.setObjectName("ui_FISCAL_eCarregarBitmapPromocional")
        ui_FISCAL_eCarregarBitmapPromocional.resize(243, 103)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_eCarregarBitmapPromocional)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_eCarregarBitmapPromocional)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditPath = QtGui.QLineEdit(ui_FISCAL_eCarregarBitmapPromocional)
        self.lineEditPath.setText("")
        self.lineEditPath.setObjectName("lineEditPath")
        self.gridLayout_2.addWidget(self.lineEditPath, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtGui.QLabel(ui_FISCAL_eCarregarBitmapPromocional)
        self.label_2.setMinimumSize(QtCore.QSize(46, 13))
        self.label_2.setMaximumSize(QtCore.QSize(46, 13))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBoxIndice = QtGui.QComboBox(ui_FISCAL_eCarregarBitmapPromocional)
        self.comboBoxIndice.setMinimumSize(QtCore.QSize(41, 22))
        self.comboBoxIndice.setMaximumSize(QtCore.QSize(41, 22))
        self.comboBoxIndice.setObjectName("comboBoxIndice")
        self.gridLayout_3.addWidget(self.comboBoxIndice, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(ui_FISCAL_eCarregarBitmapPromocional)
        self.label_3.setMinimumSize(QtCore.QSize(57, 20))
        self.label_3.setMaximumSize(QtCore.QSize(57, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditOrientacao = QtGui.QLineEdit(ui_FISCAL_eCarregarBitmapPromocional)
        self.lineEditOrientacao.setMinimumSize(QtCore.QSize(31, 20))
        self.lineEditOrientacao.setMaximumSize(QtCore.QSize(31, 20))
        self.lineEditOrientacao.setText("")
        self.lineEditOrientacao.setObjectName("lineEditOrientacao")
        self.gridLayout.addWidget(self.lineEditOrientacao, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eCarregarBitmapPromocional)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eCarregarBitmapPromocional)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_eCarregarBitmapPromocional)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eCarregarBitmapPromocional)

    def retranslateUi(self, ui_FISCAL_eCarregarBitmapPromocional):
        ui_FISCAL_eCarregarBitmapPromocional.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eCarregarBitmapPromocional", "Método eCarregarBitmapPromocional_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eCarregarBitmapPromocional", "Local Bitmap:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_eCarregarBitmapPromocional", "Índice:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_eCarregarBitmapPromocional", "Orientaçao:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eCarregarBitmapPromocional", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eCarregarBitmapPromocional", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

