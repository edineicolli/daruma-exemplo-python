# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_eapagar.ui'
#
# Created: Mon Nov 24 22:26:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_eApagar(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_eApagar, self).__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_enviar_clicked)
        self.pushButton_2.clicked.connect(self.on_fechar_clicked)

    def on_enviar_clicked(self):
        pass

    def on_fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_eApagar):
        ui_MODEM_eApagar.setObjectName("ui_MODEM_eApagar")
        ui_MODEM_eApagar.resize(212, 115)
        self.lineEditIndiceSms = QtGui.QLineEdit(ui_MODEM_eApagar)
        self.lineEditIndiceSms.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.lineEditIndiceSms.setObjectName("lineEditIndiceSms")
        self.label = QtGui.QLabel(ui_MODEM_eApagar)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(ui_MODEM_eApagar)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(ui_MODEM_eApagar)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(ui_MODEM_eApagar)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_eApagar)

    def retranslateUi(self, ui_MODEM_eApagar):
        ui_MODEM_eApagar.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_eApagar", "Método eApagarSms_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_eApagar", "Indice do SMS a ser apagado:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ui_MODEM_eApagar", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ui_MODEM_eApagar", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

