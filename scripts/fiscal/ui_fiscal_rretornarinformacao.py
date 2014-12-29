# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rretornarinformacao.ui'
#
# Created: Mon Nov 24 22:26:32 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rRetornarInformacao(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rRetornarInformacao, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        pass

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rRetornarInformacao):
        ui_FISCAL_rRetornarInformacao.setObjectName("ui_FISCAL_rRetornarInformacao")
        ui_FISCAL_rRetornarInformacao.resize(632, 395)
        ui_FISCAL_rRetornarInformacao.setMinimumSize(QtCore.QSize(632, 395))
        ui_FISCAL_rRetornarInformacao.setMaximumSize(QtCore.QSize(632, 395))
        self.verticalLayout_6 = QtGui.QVBoxLayout(ui_FISCAL_rRetornarInformacao)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxInformacoes = QtGui.QGroupBox(ui_FISCAL_rRetornarInformacao)
        self.groupBoxInformacoes.setMaximumSize(QtCore.QSize(370, 83))
        self.groupBoxInformacoes.setObjectName("groupBoxInformacoes")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBoxInformacoes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBoxInformacoes)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditIndice = QtGui.QLineEdit(self.groupBoxInformacoes)
        self.lineEditIndice.setMaximumSize(QtCore.QSize(51, 20))
        self.lineEditIndice.setObjectName("lineEditIndice")
        self.gridLayout.addWidget(self.lineEditIndice, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(self.groupBoxInformacoes)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxInformacoes)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBoxInformacoes)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.groupBoxRetorno = QtGui.QGroupBox(ui_FISCAL_rRetornarInformacao)
        self.groupBoxRetorno.setObjectName("groupBoxRetorno")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBoxRetorno)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.textEditRetorno = QtGui.QTextEdit(self.groupBoxRetorno)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditRetorno.sizePolicy().hasHeightForWidth())
        self.textEditRetorno.setSizePolicy(sizePolicy)
        self.textEditRetorno.setMinimumSize(QtCore.QSize(0, 0))
        self.textEditRetorno.setObjectName("textEditRetorno")
        self.verticalLayout.addWidget(self.textEditRetorno)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_6.addWidget(self.groupBoxRetorno)

        self.retranslateUi(ui_FISCAL_rRetornarInformacao)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rRetornarInformacao)

    def retranslateUi(self, ui_FISCAL_rRetornarInformacao):
        ui_FISCAL_rRetornarInformacao.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "Método rRetornarInformacao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxInformacoes.setTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "Informações:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "Indice da Informação:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditIndice.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "78", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxRetorno.setTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarInformacao", "Retorno:", None, QtGui.QApplication.UnicodeUTF8))

