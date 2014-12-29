# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rleituraxcustomizada.ui'
#
# Created: Mon Nov 24 22:26:30 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rLeituraXCustomizada(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rLeituraXCustomizada, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        pass

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rLeituraXCustomizada):
        ui_FISCAL_rLeituraXCustomizada.setObjectName("ui_FISCAL_rLeituraXCustomizada")
        ui_FISCAL_rLeituraXCustomizada.resize(227, 96)
        ui_FISCAL_rLeituraXCustomizada.setMinimumSize(QtCore.QSize(227, 96))
        ui_FISCAL_rLeituraXCustomizada.setMaximumSize(QtCore.QSize(227, 96))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_rLeituraXCustomizada)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_rLeituraXCustomizada)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditCaminho = QtGui.QLineEdit(ui_FISCAL_rLeituraXCustomizada)
        self.lineEditCaminho.setObjectName("lineEditCaminho")
        self.verticalLayout.addWidget(self.lineEditCaminho)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rLeituraXCustomizada)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rLeituraXCustomizada)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rLeituraXCustomizada)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rLeituraXCustomizada)

    def retranslateUi(self, ui_FISCAL_rLeituraXCustomizada):
        ui_FISCAL_rLeituraXCustomizada.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rLeituraXCustomizada", "Método rLeituraXCustomizada_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rLeituraXCustomizada", "Caminho para Gravação:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminho.setText(QtGui.QApplication.translate("ui_FISCAL_rLeituraXCustomizada", "C:\\Daruma\\LeituraX.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rLeituraXCustomizada", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rLeituraXCustomizada", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

