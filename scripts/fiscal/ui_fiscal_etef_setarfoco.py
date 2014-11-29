# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_etef_setarfoco.ui'
#
# Created: Mon Nov 24 22:25:30 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_eTEF_SetarFoco(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eTEF_SetarFoco, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_eTEF_SetarFoco):
        ui_FISCAL_eTEF_SetarFoco.setObjectName("ui_FISCAL_eTEF_SetarFoco")
        ui_FISCAL_eTEF_SetarFoco.resize(329, 125)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_eTEF_SetarFoco)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_eTEF_SetarFoco)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditCaption = QtGui.QLineEdit(ui_FISCAL_eTEF_SetarFoco)
        self.lineEditCaption.setObjectName("lineEditCaption")
        self.verticalLayout.addWidget(self.lineEditCaption)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eTEF_SetarFoco)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eTEF_SetarFoco)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_eTEF_SetarFoco)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eTEF_SetarFoco)

    def retranslateUi(self, ui_FISCAL_eTEF_SetarFoco):
        ui_FISCAL_eTEF_SetarFoco.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eTEF_SetarFoco", "Método eTEF_SetarFoco_ECF_Daruma ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_SetarFoco", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Digite o Caption da Tela para ser capturada:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaption.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_SetarFoco", "Internet Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_SetarFoco", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_SetarFoco", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

