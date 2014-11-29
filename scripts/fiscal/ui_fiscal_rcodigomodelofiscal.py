# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rcodigomodelofiscal.ui'
#
# Created: Mon Nov 24 22:26:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rCodigoModeloFiscal(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rCodigoModeloFiscal, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_rCodigoModeloFiscal):
        ui_FISCAL_rCodigoModeloFiscal.setObjectName("ui_FISCAL_rCodigoModeloFiscal")
        ui_FISCAL_rCodigoModeloFiscal.resize(357, 145)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_rCodigoModeloFiscal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rCodigoModeloFiscal)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditModeloFiscal = QtGui.QLineEdit(ui_FISCAL_rCodigoModeloFiscal)
        self.lineEditModeloFiscal.setReadOnly(True)
        self.lineEditModeloFiscal.setObjectName("lineEditModeloFiscal")
        self.verticalLayout.addWidget(self.lineEditModeloFiscal)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rCodigoModeloFiscal)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rCodigoModeloFiscal)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rCodigoModeloFiscal)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rCodigoModeloFiscal)

    def retranslateUi(self, ui_FISCAL_rCodigoModeloFiscal):
        ui_FISCAL_rCodigoModeloFiscal.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rCodigoModeloFiscal", "Método rCodigoModeloFiscal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rCodigoModeloFiscal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Codigo do Modelo Fiscal:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rCodigoModeloFiscal", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rCodigoModeloFiscal", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

