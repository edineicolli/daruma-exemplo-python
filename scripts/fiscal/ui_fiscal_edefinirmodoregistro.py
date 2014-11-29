# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_edefinirmodoregistro.ui'
#
# Created: Mon Nov 24 22:25:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_eDefinirModoRegistro(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eDefinirModoRegistro, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_eDefinirModoRegistro):
        ui_FISCAL_eDefinirModoRegistro.setObjectName("ui_FISCAL_eDefinirModoRegistro")
        ui_FISCAL_eDefinirModoRegistro.setWindowModality(QtCore.Qt.ApplicationModal)
        ui_FISCAL_eDefinirModoRegistro.resize(194, 167)
        ui_FISCAL_eDefinirModoRegistro.setMinimumSize(QtCore.QSize(194, 167))
        self.gridLayout_2 = QtGui.QGridLayout(ui_FISCAL_eDefinirModoRegistro)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_eDefinirModoRegistro)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_eDefinirModoRegistro)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonTipo_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonTipo_2.setObjectName("radioButtonTipo_2")
        self.gridLayout.addWidget(self.radioButtonTipo_2, 2, 0, 1, 1)
        self.radioButtonTipo_1 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonTipo_1.setObjectName("radioButtonTipo_1")
        self.gridLayout.addWidget(self.radioButtonTipo_1, 1, 0, 1, 1)
        self.radioButtonTipo_0 = QtGui.QRadioButton(self.groupBox)
        self.radioButtonTipo_0.setObjectName("radioButtonTipo_0")
        self.gridLayout.addWidget(self.radioButtonTipo_0, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_eDefinirModoRegistro)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eDefinirModoRegistro)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(ui_FISCAL_eDefinirModoRegistro)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eDefinirModoRegistro)

    def retranslateUi(self, ui_FISCAL_eDefinirModoRegistro):
        ui_FISCAL_eDefinirModoRegistro.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "Método eDefinirModoRegistro_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Escolha o modo de Registro:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "Modo", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTipo_2.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "2 - XML", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTipo_1.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "1 - CurrentUser e XML", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTipo_0.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "0 - LocalMachine e XML", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eDefinirModoRegistro", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

