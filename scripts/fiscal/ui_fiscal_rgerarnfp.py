# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rgerarnfp.ui'
#
# Created: Mon Nov 24 22:26:24 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rGerarNFP(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rGerarNFP, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_rGerarNFP):
        ui_FISCAL_rGerarNFP.setObjectName("ui_FISCAL_rGerarNFP")
        ui_FISCAL_rGerarNFP.resize(319, 225)
        ui_FISCAL_rGerarNFP.setMaximumSize(QtCore.QSize(319, 225))
        self.verticalLayout_4 = QtGui.QVBoxLayout(ui_FISCAL_rGerarNFP)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_rGerarNFP)
        self.groupBox_2.setMinimumSize(QtCore.QSize(301, 98))
        self.groupBox_2.setMaximumSize(QtCore.QSize(301, 98))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonDATAM = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonDATAM.setChecked(True)
        self.radioButtonDATAM.setObjectName("radioButtonDATAM")
        self.verticalLayout.addWidget(self.radioButtonDATAM)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelInicial = QtGui.QLabel(self.groupBox_2)
        self.labelInicial.setObjectName("labelInicial")
        self.verticalLayout_2.addWidget(self.labelInicial)
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
        self.groupBox_3 = QtGui.QGroupBox(ui_FISCAL_rGerarNFP)
        self.groupBox_3.setMinimumSize(QtCore.QSize(301, 72))
        self.groupBox_3.setMaximumSize(QtCore.QSize(301, 72))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditLocalArquivos = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditLocalArquivos.setObjectName("lineEditLocalArquivos")
        self.gridLayout_3.addWidget(self.lineEditLocalArquivos, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rGerarNFP)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rGerarNFP)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rGerarNFP)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rGerarNFP)

    def retranslateUi(self, ui_FISCAL_rGerarNFP):
        ui_FISCAL_rGerarNFP.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Método rGerarNFP_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Intervalo:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDATAM.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "DATAM", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInicial.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditInicial.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFinal.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEditFinal.setDisplayFormat(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "ddMMyyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Local de Gravação", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Local:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rGerarNFP", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
