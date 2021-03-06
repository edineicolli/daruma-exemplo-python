# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_etef_esperararquivo.ui'
#
# Created: Mon Nov 24 22:25:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import eTEF_EsperarArquivo_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_eTEF_EsperarArquivo(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eTEF_EsperarArquivo, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):

        StrCaminhoArq = self.lineEditCaminhoArquivo.text()
        StrTempoEspera = self.lineEditTempoEspera.text()
        iTempoEspera = StrTempoEspera.toInt()

        if(self.radioButtonTravarSIM.isChecked()):
            bTravarTeclado = True
        if(self.radioButtonTravarNAO.isChecked()):
            bTravarTeclado = False

        tratarRetornoFiscal(eTEF_EsperarArquivo_ECF_Daruma(StrCaminhoArq, bTravarTeclado, iTempoEspera), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_eTEF_EsperarArquivo):
        ui_FISCAL_eTEF_EsperarArquivo.setObjectName("ui_FISCAL_eTEF_EsperarArquivo")
        ui_FISCAL_eTEF_EsperarArquivo.resize(295, 293)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_eTEF_EsperarArquivo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_eTEF_EsperarArquivo)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditCaminhoArquivo = QtGui.QLineEdit(self.groupBox)
        self.lineEditCaminhoArquivo.setObjectName("lineEditCaminhoArquivo")
        self.gridLayout_2.addWidget(self.lineEditCaminhoArquivo, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_eTEF_EsperarArquivo)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(61, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(76, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 2)
        self.radioButtonTravarSIM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonTravarSIM.setObjectName("radioButtonTravarSIM")
        self.gridLayout.addWidget(self.radioButtonTravarSIM, 1, 2, 1, 1)
        self.radioButtonTravarNAO = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonTravarNAO.setObjectName("radioButtonTravarNAO")
        self.gridLayout.addWidget(self.radioButtonTravarNAO, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(76, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 4, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(ui_FISCAL_eTEF_EsperarArquivo)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(66, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)
        self.lineEditTempoEspera = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditTempoEspera.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEditTempoEspera.setMaxLength(2)
        self.lineEditTempoEspera.setObjectName("lineEditTempoEspera")
        self.gridLayout_3.addWidget(self.lineEditTempoEspera, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setMinimumSize(QtCore.QSize(61, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(65, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eTEF_EsperarArquivo)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eTEF_EsperarArquivo)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_eTEF_EsperarArquivo)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eTEF_EsperarArquivo)

    def retranslateUi(self, ui_FISCAL_eTEF_EsperarArquivo):
        ui_FISCAL_eTEF_EsperarArquivo.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Método eTEF_EsperarArquivo_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Local do Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Insira o caminho com o nome e externsão do arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminhoArquivo.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "C:\\Tef_Dial\\Resp\\Intpos.001", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Teclado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Deseja travar o teclado?", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTravarSIM.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Sim", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTravarNAO.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Não", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Tempo de Espera:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Insira o tempo de espera do arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditTempoEspera.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "segundos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_EsperarArquivo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

