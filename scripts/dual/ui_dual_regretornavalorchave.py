# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_regretornavalorchave.ui'
#
# Created: Mon Nov 24 22:25:17 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_regretornavalorchave(object):
    def setupUi(self, ui_dual_regretornavalorchave):
        ui_dual_regretornavalorchave.setObjectName("ui_dual_regretornavalorchave")
        ui_dual_regretornavalorchave.resize(499, 204)
        self.label = QtGui.QLabel(ui_dual_regretornavalorchave)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_dual_regretornavalorchave)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 281, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditProduto = QtGui.QLineEdit(ui_dual_regretornavalorchave)
        self.lineEditProduto.setGeometry(QtCore.QRect(10, 30, 271, 20))
        self.lineEditProduto.setObjectName("lineEditProduto")
        self.lineEditChave = QtGui.QLineEdit(ui_dual_regretornavalorchave)
        self.lineEditChave.setGeometry(QtCore.QRect(10, 80, 271, 20))
        self.lineEditChave.setObjectName("lineEditChave")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_regretornavalorchave)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(420, 170, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_regretornavalorchave)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(350, 170, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.label_3 = QtGui.QLabel(ui_dual_regretornavalorchave)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditRetorno = QtGui.QLineEdit(ui_dual_regretornavalorchave)
        self.lineEditRetorno.setGeometry(QtCore.QRect(10, 130, 271, 20))
        self.lineEditRetorno.setObjectName("lineEditRetorno")
        self.groupBox = QtGui.QGroupBox(ui_dual_regretornavalorchave)
        self.groupBox.setGeometry(QtCore.QRect(300, 20, 181, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 171, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(ui_dual_regretornavalorchave)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_regretornavalorchave)

    def retranslateUi(self, ui_dual_regretornavalorchave):
        ui_dual_regretornavalorchave.setWindowTitle(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Método regRetornaValorChave_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Informe abaixo qual produto ira trabalhar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Informe a Chave no qual gostaria de verificar o conteudo:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Valor resgatado:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "Nome dos Produtos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "TA2000 - MiniTerminais", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "DUAL - MiniImpressoras", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "MODEM - Modems MIN100/MIN200", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "ECF - Impressoras Fiscais", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ui_dual_regretornavalorchave", "DSP - Display", None, QtGui.QApplication.UnicodeUTF8))

