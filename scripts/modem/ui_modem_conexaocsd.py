# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_modem_conexaocsd.ui'
#
# Created: Mon Nov 24 22:26:41 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_MODEM_ConexaoCSD(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_MODEM_ConexaoCSD, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_MODEM_ConexaoCSD):
        ui_MODEM_ConexaoCSD.setObjectName("ui_MODEM_ConexaoCSD")
        ui_MODEM_ConexaoCSD.resize(663, 415)
        self.label = QtGui.QLabel(ui_MODEM_ConexaoCSD)
        self.label.setGeometry(QtCore.QRect(180, 20, 311, 16))
        self.label.setObjectName("label")
        self.pushButtonAtivarConexao = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonAtivarConexao.setGeometry(QtCore.QRect(260, 40, 121, 23))
        self.pushButtonAtivarConexao.setObjectName("pushButtonAtivarConexao")
        self.line = QtGui.QFrame(ui_MODEM_ConexaoCSD)
        self.line.setGeometry(QtCore.QRect(20, 70, 621, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtGui.QLabel(ui_MODEM_ConexaoCSD)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditTelefone = QtGui.QLineEdit(ui_MODEM_ConexaoCSD)
        self.lineEditTelefone.setGeometry(QtCore.QRect(160, 90, 81, 20))
        self.lineEditTelefone.setObjectName("lineEditTelefone")
        self.pushButtonRealizarChamada = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonRealizarChamada.setGeometry(QtCore.QRect(350, 90, 131, 23))
        self.pushButtonRealizarChamada.setObjectName("pushButtonRealizarChamada")
        self.pushButtonFinalizarChamada = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonFinalizarChamada.setGeometry(QtCore.QRect(500, 90, 131, 23))
        self.pushButtonFinalizarChamada.setObjectName("pushButtonFinalizarChamada")
        self.line_3 = QtGui.QFrame(ui_MODEM_ConexaoCSD)
        self.line_3.setGeometry(QtCore.QRect(20, 130, 621, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.textEditDadosEnviados = QtGui.QTextEdit(ui_MODEM_ConexaoCSD)
        self.textEditDadosEnviados.setGeometry(QtCore.QRect(40, 170, 241, 131))
        self.textEditDadosEnviados.setObjectName("textEditDadosEnviados")
        self.textEditDadosRecebidos = QtGui.QTextEdit(ui_MODEM_ConexaoCSD)
        self.textEditDadosRecebidos.setGeometry(QtCore.QRect(380, 170, 241, 131))
        self.textEditDadosRecebidos.setObjectName("textEditDadosRecebidos")
        self.label_3 = QtGui.QLabel(ui_MODEM_ConexaoCSD)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(ui_MODEM_ConexaoCSD)
        self.label_4.setGeometry(QtCore.QRect(460, 150, 91, 16))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtGui.QFrame(ui_MODEM_ConexaoCSD)
        self.line_2.setGeometry(QtCore.QRect(320, 150, 16, 191))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButtonLimparEnviados = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonLimparEnviados.setGeometry(QtCore.QRect(50, 310, 91, 23))
        self.pushButtonLimparEnviados.setObjectName("pushButtonLimparEnviados")
        self.pushButtonEnviarDados = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonEnviarDados.setGeometry(QtCore.QRect(160, 310, 111, 23))
        self.pushButtonEnviarDados.setObjectName("pushButtonEnviarDados")
        self.pushButtonReceberDados = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonReceberDados.setGeometry(QtCore.QRect(390, 310, 111, 23))
        self.pushButtonReceberDados.setObjectName("pushButtonReceberDados")
        self.pushButtonLimparRecebidos = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonLimparRecebidos.setGeometry(QtCore.QRect(520, 310, 91, 23))
        self.pushButtonLimparRecebidos.setObjectName("pushButtonLimparRecebidos")
        self.line_4 = QtGui.QFrame(ui_MODEM_ConexaoCSD)
        self.line_4.setGeometry(QtCore.QRect(20, 350, 621, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButtonFechar = QtGui.QPushButton(ui_MODEM_ConexaoCSD)
        self.pushButtonFechar.setGeometry(QtCore.QRect(560, 370, 75, 23))
        self.pushButtonFechar.setObjectName("pushButtonFechar")

        self.retranslateUi(ui_MODEM_ConexaoCSD)
        QtCore.QMetaObject.connectSlotsByName(ui_MODEM_ConexaoCSD)

    def retranslateUi(self, ui_MODEM_ConexaoCSD):
        ui_MODEM_ConexaoCSD.setWindowTitle(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Serviço CSD - DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Configuração inicial para o modem que receberá a chamada csd", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAtivarConexao.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "eAtivarConexaoCsd", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Numero a ser discado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditTelefone.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "0xxTelefone", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRealizarChamada.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "eRealizarChamadaCsd", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFinalizarChamada.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "eFinalizarChamadaCsd", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Dados enviados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Dados recebidos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLimparEnviados.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Limpar Enviados", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviarDados.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "tEnviarDadosCsd", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReceberDados.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "rReceberDadosCsd", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLimparRecebidos.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Limpar Recebidos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_MODEM_ConexaoCSD", "Fechar", None, QtGui.QApplication.UnicodeUTF8))

