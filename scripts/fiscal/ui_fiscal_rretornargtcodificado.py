# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rretornargtcodificado.ui'
#
# Created: Mon Nov 24 22:26:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_rRetornarGTCodificado(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rRetornarGTCodificado, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        pass

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rRetornarGTCodificado):
        ui_FISCAL_rRetornarGTCodificado.setObjectName("ui_FISCAL_rRetornarGTCodificado")
        ui_FISCAL_rRetornarGTCodificado.resize(487, 106)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_rRetornarGTCodificado)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rRetornarGTCodificado)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditGTCodificado = QtGui.QLineEdit(ui_FISCAL_rRetornarGTCodificado)
        self.lineEditGTCodificado.setReadOnly(True)
        self.lineEditGTCodificado.setObjectName("lineEditGTCodificado")
        self.verticalLayout.addWidget(self.lineEditGTCodificado)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rRetornarGTCodificado)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rRetornarGTCodificado)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rRetornarGTCodificado)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rRetornarGTCodificado)

    def retranslateUi(self, ui_FISCAL_rRetornarGTCodificado):
        ui_FISCAL_rRetornarGTCodificado.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rRetornarGTCodificado", "Método rRetornarGTCodificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarGTCodificado", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GT Codificado:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarGTCodificado", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rRetornarGTCodificado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

