# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_rrecebersmsindice.ui'
#
# Created: Mon Nov 24 22:26:49 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_rReceberSmsIndice(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_rReceberSmsIndice, self).__init__()

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

    def setupUi(self, ui_MODEM_rReceberSmsIndice):
        ui_MODEM_rReceberSmsIndice.setObjectName("ui_MODEM_rReceberSmsIndice")
        ui_MODEM_rReceberSmsIndice.resize(251, 338)
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_rReceberSmsIndice)
        self.pushButtonFechar.setGeometry(QtCore.QRect(150, 100, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.label_3 = QtGui.QLabel(ui_MODEM_rReceberSmsIndice)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 46, 13))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtGui.QLabel(ui_MODEM_rReceberSmsIndice)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEditTelefone = QtGui.QLineEdit(ui_MODEM_rReceberSmsIndice)
        self.lineEditTelefone.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.lineEditTelefone.setObjectName("lineEditTelefone")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_rReceberSmsIndice)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(150, 40, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.label_4 = QtGui.QLabel(ui_MODEM_rReceberSmsIndice)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 46, 13))
        self.label_4.setObjectName("label_4")
        self.lineEditIndiceSms = QtGui.QLineEdit(ui_MODEM_rReceberSmsIndice)
        self.lineEditIndiceSms.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEditIndiceSms.setObjectName("lineEditIndiceSms")
        self.textEditMensagem = QtGui.QTextEdit(ui_MODEM_rReceberSmsIndice)
        self.textEditMensagem.setGeometry(QtCore.QRect(20, 240, 111, 71))
        self.textEditMensagem.setObjectName("textEditMensagem")
        self.pushButtonLimpar = QtGui.QPushButton(ui_MODEM_rReceberSmsIndice)
        self.pushButtonLimpar.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.pushButtonLimpar.setObjectName("pushButtonLimpar")
        self.label_2 = QtGui.QLabel(ui_MODEM_rReceberSmsIndice)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditHora = QtGui.QLineEdit(ui_MODEM_rReceberSmsIndice)
        self.lineEditHora.setGeometry(QtCore.QRect(20, 190, 113, 20))
        self.lineEditHora.setObjectName("lineEditHora")
        self.label = QtGui.QLabel(ui_MODEM_rReceberSmsIndice)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.lineEditData = QtGui.QLineEdit(ui_MODEM_rReceberSmsIndice)
        self.lineEditData.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.lineEditData.setObjectName("lineEditData")

        self.retranslateUi(ui_MODEM_rReceberSmsIndice)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_rReceberSmsIndice)

    def retranslateUi(self, ui_MODEM_rReceberSmsIndice):
        ui_MODEM_rReceberSmsIndice.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Método rReceberSmsIndice_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Mensagem", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Hora:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLimpar.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Telefone Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_rReceberSmsIndice", "Indice SMS:", None, QtGui.QApplication.UnicodeUTF8))

