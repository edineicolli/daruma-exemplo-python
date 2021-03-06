# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_imflerserial.ui'
#
# Created: Mon Nov 24 22:26:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import QDate
from pydaruma.pydaruma import regAlterarValor_Daruma, iMFLerSerial_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iMFLerSerial(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iMFLerSerial, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.radioButtonCRZ.pressed.connect(self.on_radioButtonCRZ_pressed)
        self.radioButtonDATAM.pressed.connect(self.on_radioButtonDATAM_pressed)
        self.radioButtonTipoCompleta.pressed.connect(self.on_radioButtonTipoCompleta_pressed)
        self.radioButtonTipoSimplificada.pressed.connect(self.on_radioButtonTipoSimplificada_pressed)

        self.groupBoxIntervaloDataM.setVisible(False)
        self.groupBoxIntervaloCRZ.setVisible(False)
        self.groupBoxTipoLeitura.setVisible(False)
        self.dateEditInicial.setDate(QDate.currentDate())
        self.dateEditFinal.setDate(QDate.currentDate())

    def on_radioButtonCRZ_pressed(self):
        self.groupBoxIntervaloDataM.setVisible(False)
        self.groupBoxIntervaloCRZ.setVisible(True)
        self.labelInformacao.setVisible(False)
        self.groupBoxTipoLeitura.setVisible(True)

    def on_radioButtonDATAM_pressed(self):
        self.groupBoxIntervaloDataM.setVisible(True)
        self.groupBoxIntervaloCRZ.setVisible(False)
        self.labelInformacao.setVisible(False)
        self.groupBoxTipoLeitura.setVisible(True)

    def on_radioButtonTipoCompleta_pressed(self):
        regAlterarValor_Daruma("ECF\\LMFCompleta","1")

    def on_radioButtonTipoSimplificada_pressed(self):
        regAlterarValor_Daruma("ECF\\LMFCompleta","0")

    def on_pushButtonEnviar_clicked(self):
        if(self.radioButtonCRZ.isChecked()):
            StrIntInicial = self.lineEditCRZInicial.text()
            StrIntFinal = self.lineEditCRZFinal.text()

        if(self.radioButtonDATAM.isChecked()):
            StrIntInicial = self.dateEditInicial.text()
            StrIntFinal = self.dateEditFinal.text()

        tratarRetornoFiscal(iMFLerSerial_ECF_Daruma(StrIntInicial,StrIntFinal), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iMFLerSerial):
        ui_FISCAL_iMFLerSerial.setObjectName("ui_FISCAL_iMFLerSerial")
        ui_FISCAL_iMFLerSerial.resize(249, 389)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iMFLerSerial)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_iMFLerSerial)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.groupBoxPorIntervalo = QtGui.QGroupBox(ui_FISCAL_iMFLerSerial)
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
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.labelInformacao = QtGui.QLabel(ui_FISCAL_iMFLerSerial)
        self.labelInformacao.setObjectName("labelInformacao")
        self.verticalLayout_2.addWidget(self.labelInformacao)
        self.groupBoxTipoLeitura = QtGui.QGroupBox(ui_FISCAL_iMFLerSerial)
        self.groupBoxTipoLeitura.setObjectName("groupBoxTipoLeitura")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBoxTipoLeitura)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonTipoCompleta = QtGui.QRadioButton(self.groupBoxTipoLeitura)
        self.radioButtonTipoCompleta.setObjectName("radioButtonTipoCompleta")
        self.horizontalLayout_2.addWidget(self.radioButtonTipoCompleta)
        self.radioButtonTipoSimplificada = QtGui.QRadioButton(self.groupBoxTipoLeitura)
        self.radioButtonTipoSimplificada.setObjectName("radioButtonTipoSimplificada")
        self.horizontalLayout_2.addWidget(self.radioButtonTipoSimplificada)
        self.verticalLayout_2.addWidget(self.groupBoxTipoLeitura)
        self.groupBoxIntervaloCRZ = QtGui.QGroupBox(ui_FISCAL_iMFLerSerial)
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
        self.lineEditCRZInicial.setMaxLength(6)
        self.lineEditCRZInicial.setObjectName("lineEditCRZInicial")
        self.gridLayout_4.addWidget(self.lineEditCRZInicial, 1, 0, 1, 1)
        self.lineEditCRZFinal = QtGui.QLineEdit(self.groupBoxIntervaloCRZ)
        self.lineEditCRZFinal.setEnabled(True)
        self.lineEditCRZFinal.setMaximumSize(QtCore.QSize(61, 20))
        self.lineEditCRZFinal.setMaxLength(6)
        self.lineEditCRZFinal.setObjectName("lineEditCRZFinal")
        self.gridLayout_4.addWidget(self.lineEditCRZFinal, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.groupBoxIntervaloCRZ)
        self.groupBoxIntervaloDataM = QtGui.QGroupBox(ui_FISCAL_iMFLerSerial)
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
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iMFLerSerial)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iMFLerSerial)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iMFLerSerial)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iMFLerSerial)

    def retranslateUi(self, ui_FISCAL_iMFLerSerial):
        ui_FISCAL_iMFLerSerial.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Método iMFLerSerial_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Leitura da Memoria Fiscal em Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxPorIntervalo.setTitle(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Relatório Por:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCRZ.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "CRZ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInformacao.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Selecione o Intervalo por DATAM ou CRZ.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxTipoLeitura.setTitle(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Tipo de Leitura:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTipoCompleta.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Completa", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTipoSimplificada.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Simplificada", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloCRZ.setTitle(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Intevalo CRZ:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCRZIni_2.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "CRZ Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCRZFim_2.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "CRZ Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCRZInicial.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "000001", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCRZFinal.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "000005", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxIntervaloDataM.setTitle(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Intevalo DATAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDataIni.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Data Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDataFim.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Data Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iMFLerSerial", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

