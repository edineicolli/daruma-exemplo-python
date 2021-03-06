# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rgerarrelatoriobaixonivel.ui'
#
# Created: Mon Nov 24 22:26:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QDate
from pydaruma.pydaruma import rGerarRelatorio_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_rGerarRelatorioBaixoNivel(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rGerarRelatorioBaixoNivel, self).__init__()

        self.setupUi(self)

        self.radioButtonDATAM.clicked.connect(self.on_radioButtonDATAM_clicked)
        self.radioButtonCRZ.clicked.connect(self.on_radioButtonCRZ_clicked)
        self.radioButtonCOO.clicked.connect(self.on_radioButtonCOO_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.lineEditFinal.setVisible(False)
        self.lineEditInicial.setVisible(False)
        self.dateEditFinal.setVisible(False)
        self.dateEditInicial.setVisible(False)
        self.labelInicial.setVisible(False)
        self.labelFinal.setVisible(False)
        self.lineEditRelatorios.setText("CF_Abrir+CF_Item")
        self.dateEditInicial.setDate(QDate.currentDate())
        self.dateEditFinal.setDate(QDate.currentDate())

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

        if(self.radioButtonCOO.isChecked(self) and self.radioButtonCRZ.isChecked(self) and self.radioButtonDATAM.isChecked(self)):
            StrInicial = self.lineEditInicial.text()
            StrFinal = self.lineEditFinal.text()
            if(self.radioButtonCOO.isChecked(self)):
                StrTipoIntervalo = "COO"
            if(self.radioButtonCRZ.isChecked(self)):
                StrTipoIntervalo = "CRZ"
            if(self.radioButtonDATAM.isChecked(self)):
                StrInicial = self.dateEditInicial.text()
                StrFinal = self.dateEditFinal.text()
                StrTipoIntervalo = "DATAM"

        StrRelatorios = self.lineEditRelatorios.text()

        # Execuçao do Metodo
        tratarRetornoFiscal(rGerarRelatorio_ECF_Daruma(StrRelatorios,StrTipoIntervalo,StrInicial,StrFinal),self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rGerarRelatorioBaixoNivel):
        ui_FISCAL_rGerarRelatorioBaixoNivel.setObjectName("ui_FISCAL_rGerarRelatorioBaixoNivel")
        ui_FISCAL_rGerarRelatorioBaixoNivel.resize(319, 194)
        ui_FISCAL_rGerarRelatorioBaixoNivel.setMaximumSize(QtCore.QSize(319, 194))
        self.verticalLayout_4 = QtGui.QVBoxLayout(ui_FISCAL_rGerarRelatorioBaixoNivel)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rGerarRelatorioBaixoNivel)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditRelatorios = QtGui.QLineEdit(ui_FISCAL_rGerarRelatorioBaixoNivel)
        self.lineEditRelatorios.setObjectName("lineEditRelatorios")
        self.gridLayout.addWidget(self.lineEditRelatorios, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_rGerarRelatorioBaixoNivel)
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rGerarRelatorioBaixoNivel)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rGerarRelatorioBaixoNivel)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rGerarRelatorioBaixoNivel)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rGerarRelatorioBaixoNivel)

    def retranslateUi(self, ui_FISCAL_rGerarRelatorioBaixoNivel):
        ui_FISCAL_rGerarRelatorioBaixoNivel.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "rGerarRelatorio_ECF_Daruma - Baixo Nivel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "Informações:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "Intervalo:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCRZ.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "CRZ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCOO.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "COO", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInicial.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFinal.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarRelatorioBaixoNivel", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

