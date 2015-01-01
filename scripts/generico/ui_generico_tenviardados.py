# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_generico_tenviardados.ui'
#
# Created: Mon Nov 24 22:26:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import tEnviarDados_Daruma
from scripts.generico.retornogenerico import tratarRetornoGenerico


class Ui_ui_GENERICO_tEnviarDados(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_GENERICO_tEnviarDados, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrDados = self.textEdit.toPlainText()
        StrBytes = self.lineEdit.text()

        iRetorno = tEnviarDados_Daruma(StrDados, StrBytes)
        tratarRetornoGenerico(iRetorno, self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_GENERICO_tEnviarDados):
        ui_GENERICO_tEnviarDados.setObjectName("ui_GENERICO_tEnviarDados")
        ui_GENERICO_tEnviarDados.resize(347, 211)
        ui_GENERICO_tEnviarDados.setMaximumSize(QtCore.QSize(347, 211))
        self.verticalLayout = QtGui.QVBoxLayout(ui_GENERICO_tEnviarDados)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_GENERICO_tEnviarDados)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(ui_GENERICO_tEnviarDados)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_2 = QtGui.QLabel(ui_GENERICO_tEnviarDados)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(ui_GENERICO_tEnviarDados)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButtonEnviar = QtGui.QPushButton(ui_GENERICO_tEnviarDados)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.verticalLayout.addWidget(self.pushButtonEnviar)
        self.pushButtonCancelar = QtGui.QPushButton(ui_GENERICO_tEnviarDados)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.verticalLayout.addWidget(self.pushButtonCancelar)

        self.retranslateUi(ui_GENERICO_tEnviarDados)
        QtCore.QMetaObject.connectSlotsByName(ui_GENERICO_tEnviarDados)

    def retranslateUi(self, ui_GENERICO_tEnviarDados):
        ui_GENERICO_tEnviarDados.setWindowTitle(QtGui.QApplication.translate("ui_GENERICO_tEnviarDados", "Método tEnviarDados_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_GENERICO_tEnviarDados", "Comando:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_GENERICO_tEnviarDados", "Bytes:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_GENERICO_tEnviarDados", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_GENERICO_tEnviarDados", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

