# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_regtabulacao.ui'
#
# Created: Mon Nov 24 22:25:18 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_regtabulacao(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_regtabulacao, self).__init__()

        self.setupUi(self)
        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):
        pass

    def setupUi(self, ui_dual_regtabulacao):
        ui_dual_regtabulacao.setObjectName("ui_dual_regtabulacao")
        ui_dual_regtabulacao.resize(290, 108)
        self.lineEditValor = QtGui.QLineEdit(ui_dual_regtabulacao)
        self.lineEditValor.setGeometry(QtCore.QRect(10, 40, 261, 20))
        self.lineEditValor.setObjectName("lineEditValor")
        self.label = QtGui.QLabel(ui_dual_regtabulacao)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 31))
        self.label.setObjectName("label")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_regtabulacao)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(140, 70, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_regtabulacao)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(210, 70, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")

        self.retranslateUi(ui_dual_regtabulacao)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_regtabulacao)

    def retranslateUi(self, ui_dual_regtabulacao):
        ui_dual_regtabulacao.setWindowTitle(QtGui.QApplication.translate("ui_dual_regtabulacao", "Método regTabulaçao_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_regtabulacao", "\n"
"Entre com a tabulaçao desejada (\"05,10,15,20,25,35\"):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_regtabulacao", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_regtabulacao", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

