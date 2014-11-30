# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_rconsultastatusimpressora2.ui'
#
# Created: Mon Nov 24 22:25:14 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_dual_rconsultastatusimpressora2(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_rconsultastatusimpressora2, self).__init__()

        self.setupUi(self)
        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):
        pass

    def setupUi(self, ui_dual_rconsultastatusimpressora2):
        ui_dual_rconsultastatusimpressora2.setObjectName("ui_dual_rconsultastatusimpressora2")
        ui_dual_rconsultastatusimpressora2.resize(261, 125)
        self.centralwidget = QtGui.QWidget(ui_dual_rconsultastatusimpressora2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 30, 131, 16))
        self.label_3.setObjectName("label_3")
        self.pushButtonEnviar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(120, 80, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.pushButtonCancelar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(190, 80, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        ui_dual_rconsultastatusimpressora2.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ui_dual_rconsultastatusimpressora2)
        self.statusbar.setObjectName("statusbar")
        ui_dual_rconsultastatusimpressora2.setStatusBar(self.statusbar)

        self.retranslateUi(ui_dual_rconsultastatusimpressora2)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_rconsultastatusimpressora2)

    def retranslateUi(self, ui_dual_rconsultastatusimpressora2):
        ui_dual_rconsultastatusimpressora2.setWindowTitle(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora2", "Método rConsultaStatusImpressora_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora2", "Entre com o tipo da informaçao desejada:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora2", "0 - para receber valores", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora2", "1 - para receber texto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora2", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_rconsultastatusimpressora2", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

