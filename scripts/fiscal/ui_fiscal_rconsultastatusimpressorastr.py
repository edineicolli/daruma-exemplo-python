# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rconsultastatusimpressorastr.ui'
#
# Created: Mon Nov 24 22:26:17 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rConsultaStatusImpressoraStr(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rConsultaStatusImpressoraStr, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_rConsultaStatusImpressoraStr):
        ui_FISCAL_rConsultaStatusImpressoraStr.setObjectName("ui_FISCAL_rConsultaStatusImpressoraStr")
        ui_FISCAL_rConsultaStatusImpressoraStr.resize(252, 100)
        ui_FISCAL_rConsultaStatusImpressoraStr.setMaximumSize(QtCore.QSize(252, 100))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_rConsultaStatusImpressoraStr)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rConsultaStatusImpressoraStr)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditIndice = QtGui.QLineEdit(ui_FISCAL_rConsultaStatusImpressoraStr)
        self.lineEditIndice.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEditIndice.setObjectName("lineEditIndice")
        self.horizontalLayout.addWidget(self.lineEditIndice)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rConsultaStatusImpressoraStr)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_2.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rConsultaStatusImpressoraStr)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_2.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ui_FISCAL_rConsultaStatusImpressoraStr)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rConsultaStatusImpressoraStr)

    def retranslateUi(self, ui_FISCAL_rConsultaStatusImpressoraStr):
        ui_FISCAL_rConsultaStatusImpressoraStr.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rConsultaStatusImpressoraStr", "Método rConsultaStatusImpressoraStr_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rConsultaStatusImpressoraStr", "Entre com o Índice:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditIndice.setText(QtGui.QApplication.translate("ui_FISCAL_rConsultaStatusImpressoraStr", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rConsultaStatusImpressoraStr", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rConsultaStatusImpressoraStr", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

