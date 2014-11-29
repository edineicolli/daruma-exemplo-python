# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfidentificarconsumidor.ui'
#
# Created: Mon Nov 24 22:25:46 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFIdentificarConsumidor(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFIdentificarConsumidor, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFIdentificarConsumidor):
        ui_FISCAL_iCFIdentificarConsumidor.setObjectName("ui_FISCAL_iCFIdentificarConsumidor")
        ui_FISCAL_iCFIdentificarConsumidor.resize(255, 143)
        ui_FISCAL_iCFIdentificarConsumidor.setMinimumSize(QtCore.QSize(255, 143))
        ui_FISCAL_iCFIdentificarConsumidor.setMaximumSize(QtCore.QSize(255, 143))
        self.layoutWidget = QtGui.QWidget(ui_FISCAL_iCFIdentificarConsumidor)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 90, 247, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layoutWidget_2 = QtGui.QWidget(ui_FISCAL_iCFIdentificarConsumidor)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 247, 74))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtGui.QLabel(self.layoutWidget_2)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEditNome = QtGui.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNome.sizePolicy().hasHeightForWidth())
        self.lineEditNome.setSizePolicy(sizePolicy)
        self.lineEditNome.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEditNome.setMaxLength(255)
        self.lineEditNome.setCursorPosition(0)
        self.lineEditNome.setObjectName("lineEditNome")
        self.gridLayout.addWidget(self.lineEditNome, 0, 1, 1, 1)
        self.label_endereco = QtGui.QLabel(self.layoutWidget_2)
        self.label_endereco.setObjectName("label_endereco")
        self.gridLayout.addWidget(self.label_endereco, 1, 0, 1, 1)
        self.lineEditEndereco = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.gridLayout.addWidget(self.lineEditEndereco, 1, 1, 1, 1)
        self.label_cpf = QtGui.QLabel(self.layoutWidget_2)
        self.label_cpf.setObjectName("label_cpf")
        self.gridLayout.addWidget(self.label_cpf, 2, 0, 1, 1)
        self.lineEditCPF = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.gridLayout.addWidget(self.lineEditCPF, 2, 1, 1, 1)

        self.retranslateUi(ui_FISCAL_iCFIdentificarConsumidor)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFIdentificarConsumidor)

    def retranslateUi(self, ui_FISCAL_iCFIdentificarConsumidor):
        ui_FISCAL_iCFIdentificarConsumidor.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "iCFIdentificarConsumidor_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nome.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNome.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "Daruma Developers Community", None, QtGui.QApplication.UnicodeUTF8))
        self.label_endereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "Endereço:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEndereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "Shishima Hifumi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cpf.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "CPF:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCPF.setText(QtGui.QApplication.translate("ui_FISCAL_iCFIdentificarConsumidor", "111.111.111-11", None, QtGui.QApplication.UnicodeUTF8))

