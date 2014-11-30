# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_loopingstatusdocumento.ui'
#
# Created: Mon Nov 24 22:25:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_loopingstatusdocumento(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_loopingstatusdocumento, self).__init__()

        self.setupUi(self)
        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):
        pass

    def setupUi(self, ui_dual_loopingstatusdocumento):
        ui_dual_loopingstatusdocumento.setObjectName("ui_dual_loopingstatusdocumento")
        ui_dual_loopingstatusdocumento.resize(309, 123)
        self.lineEditQuantidade = QtGui.QLineEdit(ui_dual_loopingstatusdocumento)
        self.lineEditQuantidade.setGeometry(QtCore.QRect(160, 10, 141, 20))
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        self.label = QtGui.QLabel(ui_dual_loopingstatusdocumento)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_dual_loopingstatusdocumento)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_loopingstatusdocumento)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(240, 90, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_loopingstatusdocumento)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(170, 90, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.lineEditStatus = QtGui.QTextEdit(ui_dual_loopingstatusdocumento)
        self.lineEditStatus.setGeometry(QtCore.QRect(10, 60, 293, 25))
        self.lineEditStatus.setObjectName("lineEditStatus")

        self.retranslateUi(ui_dual_loopingstatusdocumento)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_loopingstatusdocumento)

    def retranslateUi(self, ui_dual_loopingstatusdocumento):
        ui_dual_loopingstatusdocumento.setWindowTitle(QtGui.QApplication.translate("ui_dual_loopingstatusdocumento", "Método rStatusDocumento_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_loopingstatusdocumento", "Qual a quantidade do looping?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_dual_loopingstatusdocumento", "Status Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_loopingstatusdocumento", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_loopingstatusdocumento", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

