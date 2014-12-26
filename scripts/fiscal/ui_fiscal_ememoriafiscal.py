# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_ememoriafiscal.ui'
#
# Created: Mon Nov 24 22:25:28 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QDate
from pydaruma.pydaruma import eMemoriaFiscal_ECF_Daruma, regAlterarValor_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_eMemoriaFiscal(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eMemoriaFiscal, self).__init__()

        self.setupUi(self)

        self.lineEditInicial.setVisible(False)
        self.lineEditFinal.setVisible(False)
        self.dateEditInicial.setVisible(False)
        self.dateEditFinal.setVisible(False)
        self.dateEditInicial.setDate(QDate.currentDate())
        self.dateEditFinal.setDate(QDate.currentDate())

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
    
        if(self.checkBoxArqMF.isChecked()):
            StrRelatorios = "ATO+"
        if(self.checkBoxEspelhoMF.isChecked()):
            StrRelatorios = "ARQ+"
        if(self.checkBoxImpMF.isChecked()):
            StrRelatorios = "IMP"
    
        if(self.radioButtonCRZ.isChecked()):
            StrIntInicial = self.lineEditInicial.text()
            StrIntFinal = self.lineEditFinal.text()
        if(self.radioButtonDATAM.isChecked()):
            StrIntInicial = self.dateEditInicial.text()
            StrIntFinal = self.dateEditFinal.text()

        if(self.lineEditDestinoArq.text() != ""):
            StrLocalDestino = self.lineEditDestinoArq.text()
    
            regAlterarValor_Daruma("START\\LocalArquivosRelatorios",StrLocalDestino)
    
        tratarRetornoFiscal(eMemoriaFiscal_ECF_Daruma(StrIntInicial,StrIntFinal, True,StrRelatorios), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_eMemoriaFiscal):
        ui_FISCAL_eMemoriaFiscal.setObjectName("ui_FISCAL_eMemoriaFiscal")
        ui_FISCAL_eMemoriaFiscal.resize(309, 295)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_eMemoriaFiscal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_eMemoriaFiscal)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxEspelhoMF = QtGui.QCheckBox(self.groupBox)
        self.checkBoxEspelhoMF.setObjectName("checkBoxEspelhoMF")
        self.horizontalLayout.addWidget(self.checkBoxEspelhoMF)
        self.checkBoxArqMF = QtGui.QCheckBox(self.groupBox)
        self.checkBoxArqMF.setObjectName("checkBoxArqMF")
        self.horizontalLayout.addWidget(self.checkBoxArqMF)
        self.checkBoxImpMF = QtGui.QCheckBox(self.groupBox)
        self.checkBoxImpMF.setObjectName("checkBoxImpMF")
        self.horizontalLayout.addWidget(self.checkBoxImpMF)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_eMemoriaFiscal)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioButtonDATAM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonDATAM.setObjectName("radioButtonDATAM")
        self.gridLayout_4.addWidget(self.radioButtonDATAM, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditInicial = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditInicial.setMaxLength(4)
        self.lineEditInicial.setObjectName("lineEditInicial")
        self.gridLayout_3.addWidget(self.lineEditInicial, 2, 0, 1, 1)
        self.dateEditInicial = QtGui.QDateEdit(self.groupBox_2)
        self.dateEditInicial.setCalendarPopup(True)
        self.dateEditInicial.setObjectName("dateEditInicial")
        self.gridLayout_3.addWidget(self.dateEditInicial, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 2, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditFinal = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditFinal.setMaxLength(4)
        self.lineEditFinal.setObjectName("lineEditFinal")
        self.gridLayout_2.addWidget(self.lineEditFinal, 2, 0, 1, 1)
        self.dateEditFinal = QtGui.QDateEdit(self.groupBox_2)
        self.dateEditFinal.setCalendarPopup(True)
        self.dateEditFinal.setObjectName("dateEditFinal")
        self.gridLayout_2.addWidget(self.dateEditFinal, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 2, 2, 1)
        self.radioButtonCRZ = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonCRZ.setObjectName("radioButtonCRZ")
        self.gridLayout_4.addWidget(self.radioButtonCRZ, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(ui_FISCAL_eMemoriaFiscal)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditDestinoArq = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditDestinoArq.setObjectName("lineEditDestinoArq")
        self.gridLayout.addWidget(self.lineEditDestinoArq, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eMemoriaFiscal)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_2.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eMemoriaFiscal)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_2.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ui_FISCAL_eMemoriaFiscal)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eMemoriaFiscal)

    def retranslateUi(self, ui_FISCAL_eMemoriaFiscal):
        ui_FISCAL_eMemoriaFiscal.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Método eMemoriaFiscal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Relatorios:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEspelhoMF.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Espelho em Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxArqMF.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "AtoCotepe", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxImpMF.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Impresso", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Intervalo:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Intervalo Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Intervalo Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCRZ.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "CRZ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Destino:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Destino do(s) Arquivo(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Gerar Relatório", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eMemoriaFiscal", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

