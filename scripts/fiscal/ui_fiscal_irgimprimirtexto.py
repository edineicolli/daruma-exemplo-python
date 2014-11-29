# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_irgimprimirtexto.ui'
#
# Created: Mon Nov 24 22:26:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iRGImprimirTexto(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iRGImprimirTexto, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iRGImprimirTexto):
        ui_FISCAL_iRGImprimirTexto.setObjectName("ui_FISCAL_iRGImprimirTexto")
        ui_FISCAL_iRGImprimirTexto.resize(301, 180)
        ui_FISCAL_iRGImprimirTexto.setMinimumSize(QtCore.QSize(301, 180))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_iRGImprimirTexto)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_iRGImprimirTexto)
        self.label.setMaximumSize(QtCore.QSize(283, 13))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEditTexto = QtGui.QTextEdit(ui_FISCAL_iRGImprimirTexto)
        self.textEditTexto.setObjectName("textEditTexto")
        self.verticalLayout.addWidget(self.textEditTexto)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iRGImprimirTexto)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iRGImprimirTexto)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iRGImprimirTexto)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iRGImprimirTexto)

    def retranslateUi(self, ui_FISCAL_iRGImprimirTexto):
        ui_FISCAL_iRGImprimirTexto.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iRGImprimirTexto", "Método iRGImprimirTexto_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iRGImprimirTexto", "Texto para Impressão:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditTexto.setHtml(QtGui.QApplication.translate("ui_FISCAL_iRGImprimirTexto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Texto com no máximo 619 caracteres</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iRGImprimirTexto", "Imprimir Texto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iRGImprimirTexto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

