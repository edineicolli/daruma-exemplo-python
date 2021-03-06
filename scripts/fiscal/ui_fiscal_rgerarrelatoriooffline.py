# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rgerarrelatoriooffline.ui'
#
# Created: Mon Nov 24 22:26:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QDate
from pydaruma.pydaruma import rGerarRelatorioOffline_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_rGerarRelatorioOffline(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rGerarRelatorioOffline, self).__init__()

        self.setupUi(self)

        self.lineEditFinal.setVisible(False)
        self.lineEditInicial.setVisible(False)
        self.dateEditFinal.setVisible(False)
        self.dateEditInicial.setVisible(False)
        self.labelInicial.setVisible(False)
        self.labelFinal.setVisible(False)
        self.dateEditInicial.setDate(QDate.currentDate())
        self.dateEditFinal.setDate(QDate.currentDate())

        self.radioButtonDATAM.clicked.connect(self.on_radioButtonDATAM_clicked)
        self.radioButtonCRZ.clicked.connect(self.on_radioButtonCRZ_clicked)
        self.radioButtonCOO.clicked.connect(self.on_radioButtonCOO_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_radioButtonDATAM_clicked(self):
        self.dateEditInicial.setVisible(True)
        self.dateEditFinal.setVisible(True)
        self.lineEditFinal.setVisible(False)
        self.lineEditInicial.setVisible(False)
        self.labelInicial.setVisible(True)
        self.labelFinal.setVisible(True)
    
    
    def on_radioButtonCRZ_clicked(self):
        self.lineEditFinal.setVisible(True)
        self.lineEditInicial.setVisible(True)
        self.dateEditFinal.setVisible(False)
        self.dateEditInicial.setVisible(False)
        self.labelInicial.setVisible(True)
        self.labelFinal.setVisible(True)
    
    
    def on_radioButtonCOO_clicked(self):
        self.lineEditFinal.setVisible(True)
        self.lineEditInicial.setVisible(True)
        self.dateEditFinal.setVisible(False)
        self.dateEditInicial.setVisible(False)
        self.labelInicial.setVisible(True)
        self.labelFinal.setVisible(True)
    
    
    def on_pushButtonEnviar_clicked(self):

        StrRelatorios = ''    
        if(self.checkBoxMF.isChecked()):
            StrRelatorios+= "MF+"
        
        if(self.checkBoxMFD.isChecked()):
            StrRelatorios+= "MFD+"
        
        if(self.checkBoxTDM.isChecked()):
            StrRelatorios+= "TDM+"
        
        if(self.checkBoxNFP.isChecked()):
            StrRelatorios+= "NFP+"
        
        if(self.checkBoxNFPTDM.isChecked()):
            StrRelatorios+= "NFPTDM+"
        
        if(self.checkBoxSINTEGRA.isChecked()):
            StrRelatorios+= "SINTEGRA+"
        
        if(self.checkBoxSPED.isChecked()):
            StrRelatorios+= "SPED+"
        
        if(self.checkBoxLMFC.isChecked()):
            StrRelatorios+= "LFMC+"
        
        if(self.checkBoxLMFS.isChecked()):
            StrRelatorios+= "LMFS+"
            
        if(self.radioButtonCOO.isChecked() and self.radioButtonCRZ.isChecked() and self.radioButtonDATAM.isChecked()):
        
            StrInicial = self.lineEditInicial.text()
            StrFinal = self.lineEditFinal.text()
            if(self.radioButtonCOO.isChecked()):
                StrTipoIntervalo = "COO"
            if(self.radioButtonCRZ.isChecked()):
                StrTipoIntervalo = "CRZ"
            if(self.radioButtonDATAM.isChecked()):
                StrInicial = self.dateEditInicial.text()
                StrFinal = self.dateEditFinal.text()
                StrTipoIntervalo = "DATAM"

        if((self.lineEditArqINF != "") and (self.lineEditArqMF !="") and (self.lineEditArqMFD != "")):
            StrArqINF = self.lineEditArqINF.text()
            StrArqMF = self.lineEditArqMF.text()
            StrArqMFD = self.lineEditArqMFD.text()

        # Execuçao do Metodo
        tratarRetornoFiscal(rGerarRelatorioOffline_ECF_Daruma(StrRelatorios,StrTipoIntervalo,StrInicial,StrFinal,StrArqMF,StrArqMFD,StrArqINF), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rGerarRelatorioOffline):
        ui_FISCAL_rGerarRelatorioOffline.setObjectName("ui_FISCAL_rGerarRelatorioOffline")
        ui_FISCAL_rGerarRelatorioOffline.resize(319, 492)
        ui_FISCAL_rGerarRelatorioOffline.setMaximumSize(QtCore.QSize(319, 492))
        self.verticalLayout_4 = QtGui.QVBoxLayout(ui_FISCAL_rGerarRelatorioOffline)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_rGerarRelatorioOffline)
        self.groupBox.setMinimumSize(QtCore.QSize(301, 171))
        self.groupBox.setMaximumSize(QtCore.QSize(301, 171))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxMF = QtGui.QCheckBox(self.groupBox)
        self.checkBoxMF.setObjectName("checkBoxMF")
        self.gridLayout.addWidget(self.checkBoxMF, 0, 0, 1, 1)
        self.checkBoxMFD = QtGui.QCheckBox(self.groupBox)
        self.checkBoxMFD.setObjectName("checkBoxMFD")
        self.gridLayout.addWidget(self.checkBoxMFD, 0, 1, 1, 1)
        self.checkBoxTDM = QtGui.QCheckBox(self.groupBox)
        self.checkBoxTDM.setObjectName("checkBoxTDM")
        self.gridLayout.addWidget(self.checkBoxTDM, 0, 2, 1, 1)
        self.checkBoxNFP = QtGui.QCheckBox(self.groupBox)
        self.checkBoxNFP.setObjectName("checkBoxNFP")
        self.gridLayout.addWidget(self.checkBoxNFP, 1, 0, 1, 1)
        self.checkBoxNFPTDM = QtGui.QCheckBox(self.groupBox)
        self.checkBoxNFPTDM.setObjectName("checkBoxNFPTDM")
        self.gridLayout.addWidget(self.checkBoxNFPTDM, 1, 1, 1, 1)
        self.checkBoxSINTEGRA = QtGui.QCheckBox(self.groupBox)
        self.checkBoxSINTEGRA.setObjectName("checkBoxSINTEGRA")
        self.gridLayout.addWidget(self.checkBoxSINTEGRA, 1, 2, 1, 1)
        self.checkBoxSPED = QtGui.QCheckBox(self.groupBox)
        self.checkBoxSPED.setObjectName("checkBoxSPED")
        self.gridLayout.addWidget(self.checkBoxSPED, 2, 0, 1, 1)
        self.checkBoxLMFC = QtGui.QCheckBox(self.groupBox)
        self.checkBoxLMFC.setObjectName("checkBoxLMFC")
        self.gridLayout.addWidget(self.checkBoxLMFC, 2, 1, 1, 1)
        self.checkBoxLMFS = QtGui.QCheckBox(self.groupBox)
        self.checkBoxLMFS.setObjectName("checkBoxLMFS")
        self.gridLayout.addWidget(self.checkBoxLMFS, 2, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_rGerarRelatorioOffline)
        self.groupBox_2.setMinimumSize(QtCore.QSize(301, 98))
        self.groupBox_2.setMaximumSize(QtCore.QSize(301, 98))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonDATAM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonDATAM.setObjectName("radioButtonDATAM")
        self.verticalLayout.addWidget(self.radioButtonDATAM)
        self.radioButtonCRZ = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonCRZ.setObjectName("radioButtonCRZ")
        self.verticalLayout.addWidget(self.radioButtonCRZ)
        self.radioButtonCOO = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonCOO.setObjectName("radioButtonCOO")
        self.verticalLayout.addWidget(self.radioButtonCOO)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelInicial = QtGui.QLabel(self.groupBox_2)
        self.labelInicial.setObjectName("labelInicial")
        self.verticalLayout_2.addWidget(self.labelInicial)
        self.lineEditInicial = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditInicial.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditInicial.setText("")
        self.lineEditInicial.setObjectName("lineEditInicial")
        self.verticalLayout_2.addWidget(self.lineEditInicial)
        self.dateEditInicial = QtGui.QDateEdit(self.groupBox_2)
        self.dateEditInicial.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 12, 30), QtCore.QTime(0, 0, 0)))
        self.dateEditInicial.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEditInicial.setCalendarPopup(True)
        self.dateEditInicial.setObjectName("dateEditInicial")
        self.verticalLayout_2.addWidget(self.dateEditInicial)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelFinal = QtGui.QLabel(self.groupBox_2)
        self.labelFinal.setObjectName("labelFinal")
        self.verticalLayout_3.addWidget(self.labelFinal)
        self.lineEditFinal = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditFinal.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditFinal.setObjectName("lineEditFinal")
        self.verticalLayout_3.addWidget(self.lineEditFinal)
        self.dateEditFinal = QtGui.QDateEdit(self.groupBox_2)
        self.dateEditFinal.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEditFinal.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 12, 30), QtCore.QTime(0, 0, 0)))
        self.dateEditFinal.setCalendarPopup(True)
        self.dateEditFinal.setObjectName("dateEditFinal")
        self.verticalLayout_3.addWidget(self.dateEditFinal)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(ui_FISCAL_rGerarRelatorioOffline)
        self.groupBox_3.setMaximumSize(QtCore.QSize(301, 162))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditArqINF = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditArqINF.setObjectName("lineEditArqINF")
        self.gridLayout_3.addWidget(self.lineEditArqINF, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEditArqMF = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditArqMF.setObjectName("lineEditArqMF")
        self.gridLayout_3.addWidget(self.lineEditArqMF, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEditArqMFD = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditArqMFD.setObjectName("lineEditArqMFD")
        self.gridLayout_3.addWidget(self.lineEditArqMFD, 5, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rGerarRelatorioOffline)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rGerarRelatorioOffline)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rGerarRelatorioOffline)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rGerarRelatorioOffline)

    def retranslateUi(self, ui_FISCAL_rGerarRelatorioOffline):
        ui_FISCAL_rGerarRelatorioOffline.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Método rGerarRelatorioOffline_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Relatórios:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMF.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "MF", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMFD.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "MFD", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxTDM.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "TDM", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxNFP.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "NFP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxNFPTDM.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "NFPTDM", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSINTEGRA.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "SINTEGRA", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSPED.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "SPED", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxLMFC.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "LMFC", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxLMFS.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "LMFS", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Intervalo:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCRZ.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "CRZ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCOO.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "COO", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInicial.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFinal.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Gerar Relatórios a partir de:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Arquivo .INF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Arquivo .MF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Arquivo .MFD", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioOffline", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

