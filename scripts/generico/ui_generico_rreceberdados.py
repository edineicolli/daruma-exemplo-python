# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_generico_rreceberdados.ui'
#
# Created: Mon Nov 24 22:26:38 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import rReceberDados_Daruma
from scripts.generico.retornogenerico import tratarRetornoGenerico


class Ui_ui_GENERICO_rReceberDados(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_GENERICO_rReceberDados, self).__init__()

        self.setupUi(self)
        self.pushButtonReceber.clicked.connect(self.on_pushButtonReceber_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonReceber_clicked(self):
        StrRecebe = ''
        # pydaruma erro
        iRetorno = rReceberDados_Daruma(StrRecebe);
        tratarRetornoGenerico(iRetorno, self);
        self.textEditRecebeDados.setText(StrRecebe);

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_GENERICO_rReceberDados):
        ui_GENERICO_rReceberDados.setObjectName("ui_GENERICO_rReceberDados")
        ui_GENERICO_rReceberDados.resize(370, 181)
        ui_GENERICO_rReceberDados.setMaximumSize(QtCore.QSize(370, 181))
        self.verticalLayout = QtGui.QVBoxLayout(ui_GENERICO_rReceberDados)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEditRecebeDados = QtGui.QTextEdit(ui_GENERICO_rReceberDados)
        self.textEditRecebeDados.setObjectName("textEditRecebeDados")
        self.verticalLayout.addWidget(self.textEditRecebeDados)
        self.pushButtonReceber = QtGui.QPushButton(ui_GENERICO_rReceberDados)
        self.pushButtonReceber.setObjectName("pushButtonReceber")
        self.verticalLayout.addWidget(self.pushButtonReceber)
        self.pushButtonCancelar = QtGui.QPushButton(ui_GENERICO_rReceberDados)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.verticalLayout.addWidget(self.pushButtonCancelar)

        self.retranslateUi(ui_GENERICO_rReceberDados)
        QtCore.QMetaObject.connectSlotsByName(ui_GENERICO_rReceberDados)

    def retranslateUi(self, ui_GENERICO_rReceberDados):
        ui_GENERICO_rReceberDados.setWindowTitle(QtGui.QApplication.translate("ui_GENERICO_rReceberDados", "Método rReceberDados_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReceber.setText(QtGui.QApplication.translate("ui_GENERICO_rReceberDados", "Receber", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_GENERICO_rReceberDados", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

