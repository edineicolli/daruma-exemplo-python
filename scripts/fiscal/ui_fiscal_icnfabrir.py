# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icnfabrir.ui'
#
# Created: Mon Nov 24 22:25:54 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCNFAbrir(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCNFAbrir, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCNFAbrir):
        ui_FISCAL_iCNFAbrir.setObjectName("ui_FISCAL_iCNFAbrir")
        ui_FISCAL_iCNFAbrir.resize(263, 123)
        ui_FISCAL_iCNFAbrir.setMinimumSize(QtCore.QSize(263, 123))
        ui_FISCAL_iCNFAbrir.setMaximumSize(QtCore.QSize(263, 123))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCNFAbrir)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtGui.QLabel(ui_FISCAL_iCNFAbrir)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEditNome = QtGui.QLineEdit(ui_FISCAL_iCNFAbrir)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNome.sizePolicy().hasHeightForWidth())
        self.lineEditNome.setSizePolicy(sizePolicy)
        self.lineEditNome.setMaxLength(255)
        self.lineEditNome.setCursorPosition(27)
        self.lineEditNome.setObjectName("lineEditNome")
        self.gridLayout.addWidget(self.lineEditNome, 0, 1, 1, 1)
        self.label_endereco = QtGui.QLabel(ui_FISCAL_iCNFAbrir)
        self.label_endereco.setObjectName("label_endereco")
        self.gridLayout.addWidget(self.label_endereco, 1, 0, 1, 1)
        self.lineEditEndereco = QtGui.QLineEdit(ui_FISCAL_iCNFAbrir)
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.gridLayout.addWidget(self.lineEditEndereco, 1, 1, 1, 1)
        self.label_cpf = QtGui.QLabel(ui_FISCAL_iCNFAbrir)
        self.label_cpf.setObjectName("label_cpf")
        self.gridLayout.addWidget(self.label_cpf, 2, 0, 1, 1)
        self.lineEditCPF = QtGui.QLineEdit(ui_FISCAL_iCNFAbrir)
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.gridLayout.addWidget(self.lineEditCPF, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(ui_FISCAL_iCNFAbrir)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(ui_FISCAL_iCNFAbrir)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCNFAbrir)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCNFAbrir)

    def retranslateUi(self, ui_FISCAL_iCNFAbrir):
        ui_FISCAL_iCNFAbrir.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Método iCNFAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nome.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNome.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Daruma Developers Community", None, QtGui.QApplication.UnicodeUTF8))
        self.label_endereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Endereço:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEndereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Shishima Hifumi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cpf.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "CPF:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCPF.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "111.111.111-11", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Abrir CNF", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCNFAbrir", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

