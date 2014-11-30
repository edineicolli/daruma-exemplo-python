# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_regportacomunicacao.ui'
#
# Created: Mon Nov 24 22:25:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_regportacomunicacao(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_regportacomunicacao, self).__init__()

        self.setupUi(self)

        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):
        pass

    def setupUi(self, ui_dual_regportacomunicacao):
        ui_dual_regportacomunicacao.setObjectName("ui_dual_regportacomunicacao")
        ui_dual_regportacomunicacao.resize(227, 109)
        self.lineEditValor = QtGui.QLineEdit(ui_dual_regportacomunicacao)
        self.lineEditValor.setGeometry(QtCore.QRect(10, 40, 201, 20))
        self.lineEditValor.setObjectName("lineEditValor")
        self.label = QtGui.QLabel(ui_dual_regportacomunicacao)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_regportacomunicacao)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(120, 70, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_regportacomunicacao)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(50, 70, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")

        self.retranslateUi(ui_dual_regportacomunicacao)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_regportacomunicacao)

    def retranslateUi(self, ui_dual_regportacomunicacao):
        ui_dual_regportacomunicacao.setWindowTitle(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Método regPortaComunicacao_DUAL_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Entre com a porta:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_regportacomunicacao", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

