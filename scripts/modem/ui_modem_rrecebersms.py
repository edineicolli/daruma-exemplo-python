# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_rrecebersms.ui'
#
# Created: Mon Nov 24 22:26:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_rReceberSms(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_rReceberSms, self).__init__()

        self.setupUi(self)
        self.pushButtonLimpar.clicked.connect(self.on_Limpar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Limpar_clicked(self):
        pass

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_rReceberSms):
        ui_MODEM_rReceberSms.setObjectName("ui_MODEM_rReceberSms")
        ui_MODEM_rReceberSms.resize(249, 337)
        self.label = QtGui.QLabel(ui_MODEM_rReceberSms)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_MODEM_rReceberSms)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(ui_MODEM_rReceberSms)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 46, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(ui_MODEM_rReceberSms)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 46, 13))
        self.label_4.setObjectName("label_4")
        self.lineEditIndiceSms = QtGui.QLineEdit(ui_MODEM_rReceberSms)
        self.lineEditIndiceSms.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEditIndiceSms.setObjectName("lineEditIndiceSms")
        self.lineEditTelefone = QtGui.QLineEdit(ui_MODEM_rReceberSms)
        self.lineEditTelefone.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.lineEditTelefone.setObjectName("lineEditTelefone")
        self.lineEditData = QtGui.QLineEdit(ui_MODEM_rReceberSms)
        self.lineEditData.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.lineEditData.setObjectName("lineEditData")
        self.lineEditHora = QtGui.QLineEdit(ui_MODEM_rReceberSms)
        self.lineEditHora.setGeometry(QtCore.QRect(20, 190, 113, 20))
        self.lineEditHora.setObjectName("lineEditHora")
        self.textEditMensagem = QtGui.QTextEdit(ui_MODEM_rReceberSms)
        self.textEditMensagem.setGeometry(QtCore.QRect(20, 240, 111, 71))
        self.textEditMensagem.setObjectName("textEditMensagem")
        self.label_5 = QtGui.QLabel(ui_MODEM_rReceberSms)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.label_5.setObjectName("label_5")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_rReceberSms)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(150, 40, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_rReceberSms)
        self.pushButtonFechar.setGeometry(QtCore.QRect(150, 100, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.pushButtonLimpar = QtGui.QPushButton(ui_MODEM_rReceberSms)
        self.pushButtonLimpar.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.pushButtonLimpar.setObjectName("pushButtonLimpar")

        self.retranslateUi(ui_MODEM_rReceberSms)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_rReceberSms)

    def retranslateUi(self, ui_MODEM_rReceberSms):
        ui_MODEM_rReceberSms.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Método rReceberSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Indice SMS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Telefone Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Hora:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Mensagem", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLimpar.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSms", "Limpar", None, QtGui.QApplication.UnicodeUTF8))

