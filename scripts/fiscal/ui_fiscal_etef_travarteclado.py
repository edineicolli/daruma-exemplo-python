# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_etef_travarteclado.ui'
#
# Created: Mon Nov 24 22:25:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import eTEF_TravarTeclado_ECF_Daruma
import time


class Ui_ui_FISCAL_eTEF_TravarTeclado(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_eTEF_TravarTeclado, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        QMessageBox.information(self, "DarumaFramework - Python/Qt!","Vou Travar o Teclado!")
        bTravar = True
        eTEF_TravarTeclado_ECF_Daruma(bTravar)
        time.sleep(5)
        bTravar = False
        eTEF_TravarTeclado_ECF_Daruma(bTravar)
        QMessageBox.information(self, "DarumaFramework - Python/Qt!", "Teclado Destravado!")

    def on_pushButtonCancelar_clicked(self):
        bTravar = False
        eTEF_TravarTeclado_ECF_Daruma(bTravar)
        QMessageBox.information(self, "DarumaFramework - Python/Qt!", "Teclado não travado!")
        self.close()

    def setupUi(self, ui_FISCAL_eTEF_TravarTeclado):
        ui_FISCAL_eTEF_TravarTeclado.setObjectName("ui_FISCAL_eTEF_TravarTeclado")
        ui_FISCAL_eTEF_TravarTeclado.resize(314, 181)
        ui_FISCAL_eTEF_TravarTeclado.setMinimumSize(QtCore.QSize(314, 181))
        ui_FISCAL_eTEF_TravarTeclado.setMaximumSize(QtCore.QSize(314, 181))
        self.gridLayout = QtGui.QGridLayout(ui_FISCAL_eTEF_TravarTeclado)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_eTEF_TravarTeclado)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_eTEF_TravarTeclado)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonTravarTeclado = QtGui.QPushButton(ui_FISCAL_eTEF_TravarTeclado)
        self.pushButtonTravarTeclado.setObjectName("pushButtonTravarTeclado")
        self.horizontalLayout.addWidget(self.pushButtonTravarTeclado)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_eTEF_TravarTeclado)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(ui_FISCAL_eTEF_TravarTeclado)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_eTEF_TravarTeclado)

    def retranslateUi(self, ui_FISCAL_eTEF_TravarTeclado):
        ui_FISCAL_eTEF_TravarTeclado.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_eTEF_TravarTeclado", "Método eTEF_TravarTeclado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_TravarTeclado", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Deseja realmente travar o teclado?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_TravarTeclado", "Seu teclado ficará travado por 5 segundos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTravarTeclado.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_TravarTeclado", "Travar Teclado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_eTEF_TravarTeclado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

