# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfabrir.ui'
#
# Created: Mon Nov 24 22:25:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFAbrir_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFAbrir(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFAbrir, self).__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)

    def on_pushButton_clicked(self):
        # Declaraçao das Variaveis que recebem os valores da UI
        StrCPF =  self.lineEditCPF.text()
        StrNome = self.lineEditNome.text()
        StrEndereco =  self.lineEditEndereco.text()

        # Chamada do Método
        tratarRetornoFiscal(iCFAbrir_ECF_Daruma(StrCPF,StrNome,StrEndereco), self)

    def on_pushButton_2_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFAbrir):
        ui_FISCAL_iCFAbrir.setObjectName("ui_FISCAL_iCFAbrir")
        ui_FISCAL_iCFAbrir.setWindowModality(QtCore.Qt.NonModal)
        ui_FISCAL_iCFAbrir.resize(263, 153)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_FISCAL_iCFAbrir.sizePolicy().hasHeightForWidth())
        ui_FISCAL_iCFAbrir.setSizePolicy(sizePolicy)
        ui_FISCAL_iCFAbrir.setMinimumSize(QtCore.QSize(263, 153))
        ui_FISCAL_iCFAbrir.setMaximumSize(QtCore.QSize(263, 153))
        self.label_nome = QtGui.QLabel(ui_FISCAL_iCFAbrir)
        self.label_nome.setGeometry(QtCore.QRect(11, 11, 31, 16))
        self.label_nome.setObjectName("label_nome")
        self.label_cpf = QtGui.QLabel(ui_FISCAL_iCFAbrir)
        self.label_cpf.setGeometry(QtCore.QRect(11, 67, 23, 16))
        self.label_cpf.setObjectName("label_cpf")
        self.label_endereco = QtGui.QLabel(ui_FISCAL_iCFAbrir)
        self.label_endereco.setGeometry(QtCore.QRect(11, 39, 49, 16))
        self.label_endereco.setObjectName("label_endereco")
        self.layoutWidget = QtGui.QWidget(ui_FISCAL_iCFAbrir)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 250, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEditNome = QtGui.QLineEdit(ui_FISCAL_iCFAbrir)
        self.lineEditNome.setGeometry(QtCore.QRect(87, 12, 161, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNome.sizePolicy().hasHeightForWidth())
        self.lineEditNome.setSizePolicy(sizePolicy)
        self.lineEditNome.setMaxLength(255)
        self.lineEditNome.setCursorPosition(0)
        self.lineEditNome.setObjectName("lineEditNome")
        self.lineEditEndereco = QtGui.QLineEdit(ui_FISCAL_iCFAbrir)
        self.lineEditEndereco.setGeometry(QtCore.QRect(87, 38, 161, 20))
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.lineEditCPF = QtGui.QLineEdit(ui_FISCAL_iCFAbrir)
        self.lineEditCPF.setGeometry(QtCore.QRect(87, 64, 91, 20))
        self.lineEditCPF.setObjectName("lineEditCPF")

        self.retranslateUi(ui_FISCAL_iCFAbrir)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFAbrir)

    def retranslateUi(self, ui_FISCAL_iCFAbrir):
        ui_FISCAL_iCFAbrir.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "iCFAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nome.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cpf.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "CPF:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_endereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "Endereço:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "Abrir CF", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNome.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "Daruma Developers Community", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEndereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "Shishima Hifumi", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCPF.setText(QtGui.QApplication.translate("ui_FISCAL_iCFAbrir", "111.111.111-11", None, QtGui.QApplication.UnicodeUTF8))

