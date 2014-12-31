# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rrsachavepublica.ui'
#
# Created: Mon Nov 24 22:26:34 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
from ctypes import create_string_buffer

from PySide import QtCore, QtGui
from pydaruma.pydaruma import rRSAChavePublica_ECF_Daruma


class Ui_ui_FISCAL_rRSAChavePublica(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rRSAChavePublica, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrCaminhoKey = self.lineEditCaminhoArq.text()

        cChavePublica = create_string_buffer(1000)
        cExpoentePublico  = create_string_buffer(1000)

        rRSAChavePublica_ECF_Daruma(StrCaminhoKey,cChavePublica,cExpoentePublico);

        StrChavePublica = cChavePublica
        StrExpoentePublico = cExpoentePublico

        self.textEditChavePublica.setText(StrChavePublica)
        self.textEditExpoentePublico.setText(StrExpoentePublico)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rRSAChavePublica):
        ui_FISCAL_rRSAChavePublica.setObjectName("ui_FISCAL_rRSAChavePublica")
        ui_FISCAL_rRSAChavePublica.resize(323, 280)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_rRSAChavePublica)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ui_FISCAL_rRSAChavePublica)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditCaminhoArq = QtGui.QLineEdit(ui_FISCAL_rRSAChavePublica)
        self.lineEditCaminhoArq.setObjectName("lineEditCaminhoArq")
        self.verticalLayout.addWidget(self.lineEditCaminhoArq)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rRSAChavePublica)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.verticalLayout.addWidget(self.pushButtonEnviar)
        self.label_2 = QtGui.QLabel(ui_FISCAL_rRSAChavePublica)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEditChavePublica = QtGui.QTextEdit(ui_FISCAL_rRSAChavePublica)
        self.textEditChavePublica.setObjectName("textEditChavePublica")
        self.verticalLayout.addWidget(self.textEditChavePublica)
        self.label_3 = QtGui.QLabel(ui_FISCAL_rRSAChavePublica)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEditExpoentePublico = QtGui.QTextEdit(ui_FISCAL_rRSAChavePublica)
        self.textEditExpoentePublico.setObjectName("textEditExpoentePublico")
        self.verticalLayout.addWidget(self.textEditExpoentePublico)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rRSAChavePublica)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.verticalLayout.addWidget(self.pushButtonCancelar)

        self.retranslateUi(ui_FISCAL_rRSAChavePublica)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rRSAChavePublica)

    def retranslateUi(self, ui_FISCAL_rRSAChavePublica):
        ui_FISCAL_rRSAChavePublica.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "Método rRSAChavePublica_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "Caminho Completo da Chave Privada .key:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCaminhoArq.setText(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "C:\\Chave.key", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "Gerar Chave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "Chave Pública Retornada:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "Expoente Público Retornado:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rRSAChavePublica", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

