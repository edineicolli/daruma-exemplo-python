# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_ersaassinararquivo.ui'
#
# Created: Mon Nov 24 22:25:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_eRSAAssinarArquivo(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eRSAAssinarArquivo, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_eRSAAssinarArquivo):
        ui_FISCAL_eRSAAssinarArquivo.setObjectName("ui_FISCAL_eRSAAssinarArquivo")
        ui_FISCAL_eRSAAssinarArquivo.resize(363, 174)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_eRSAAssinarArquivo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_eRSAAssinarArquivo)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditCaminhoArq = QtGui.QLineEdit(self.groupBox)
        self.lineEditCaminhoArq.setObjectName("lineEditCaminhoArq")
        self.gridLayout.addWidget(self.lineEditCaminhoArq, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEditCaminhoKey = QtGui.QLineEdit(self.groupBox)
        self.lineEditCaminhoKey.setObjectName("lineEditCaminhoKey")
        self.gridLayout.addWidget(self.lineEditCaminhoKey, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eRSAAssinarArquivo)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eRSAAssinarArquivo)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_eRSAAssinarArquivo)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eRSAAssinarArquivo)

    def retranslateUi(self, ui_FISCAL_eRSAAssinarArquivo):
        ui_FISCAL_eRSAAssinarArquivo.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eRSAAssinarArquivo", "Método eRSAAssinarArquivo_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_eRSAAssinarArquivo", "Assinatura de Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eRSAAssinarArquivo", "Caminho completo do arquivo a ser assinado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_eRSAAssinarArquivo", "Caminho completo da chave .key:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eRSAAssinarArquivo", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eRSAAssinarArquivo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

