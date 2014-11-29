# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_edefinirproduto.ui'
#
# Created: Mon Nov 24 22:25:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_eDefinirProduto(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eDefinirProduto, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_eDefinirProduto):
        ui_FISCAL_eDefinirProduto.setObjectName("ui_FISCAL_eDefinirProduto")
        ui_FISCAL_eDefinirProduto.resize(278, 144)
        ui_FISCAL_eDefinirProduto.setMinimumSize(QtCore.QSize(278, 144))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_eDefinirProduto)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_eDefinirProduto)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_eDefinirProduto)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonECF = QtGui.QRadioButton(self.groupBox)
        self.radioButtonECF.setObjectName("radioButtonECF")
        self.gridLayout.addWidget(self.radioButtonECF, 0, 0, 1, 1)
        self.radioButtonDUAL = QtGui.QRadioButton(self.groupBox)
        self.radioButtonDUAL.setObjectName("radioButtonDUAL")
        self.gridLayout.addWidget(self.radioButtonDUAL, 0, 1, 1, 1)
        self.radioButtonMODEM = QtGui.QRadioButton(self.groupBox)
        self.radioButtonMODEM.setObjectName("radioButtonMODEM")
        self.gridLayout.addWidget(self.radioButtonMODEM, 1, 0, 1, 1)
        self.radioButtonTA2000 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonTA2000.setObjectName("radioButtonTA2000")
        self.gridLayout.addWidget(self.radioButtonTA2000, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eDefinirProduto)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eDefinirProduto)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_eDefinirProduto)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eDefinirProduto)

    def retranslateUi(self, ui_FISCAL_eDefinirProduto):
        ui_FISCAL_eDefinirProduto.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "Método eDefinirProduto_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Escolha o produto que você deseja trabalhar:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonECF.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "ECF/FISCAL", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDUAL.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "DUAL", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonMODEM.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "MODEM", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTA2000.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "TA2000", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirProduto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

