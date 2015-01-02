# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_iautenticardocumento.ui'
#
# Created: Mon Nov 24 22:25:09 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import iAutenticarDocumento_DUAL_DarumaFramework
from scripts.dual.retornodual import tratarRetornoDUAL


class Ui_ui_dual_iautenticardocumento(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_iautenticardocumento, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

        self.lineEditLocal.setText("1")
        self.lineEditTexto.setText("<sn><c>DARUMA AUTENTICAÇÃO</c> (D:<dt></dt> H:<hr></hr>)</sn>")
        self.lineEditSegundos.setText("10")
        
    def on_pushButtonEnviar_clicked(self):
        if ((self.lineEditLocal.text()=="") or (self.lineEditTexto.text()=="") or (self.lineEditSegundos.text()=="")):
            QMessageBox.warning(self,"DarumaFramework - Python/Qt","Preencha todos os Campos!")
        else:
            Local = self.lineEditLocal.text()
            Texto = self.lineEditTexto.text()
            Segundos = self.lineEditSegundos.text()

            tratarRetornoDUAL(iAutenticarDocumento_DUAL_DarumaFramework(Texto, Local,Segundos), self)
    
    def on_pushButtonCancelar_clicked(self):
        self.close()
        

    def setupUi(self, ui_dual_iautenticardocumento):
        ui_dual_iautenticardocumento.setObjectName("ui_dual_iautenticardocumento")
        ui_dual_iautenticardocumento.resize(566, 161)
        self.label = QtGui.QLabel(ui_dual_iautenticardocumento)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_dual_iautenticardocumento)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 221, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(ui_dual_iautenticardocumento)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(ui_dual_iautenticardocumento)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 241, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditLocal = QtGui.QLineEdit(ui_dual_iautenticardocumento)
        self.lineEditLocal.setGeometry(QtCore.QRect(40, 10, 21, 20))
        self.lineEditLocal.setObjectName("lineEditLocal")
        self.lineEditTexto = QtGui.QLineEdit(ui_dual_iautenticardocumento)
        self.lineEditTexto.setGeometry(QtCore.QRect(130, 40, 421, 20))
        self.lineEditTexto.setObjectName("lineEditTexto")
        self.lineEditSegundos = QtGui.QLineEdit(ui_dual_iautenticardocumento)
        self.lineEditSegundos.setGeometry(QtCore.QRect(250, 80, 31, 20))
        self.lineEditSegundos.setObjectName("lineEditSegundos")
        self.label_5 = QtGui.QLabel(ui_dual_iautenticardocumento)
        self.label_5.setGeometry(QtCore.QRect(290, 80, 51, 16))
        self.label_5.setObjectName("label_5")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_iautenticardocumento)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(490, 120, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_iautenticardocumento)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(420, 120, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")

        self.retranslateUi(ui_dual_iautenticardocumento)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_iautenticardocumento)

    def retranslateUi(self, ui_dual_iautenticardocumento):
        ui_dual_iautenticardocumento.setWindowTitle(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Método iAutenticarDocumento_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "1(somente no doc) / 0(no doc e na bobina)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Texto da Autenticaçao:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Tempo de espera para o posicionamento do doc:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditLocal.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditTexto.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "<sn><c>DARUMA AUTENTICAÇÃO</c> (D:<dt></dt> H:<hr></hr>)</sn>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSegundos.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Segundos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_iautenticardocumento", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

