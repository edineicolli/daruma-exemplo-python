# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_rinfoestendida.ui'
#
# Created: Mon Nov 24 22:26:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
from ctypes import create_string_buffer

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_rInfoEstendida(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_rInfoEstendida, self).__init__()

        self.setupUi(self)

        self.comboBoxIndice.addItem("Selecione...")
        self.comboBoxIndice.addItem("1")
        self.comboBoxIndice.addItem("2")
        self.comboBoxIndice.addItem("3")
        self.comboBoxIndice.addItem("4")
        self.comboBoxIndice.addItem("5")

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Definiçao do Tamanho do Vetor de Recebimento da informação
        cRetorno = create_string_buffer(100)
        iIndice = self.comboBoxIndice.currentIndex()
        if(self.comboBoxIndice.currentIndex()==0):
            QMessageBox.warning(self,"DarumaFramework - Qt C++","Selecione o Indice!")
        else:
             # Execuçao do Método de Retorno da Informação*** */
            # pydaruma
            #tratarRetornoFiscal(rInfoEstentida_ECF_Daruma(iIndice,cRetorno),self)
            StrRetorno = cRetorno
            # Devolve o retorno da DLL para o campo de texto
            QMessageBox.information(self,"DarumaFramework - Qt C++","Informaçao: "+ StrRetorno)


    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_rInfoEstendida):
        ui_FISCAL_rInfoEstendida.setObjectName("ui_FISCAL_rInfoEstendida")
        ui_FISCAL_rInfoEstendida.resize(194, 98)
        ui_FISCAL_rInfoEstendida.setMaximumSize(QtCore.QSize(194, 100))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_rInfoEstendida)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_rInfoEstendida)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBoxIndice = QtGui.QComboBox(ui_FISCAL_rInfoEstendida)
        self.comboBoxIndice.setObjectName("comboBoxIndice")
        self.horizontalLayout_2.addWidget(self.comboBoxIndice)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(ui_FISCAL_rInfoEstendida)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_rInfoEstendida)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_rInfoEstendida)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_rInfoEstendida)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_rInfoEstendida)

    def retranslateUi(self, ui_FISCAL_rInfoEstendida):
        ui_FISCAL_rInfoEstendida.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_rInfoEstendida", "Método rInfoEstendida_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_rInfoEstendida", "Indice:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_rInfoEstendida", "Indice de 01 até 05", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_rInfoEstendida", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_rInfoEstendida", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

