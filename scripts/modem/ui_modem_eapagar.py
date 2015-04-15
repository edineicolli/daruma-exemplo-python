'''teste'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_eapagar.ui'
#
# Created: Mon Nov 24 22:26:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import eApagarSms_MODEM_DarumaFramework
from scripts.modem.retornomodem import tratarRetornoModem

class Ui_ui_MODEM_eApagar(QtGui.QWidget):
    '''teste'''
    def __init__(self):
        '''teste'''
        super(Ui_ui_MODEM_eApagar, self).__init__()

        self.setupui(self)
        self.pushButton.clicked.connect(self.on_apagar_clicked)
        self.BtnFechar.clicked.connect(self.on_fechar_clicked)

    def on_apagar_clicked(self):
        '''teste'''
        indice_sms = self.lineEditIndiceSms.text()
        tratarRetornoModem(eApagarSms_MODEM_DarumaFramework(indice_sms), self)

    def on_fechar_clicked(self):
        '''teste'''
        self.close()

    def setupui(self, ui_modem_eapagar):
        '''teste'''
        ui_modem_eapagar.setObjectName("ui_modem_eapagar")
        ui_modem_eapagar.resize(212, 115)
        self.lineEditIndiceSms = QtGui.QLineEdit(ui_modem_eapagar)
        self.lineEditIndiceSms.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.lineEditIndiceSms.setObjectName("lineEditIndiceSms")
        self.label = QtGui.QLabel(ui_modem_eapagar)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(ui_modem_eapagar)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.BtnFechar = QtGui.QPushButton(ui_modem_eapagar)
        self.BtnFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.BtnFechar.setObjectName("pushButton_2")

        self.retranslateui(ui_modem_eapagar)
        QtCore.QMetaObject.connectSlotsByName(ui_modem_eapagar)

    def retranslateui(self, ui_modem_eapagar):
        '''teste'''
        ui_modem_eapagar.setWindowTitle(
            QtGui.QApplication.translate(
                "ui_modem_eapagar",
                "Método eApagarSms_MODEM_DarumaFramework",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate(
            "ui_modem_eapagar",
            "Indice do SMS a ser apagado:",
            None,
            QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate(
            "ui_modem_eapagar",
            "Enviar",
            None,
            QtGui.QApplication.UnicodeUTF8))
        self.BtnFechar.setText(QtGui.QApplication.translate(
            "ui_modem_eapagar",
            "Fechar",
            None,
            QtGui.QApplication.UnicodeUTF8))
