# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_regvelocidade.ui'
#
# Created: Mon Nov 24 22:25:19 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_regvelocidade(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_regvelocidade, self).__init__()

        self.setupUi(self)
        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):
        pass

    def setupUi(self, ui_dual_regvelocidade):
        ui_dual_regvelocidade.setObjectName("ui_dual_regvelocidade")
        ui_dual_regvelocidade.resize(282, 100)
        self.label = QtGui.QLabel(ui_dual_regvelocidade)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 20))
        self.label.setObjectName("label")
        self.lineEditValor = QtGui.QLineEdit(ui_dual_regvelocidade)
        self.lineEditValor.setGeometry(QtCore.QRect(10, 30, 261, 20))
        self.lineEditValor.setObjectName("lineEditValor")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_regvelocidade)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(210, 60, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_regvelocidade)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(140, 60, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")

        self.retranslateUi(ui_dual_regvelocidade)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_regvelocidade)

    def retranslateUi(self, ui_dual_regvelocidade):
        ui_dual_regvelocidade.setWindowTitle(QtGui.QApplication.translate("ui_dual_regvelocidade", "Método regVelocidade_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_regvelocidade", "Digite a velocidade de comunicaçao com a impressora:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_regvelocidade", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_regvelocidade", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

