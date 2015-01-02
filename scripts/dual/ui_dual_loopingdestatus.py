# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dual_loopingdestatus.ui'
#
# Created: Mon Nov 24 22:25:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import rStatusImpressora_DUAL_DarumaFramework


class Ui_ui_dual_loopingdestatus(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_dual_loopingdestatus, self).__init__()

        self.setupUi(self)
        self.pushButtonCancelar.clicked.connect(self.on_Cancelar_clicked)
        self.pushButtonEnviar.clicked.connect(self.on_Enviar_clicked)

    def on_Cancelar_clicked(self):
        self.close()

    def on_Enviar_clicked(self):

        sQtd = self.lineEditQuantidade.text() # recebe Quantidade de Looping do LineEdit
        iRetornoInicio = rStatusImpressora_DUAL_DarumaFramework()

        if (iRetornoInicio):
            for qnt in range(1, int(sQtd)):
                iRetorno = rStatusImpressora_DUAL_DarumaFramework()
                if iRetorno == 0:
                    self.lineEditStatus.setText("Retorno 0 - Erro de comunicação, não foi possível enviar o método.")
                    break
                elif iRetorno == 1:
                    self.lineEditStatus.setText("Retorno 1 - OK, Sucesso ao enviar o método.")
                    break
                elif iRetorno == -99:
                    self.lineEditStatus.setText("Retorno -99 - Método não executado, parâmetro inválido.")
                    break
                elif iRetorno == -1:
                    self.lineEditStatus.setText("Retorno -1 - Erro de atualização de Chave.")
                    break
                elif iRetorno == -2:
                    self.lineEditStatus.setText("Retorno -2 - Linhas e Colunas inválidas.")
                    break
                elif iRetorno == -4:
                    self.lineEditStatus.setText("Retorno -4 - A chave ou Valor no Arquivo do Registro(Registry) não foi encontada.")
                    break
                elif iRetorno == -27:
                    self.lineEditStatus.setText("Retorno -27 - Erro Genérico.")
                    break
                elif iRetorno == -50:
                    self.lineEditStatus.setText("Retorno -50 - Impressora OFF-LINE.")
                    break
                elif iRetorno == -51:
                    self.lineEditStatus.setText("Retorno -51 -  Impressora sem papel.")
                    break
                elif iRetorno == -52:
                    self.lineEditStatus.setText("Retorno -52 -  Impressora inicializando.")
                    break

            QMessageBox.information(self,"DarumaFramework - Python/Qt","Processo Concluido.")

        if (sQtd == ""):
            QMessageBox.information(self,"DarumaFramework - Python/Qt","Preencha todos os campos!")

    def setupUi(self, ui_dual_loopingdestatus):
        ui_dual_loopingdestatus.setObjectName("ui_dual_loopingdestatus")
        ui_dual_loopingdestatus.resize(309, 119)
        self.label = QtGui.QLabel(ui_dual_loopingdestatus)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ui_dual_loopingdestatus)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditQuantidade = QtGui.QLineEdit(ui_dual_loopingdestatus)
        self.lineEditQuantidade.setGeometry(QtCore.QRect(170, 10, 131, 20))
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        self.pushButtonCancelar = QtGui.QPushButton(ui_dual_loopingdestatus)
        self.pushButtonCancelar.setGeometry(QtCore.QRect(240, 90, 61, 23))
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.pushButtonEnviar = QtGui.QPushButton(ui_dual_loopingdestatus)
        self.pushButtonEnviar.setGeometry(QtCore.QRect(170, 90, 61, 23))
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.lineEditStatus = QtGui.QTextEdit(ui_dual_loopingdestatus)
        self.lineEditStatus.setGeometry(QtCore.QRect(8, 57, 293, 25))
        self.lineEditStatus.setObjectName("lineEditStatus")

        self.retranslateUi(ui_dual_loopingdestatus)
        QtCore.QMetaObject.connectSlotsByName(ui_dual_loopingdestatus)

    def retranslateUi(self, ui_dual_loopingdestatus):
        ui_dual_loopingdestatus.setWindowTitle(QtGui.QApplication.translate("ui_dual_loopingdestatus", "Método rStatusImpressora_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_dual_loopingdestatus", "Qual a quantidade do Looping?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_dual_loopingdestatus", "Status Impressora:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_dual_loopingdestatus", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_dual_loopingdestatus", "Enviar", None, QtGui.QApplication.UnicodeUTF8))

