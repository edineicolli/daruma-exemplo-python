# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_regcaptionwinapp.ui'
#
# Created: Mon Nov 24 22:26:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_regCaptionWinAPP(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_regCaptionWinAPP, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)
        self.pushButtonFechar.clicked.connect(self.on_Fechar_clicked)

    def on_Enviar_clicked(self):
        pass

    def on_Fechar_clicked(self):
        self.close()

    def setupUi(self, ui_MODEM_regCaptionWinAPP):
        ui_MODEM_regCaptionWinAPP.setObjectName("ui_MODEM_regCaptionWinAPP")
        ui_MODEM_regCaptionWinAPP.resize(328, 122)
        self.lineEditCaptionWinAPP = QtGui.QLineEdit(ui_MODEM_regCaptionWinAPP)
        self.lineEditCaptionWinAPP.setGeometry(QtCore.QRect(20, 40, 281, 20))
        self.lineEditCaptionWinAPP.setObjectName("lineEditCaptionWinAPP")
        self.label = QtGui.QLabel(ui_MODEM_regCaptionWinAPP)
        self.label.setGeometry(QtCore.QRect(20, 20, 291, 16))
        self.label.setObjectName("label")
        self.pushButtonEnviar = QtGui.QPushButton(ui_MODEM_regCaptionWinAPP)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_regCaptionWinAPP)
        self.pushButtonFechar.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_regCaptionWinAPP)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_regCaptionWinAPP)

    def retranslateUi(self, ui_MODEM_regCaptionWinAPP):
        ui_MODEM_regCaptionWinAPP.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_regCaptionWinAPP", "Método regCaptionWinAPP_MODEM_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_regCaptionWinAPP", "Digite o Caption da janela que irá receber os SMS UNREAD:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_MODEM_regCaptionWinAPP", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_regCaptionWinAPP", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

