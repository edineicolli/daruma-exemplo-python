# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_menufiscal_lmfs.ui'
#
# Created: Mon Nov 24 22:26:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in self file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QDate
from pydaruma.pydaruma import iMFLerSerial_ECF_Daruma, iMFLer_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_MenuFiscal_LMFS(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_MenuFiscal_LMFS, self).__init__()

        self.setupUi(self)

        self.radioButtonDATAM.clicked.connect(self.on_radioButtonDATAM_clicked)
        self.radioButtonCRZ.clicked.connect(self.on_radioButtonCRZ_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.groupBoxIntervaloDataM.setVisible(False)
        self.groupBoxIntervaloCRZ.setVisible(False)
        self.dateEditInicial.setDate(QDate.currentDate())
        self.dateEditFinal.setDate(QDate.currentDate())
        
    def on_radioButtonCRZ_clicked(self):
        self.groupBoxIntervaloDataM.setVisible(False)
        self.groupBoxIntervaloCRZ.setVisible(True)
    
    def on_radioButtonDATAM_clicked(self):
        self.groupBoxIntervaloDataM.setVisible(True)
        self.groupBoxIntervaloCRZ.setVisible(False)
    
    def on_pushButtonEnviar_clicked(self):
        if(self.radioButtonCRZ.isChecked(self)):
            StrInicial = self.lineEditCRZInicial.text()
            StrFinal = self.lineEditCRZFinal.text()
        
        if(self.radioButtonDATAM.isChecked(self)):
            StrInicial = self.dateEditInicial.text()
            StrFinal = self.dateEditFinal.text()

        #Execuçao do comando
        if(self.radioButtonLMFTipoArquivo.isChecked(self)):
            tratarRetornoFiscal(iMFLerSerial_ECF_Daruma(StrInicial,StrFinal),self)

        if(self.radioButtonLMFTipoImpressa.isChecked(self)):
            tratarRetornoFiscal(iMFLer_ECF_Daruma(StrInicial,StrFinal),self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_MenuFiscal_LMFS):
        ui_FISCAL_MenuFiscal_LMFS.setObjectName("ui_FISCAL_MenuFiscal_LMFS")
        ui_FISCAL_MenuFiscal_LMFS.resize(249, 370)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_MenuFiscal_LMFS)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_MenuFiscal_LMFS)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.groupBoxPorIntervalo = QtGui.QGroupBox(ui_FISCAL_MenuFiscal_LMFS)
        self.groupBoxPorIntervalo.setObjectName("groupBoxPorIntervalo")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxPorIntervalo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButtonCRZ = QtGui.QRadioButton(self.groupBoxPorIntervalo)
        self.radioButtonCRZ.setObjectName("radioButtonCRZ")
        self.gridLayout_2.addWidget(self.radioButtonCRZ, 0, 0, 1, 1)
        self.radioButtonDATAM = QtGui.QRadioButton(self.groupBoxPorIntervalo)
        self.radioButtonDATAM.setObjectName("radioButtonDATAM")
        self.gridLayout_2.addWidget(self.radioButtonDATAM, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBoxPorIntervalo)
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_MenuFiscal_LMFS)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButtonLMFTipoImpressa = QtGui.QRadioButton(self.groupBox)
        self.radioButtonLMFTipoImpressa.setObjectName("radioButtonLMFTipoImpressa")
        self.gridLayout_3.addWidget(self.radioButtonLMFTipoImpressa, 0, 0, 1, 1)
        self.radioButtonLMFTipoArquivo = QtGui.QRadioButton(self.groupBox)
        self.radioButtonLMFTipoArquivo.setObjectName("radioButtonLMFTipoArquivo")
        self.gridLayout_3.addWidget(self.radioButtonLMFTipoArquivo, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBoxIntervaloCRZ = QtGui.QGroupBox(ui_FISCAL_MenuFiscal_LMFS)
        self.groupBoxIntervaloCRZ.setMinimumSize(QtCore.QSize(231, 86))
        self.groupBoxIntervaloCRZ.setAutoFillBackground(False)
        self.groupBoxIntervaloCRZ.setFlat(False)
        self.groupBoxIntervaloCRZ.setCheckable(False)
        self.groupBoxIntervaloCRZ.setObjectName("groupBoxIntervaloCRZ")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBoxIntervaloCRZ)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelCRZIni_2 = QtGui.QLabel(self.groupBoxIntervaloCRZ)
        self.labelCRZIni_2.setEnabled(True)
        self.labelCRZIni_2.setObjectName("labelCRZIni_2")
        self.gridLayout_4.addWidget(self.labelCRZIni_2, 0, 0, 1, 1)
        self.labelCRZFim_2 = QtGui.QLabel(self.groupBoxIntervaloCRZ)
        self.labelCRZFim_2.setEnabled(True)
        self.labelCRZFim_2.setObjectName("labelCRZFim_2")
        self.gridLayout_4.addWidget(self.labelCRZFim_2, 0, 1, 1, 1)
        self.lineEditCRZInicial = QtGui.QLineEdit(self.groupBoxIntervaloCRZ)
        self.lineEditCRZInicial.setEnabled(True)
        self.lineEditCRZInicial.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditCRZInicial.setMaxLength(4)
        self.lineEditCRZInicial.setObjectName("lineEditCRZInicial")
        self.gridLayout_4.addWidget(self.lineEditCRZInicial, 1, 0, 1, 1)
        self.lineEditCRZFinal = QtGui.QLineEdit(self.groupBoxIntervaloCRZ)
        self.lineEditCRZFinal.setEnabled(True)
        self.lineEditCRZFinal.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditCRZFinal.setMaxLength(4)
        self.lineEditCRZFinal.setObjectName("lineEditCRZFinal")
        self.gridLayout_4.addWidget(self.lineEditCRZFinal, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.groupBoxIntervaloCRZ)
        self.groupBoxIntervaloDataM = QtGui.QGroupBox(ui_FISCAL_MenuFiscal_LMFS)
        self.groupBoxIntervaloDataM.setMinimumSize(QtCore.QSize(231, 86))
        self.groupBoxIntervaloDataM.setAutoFillBackground(False)
        self.groupBoxIntervaloDataM.setFlat(False)
        self.groupBoxIntervaloDataM.setCheckable(False)
        self.groupBoxIntervaloDataM.setObjectName("groupBoxIntervaloDataM")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBoxIntervaloDataM)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelDataIni = QtGui.QLabel(self.groupBoxIntervaloDataM)
        self.labelDataIni.setEnabled(True)
        self.labelDataIni.setObjectName("labelDataIni")
        self.gridLayout.addWidget(self.labelDataIni, 0, 0, 1, 1)
        self.labelDataFim = QtGui.QLabel(self.groupBoxIntervaloDataM)
        self.labelDataFim.setEnabled(True)
        self.labelDataFim.setObjectName("labelDataFim")
        self.gridLayout.addWidget(self.labelDataFim, 0, 1, 1, 1)
        self.dateEditInicial = QtGui.QDateEdit(self.groupBoxIntervaloDataM)
        self.dateEditInicial.setCalendarPopup(True)
        self.dateEditInicial.setObjectName("dateEditInicial")
        self.gridLayout.addWidget(self.dateEditInicial, 1, 0, 1, 1)
        self.dateEditFinal = QtGui.QDateEdit(self.groupBoxIntervaloDataM)
        self.dateEditFinal.setCalendarPopup(True)
        self.dateEditFinal.setObjectName("dateEditFinal")
        self.gridLayout.addWidget(self.dateEditFinal, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.groupBoxIntervaloDataM)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_MenuFiscal_LMFS)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_MenuFiscal_LMFS)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem8 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)

        self.retranslateUi(ui_FISCAL_MenuFiscal_LMFS)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_MenuFiscal_LMFS)

    def retranslateUi(self, ui_FISCAL_MenuFiscal_LMFS):
        ui_FISCAL_MenuFiscal_LMFS.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Menu Fiscal - Leitura da Memoria Fiscal Simplificada", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Leitura de Memória Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxPorIntervalo.setTitle(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Relatório Por:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCRZ.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "CRZ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Tipo de Leitura da Memoria Fiscal:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonLMFTipoImpressa.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Impressa", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonLMFTipoArquivo.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloCRZ.setTitle(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Intevalo CRZ:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCRZIni_2.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "CRZ Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCRZFim_2.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "CRZ Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCRZInicial.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "0001", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCRZFinal.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "0005", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloDataM.setTitle(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Intevalo DATAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDataIni.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Data Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDataFim.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Data Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_MenuFiscal_LMFS", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

