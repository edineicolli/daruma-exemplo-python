# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rgerarespelhomfd.ui'
#
# Created: Mon Nov 24 22:26:21 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QDate
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import rGerarEspelhoMFD_ECF_Daruma, regAlterarValor_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_rGerarEspelhoMFD(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rGerarEspelhoMFD, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.radioButtonIntervaloCOO.clicked.connect(self.on_radioButtonIntervaloCOO_clicked)
        self.radioButtonIntervaloDATA.clicked.connect(self.on_radioButtonIntervaloDATA_clicked)
        self.radioButtonIntervaloDATAM.clicked.connect(self.on_radioButtonIntervaloDATAM_clicked)

        self.groupBoxTipoIntervalo.setVisible(True)
        self.groupBoxIntervaloCOO.setVisible(False)
        self.groupBoxIntervaloDATA.setVisible(False)
        self.groupBoxIntervaloDATAM.setVisible(False)
        self.groupBoxLocalDestino.setVisible(False)
        self.dateEditDATAInicial.setDate(QDate.currentDate())
        self.dateEditDATAFinal.setDate(QDate.currentDate())
        self.dateEditDATAMInicial.setDate(QDate.currentDate())
        self.dateEditDATAMFinal.setDate(QDate.currentDate())
        
    def on_radioButtonIntervaloCOO_clicked(self):
        self.groupBoxTipoIntervalo.setVisible(True)
        self.groupBoxIntervaloCOO.setVisible(True)
        self.groupBoxIntervaloDATA.setVisible(False)
        self.groupBoxIntervaloDATAM.setVisible(False)
        self.groupBoxLocalDestino.setVisible(True)
    
    def on_radioButtonIntervaloDATA_clicked(self):
        self.groupBoxTipoIntervalo.setVisible(True)
        self.groupBoxIntervaloCOO.setVisible(False)
        self.groupBoxIntervaloDATA.setVisible(True)
        self.groupBoxIntervaloDATAM.setVisible(False)
        self.groupBoxLocalDestino.setVisible(True)
    
    def on_radioButtonIntervaloDATAM_clicked(self):
        self.groupBoxTipoIntervalo.setVisible(True)
        self.groupBoxIntervaloCOO.setVisible(False)
        self.groupBoxIntervaloDATA.setVisible(False)
        self.groupBoxIntervaloDATAM.setVisible(True)
        self.groupBoxLocalDestino.setVisible(True)

    def on_pushButtonEnviar_clicked(self):

        if (self.radioButtonIntervaloCOO.isChecked()):

            if(self.lineEditLocalDestino.text() != ""):
                StrLocalCaminho = self.lineEditLocalDestino.text()
                regAlterarValor_Daruma("START\\LocalArquivos",StrLocalCaminho)

            # Declaraçao das Variaveis que recebem os valores da UI
            StrCOOInicial = self.lineEditCOOInicial.text()
            StrCOOFinal = self.lineEditCOOFinal.text()

            tratarRetornoFiscal(rGerarEspelhoMFD_ECF_Daruma("2",StrCOOInicial,StrCOOFinal), self)

        elif (self.radioButtonIntervaloDATA.isChecked()):
            if(self.lineEditLocalDestino.text() != ""):
                StrLocalCaminho = self.lineEditLocalDestino.text()
                regAlterarValor_Daruma("START\\LocalArquivos",StrLocalCaminho)

            # Declaraçao das Variaveis que recebem os valores da UI
            StrDATAInicial = self.dateEditDATAInicial.text()
            StrDATAFinal = self.dateEditDATAFinal.text()

            tratarRetornoFiscal(rGerarEspelhoMFD_ECF_Daruma("1",StrDATAInicial,StrDATAFinal), self)

        elif (self.radioButtonIntervaloDATAM.isChecked()):
            if(self.lineEditLocalDestino.text() != ""):
                StrLocalCaminho = self.lineEditLocalDestino.text()
                regAlterarValor_Daruma("START\\LocalArquivos",StrLocalCaminho)

            # Declaraçao das Variaveis que recebem os valores da UI
            StrDATAMInicial = self.dateEditDATAMInicial.text()
            StrDATAMFinal = self.dateEditDATAMFinal.text()

            tratarRetornoFiscal(rGerarEspelhoMFD_ECF_Daruma("3",StrDATAMInicial,StrDATAMFinal), self)
        else:
            QMessageBox.information(self, "DarumaFramework - Python/Qt","Selecione o Tipo de Intervalo!")

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rGerarEspelhoMFD):
        ui_FISCAL_rGerarEspelhoMFD.setObjectName("ui_FISCAL_rGerarEspelhoMFD")
        ui_FISCAL_rGerarEspelhoMFD.setWindowModality(QtCore.Qt.NonModal)
        ui_FISCAL_rGerarEspelhoMFD.resize(265, 307)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_FISCAL_rGerarEspelhoMFD.sizePolicy().hasHeightForWidth())
        ui_FISCAL_rGerarEspelhoMFD.setSizePolicy(sizePolicy)
        ui_FISCAL_rGerarEspelhoMFD.setMaximumSize(QtCore.QSize(265, 307))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_rGerarEspelhoMFD)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxTipoIntervalo = QtGui.QGroupBox(ui_FISCAL_rGerarEspelhoMFD)
        self.groupBoxTipoIntervalo.setObjectName("groupBoxTipoIntervalo")
        self.gridLayout = QtGui.QGridLayout(self.groupBoxTipoIntervalo)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonIntervaloDATA = QtGui.QRadioButton(self.groupBoxTipoIntervalo)
        self.radioButtonIntervaloDATA.setObjectName("radioButtonIntervaloDATA")
        self.gridLayout.addWidget(self.radioButtonIntervaloDATA, 0, 0, 1, 1)
        self.radioButtonIntervaloDATAM = QtGui.QRadioButton(self.groupBoxTipoIntervalo)
        self.radioButtonIntervaloDATAM.setObjectName("radioButtonIntervaloDATAM")
        self.gridLayout.addWidget(self.radioButtonIntervaloDATAM, 1, 0, 1, 1)
        self.radioButtonIntervaloCOO = QtGui.QRadioButton(self.groupBoxTipoIntervalo)
        self.radioButtonIntervaloCOO.setObjectName("radioButtonIntervaloCOO")
        self.gridLayout.addWidget(self.radioButtonIntervaloCOO, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxTipoIntervalo)
        self.groupBoxIntervaloCOO = QtGui.QGroupBox(ui_FISCAL_rGerarEspelhoMFD)
        self.groupBoxIntervaloCOO.setObjectName("groupBoxIntervaloCOO")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxIntervaloCOO)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.groupBoxIntervaloCOO)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxIntervaloCOO)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEditCOOInicial = QtGui.QLineEdit(self.groupBoxIntervaloCOO)
        self.lineEditCOOInicial.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditCOOInicial.setMaxLength(6)
        self.lineEditCOOInicial.setObjectName("lineEditCOOInicial")
        self.gridLayout_2.addWidget(self.lineEditCOOInicial, 1, 0, 1, 1)
        self.lineEditCOOFinal = QtGui.QLineEdit(self.groupBoxIntervaloCOO)
        self.lineEditCOOFinal.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditCOOFinal.setMaxLength(6)
        self.lineEditCOOFinal.setObjectName("lineEditCOOFinal")
        self.gridLayout_2.addWidget(self.lineEditCOOFinal, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxIntervaloCOO)
        self.groupBoxIntervaloDATA = QtGui.QGroupBox(ui_FISCAL_rGerarEspelhoMFD)
        self.groupBoxIntervaloDATA.setObjectName("groupBoxIntervaloDATA")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxIntervaloDATA)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtGui.QLabel(self.groupBoxIntervaloDATA)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBoxIntervaloDATA)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(111, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.dateEditDATAInicial = QtGui.QDateEdit(self.groupBoxIntervaloDATA)
        self.dateEditDATAInicial.setCalendarPopup(True)
        self.dateEditDATAInicial.setObjectName("dateEditDATAInicial")
        self.gridLayout_3.addWidget(self.dateEditDATAInicial, 1, 0, 1, 1)
        self.dateEditDATAFinal = QtGui.QDateEdit(self.groupBoxIntervaloDATA)
        self.dateEditDATAFinal.setCalendarPopup(True)
        self.dateEditDATAFinal.setObjectName("dateEditDATAFinal")
        self.gridLayout_3.addWidget(self.dateEditDATAFinal, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxIntervaloDATA)
        self.groupBoxIntervaloDATAM = QtGui.QGroupBox(ui_FISCAL_rGerarEspelhoMFD)
        self.groupBoxIntervaloDATAM.setObjectName("groupBoxIntervaloDATAM")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBoxIntervaloDATAM)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtGui.QLabel(self.groupBoxIntervaloDATAM)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBoxIntervaloDATAM)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(111, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 1, 1, 1)
        self.dateEditDATAMInicial = QtGui.QDateEdit(self.groupBoxIntervaloDATAM)
        self.dateEditDATAMInicial.setCalendarPopup(True)
        self.dateEditDATAMInicial.setObjectName("dateEditDATAMInicial")
        self.gridLayout_4.addWidget(self.dateEditDATAMInicial, 1, 0, 1, 1)
        self.dateEditDATAMFinal = QtGui.QDateEdit(self.groupBoxIntervaloDATAM)
        self.dateEditDATAMFinal.setCalendarPopup(True)
        self.dateEditDATAMFinal.setObjectName("dateEditDATAMFinal")
        self.gridLayout_4.addWidget(self.dateEditDATAMFinal, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxIntervaloDATAM)
        self.groupBoxLocalDestino = QtGui.QGroupBox(ui_FISCAL_rGerarEspelhoMFD)
        self.groupBoxLocalDestino.setObjectName("groupBoxLocalDestino")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBoxLocalDestino)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtGui.QLabel(self.groupBoxLocalDestino)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEditLocalDestino = QtGui.QLineEdit(self.groupBoxLocalDestino)
        self.lineEditLocalDestino.setText("")
        self.lineEditLocalDestino.setObjectName("lineEditLocalDestino")
        self.gridLayout_5.addWidget(self.lineEditLocalDestino, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxLocalDestino)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rGerarEspelhoMFD)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rGerarEspelhoMFD)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)

        self.retranslateUi(ui_FISCAL_rGerarEspelhoMFD)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rGerarEspelhoMFD)

    def retranslateUi(self, ui_FISCAL_rGerarEspelhoMFD):
        ui_FISCAL_rGerarEspelhoMFD.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Método rGerarEspelhoMFD_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxTipoIntervalo.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Tipo de Intervalo:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonIntervaloDATA.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "DATA", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonIntervaloDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "DATAM ( Data com movimento encerrado )", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonIntervaloCOO.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "COO ( Contador de Ordem de Operação )", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloCOO.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Intervalo COO:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "COO Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "COO Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCOOInicial.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "000123", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCOOFinal.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "000123", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloDATA.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Intervalo DATA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Data Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Data Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditDATAInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "ddMMyy", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditDATAFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "ddMMyy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloDATAM.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Intervalo DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Data Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Data Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditDATAMInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "ddMMyy", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditDATAMFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "ddMMyy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxLocalDestino.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Local de Gravação", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Destino do Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarEspelhoMFD", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

