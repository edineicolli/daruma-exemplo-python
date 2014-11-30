# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_regretornavalorchave.ui'
#
# Created: Mon Nov 24 22:26:46 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_regRetornaValorChave(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_regRetornaValorChave, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_regRetornaValorChave):
        ui_MODEM_regRetornaValorChave.setObjectName("ui_MODEM_regRetornaValorChave")
        ui_MODEM_regRetornaValorChave.resize(442, 225)
        self.lineEditProduto = QtGui.QLineEdit(ui_MODEM_regRetornaValorChave)
        self.lineEditProduto.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.lineEditProduto.setObjectName("lineEditProduto")
        self.label = QtGui.QLabel(ui_MODEM_regRetornaValorChave)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_MODEM_regRetornaValorChave)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 41, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditChave = QtGui.QLineEdit(ui_MODEM_regRetornaValorChave)
        self.lineEditChave.setGeometry(QtCore.QRect(20, 90, 181, 20))
        self.lineEditChave.setObjectName("lineEditChave")
        self.lineEditValorRetornado = QtGui.QLineEdit(ui_MODEM_regRetornaValorChave)
        self.lineEditValorRetornado.setGeometry(QtCore.QRect(20, 140, 181, 20))
        self.lineEditValorRetornado.setObjectName("lineEditValorRetornado")
        self.label_3 = QtGui.QLabel(ui_MODEM_regRetornaValorChave)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_regRetornaValorChave)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 180, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_regRetornaValorChave)
        self.pushButtonFechar.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.groupBox = QtGui.QGroupBox(ui_MODEM_regRetornaValorChave)
        self.groupBox.setGeometry(QtCore.QRect(220, 20, 201, 181))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 191, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 90, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(ui_MODEM_regRetornaValorChave)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_regRetornaValorChave)

    def retranslateUi(self, ui_MODEM_regRetornaValorChave):
        ui_MODEM_regRetornaValorChave.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Método regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Produto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Chave:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Valor Retonado:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "Produtos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "TA2000 - MiniTerminais", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "DUAL - MiniImpressoras", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "MODEM - Modem", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_MODEM_regRetornaValorChave", "ECF - Impressoras Fiscais", None, QtGui.QApplication.UnicodeUTF8))

