# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_iccdestornar.ui'
#
# Created: Mon Nov 24 22:25:33 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCCDEstornar(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCCDEstornar, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCCDEstornar):
        ui_FISCAL_iCCDEstornar.setObjectName("ui_FISCAL_iCCDEstornar")
        ui_FISCAL_iCCDEstornar.resize(278, 247)
        self.layoutWidget = QtGui.QWidget(ui_FISCAL_iCCDEstornar)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 153, 250, 25))
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
        self.widget = QtGui.QWidget(ui_FISCAL_iCCDEstornar)
        self.widget.setGeometry(QtCore.QRect(10, 40, 232, 100))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome_2 = QtGui.QLabel(self.widget)
        self.label_nome_2.setObjectName("label_nome_2")
        self.gridLayout.addWidget(self.label_nome_2, 0, 0, 1, 1)
        self.lineEditDocOrigem = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDocOrigem.sizePolicy().hasHeightForWidth())
        self.lineEditDocOrigem.setSizePolicy(sizePolicy)
        self.lineEditDocOrigem.setMinimumSize(QtCore.QSize(61, 20))
        self.lineEditDocOrigem.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditDocOrigem.setMaxLength(6)
        self.lineEditDocOrigem.setCursorPosition(6)
        self.lineEditDocOrigem.setObjectName("lineEditDocOrigem")
        self.gridLayout.addWidget(self.lineEditDocOrigem, 0, 1, 1, 1)
        self.label_nome = QtGui.QLabel(self.widget)
        self.label_nome.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 1, 0, 1, 1)
        self.lineEditNome = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNome.sizePolicy().hasHeightForWidth())
        self.lineEditNome.setSizePolicy(sizePolicy)
        self.lineEditNome.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEditNome.setMaxLength(255)
        self.lineEditNome.setCursorPosition(27)
        self.lineEditNome.setObjectName("lineEditNome")
        self.gridLayout.addWidget(self.lineEditNome, 1, 1, 1, 1)
        self.label_endereco = QtGui.QLabel(self.widget)
        self.label_endereco.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_endereco.setObjectName("label_endereco")
        self.gridLayout.addWidget(self.label_endereco, 2, 0, 1, 1)
        self.lineEditEndereco = QtGui.QLineEdit(self.widget)
        self.lineEditEndereco.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.gridLayout.addWidget(self.lineEditEndereco, 2, 1, 1, 1)
        self.label_cpf = QtGui.QLabel(self.widget)
        self.label_cpf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cpf.setObjectName("label_cpf")
        self.gridLayout.addWidget(self.label_cpf, 3, 0, 1, 1)
        self.lineEditCPF = QtGui.QLineEdit(self.widget)
        self.lineEditCPF.setMaximumSize(QtCore.QSize(101, 20))
        self.lineEditCPF.setObjectName("lineEditCPF")
        self.gridLayout.addWidget(self.lineEditCPF, 3, 1, 1, 1)

        self.retranslateUi(ui_FISCAL_iCCDEstornar)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCCDEstornar)

    def retranslateUi(self, ui_FISCAL_iCCDEstornar):
        ui_FISCAL_iCCDEstornar.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Método iCCDEstornar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nome_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Doc. Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDocOrigem.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "012345", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nome.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNome.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Daruma Developers Community", None, QtGui.QApplication.UnicodeUTF8))
        self.label_endereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Endereço:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEndereco.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "Shishima Hifumi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cpf.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "CPF:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCPF.setText(QtGui.QApplication.translate("ui_FISCAL_iCCDEstornar", "111.111.111-11", None, QtGui.QApplication.UnicodeUTF8))

