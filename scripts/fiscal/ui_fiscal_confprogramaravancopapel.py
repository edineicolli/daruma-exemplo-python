# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_confprogramaravancopapel.ui'
#
# Created: Mon Nov 24 22:25:22 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import confProgramarAvancoPapel_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_confProgramarAvancoPapel(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_confProgramarAvancoPapel, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        # Declaracao de variaveis de recebimento da UI.
        StrLinhasGui = self.lineEditLinhasGui.text()
        StrSepDocs = self.lineEditSepEntreDocumentos.text()
        StrSepLinhas = self.lineEditSepEntreLinhas.text()

        StrStatusCliche = ""
        StrStatusGui = ""

        if(self.radioButtonClicheDes.isChecked()):
            StrStatusCliche = "1"
        if(self.radioButtonClicheHab.isChecked()):
            StrStatusCliche = "0"
        if(self.radioButtonGuiDes.isChecked()):
            StrStatusGui = "0"
        if(self.radioButtonGuiHab.isChecked()):
            StrStatusGui = "1"

        tratarRetornoFiscal(confProgramarAvancoPapel_ECF_Daruma(StrSepLinhas,StrSepDocs,StrLinhasGui,StrStatusGui,StrStatusCliche), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_confProgramarAvancoPapel):
        ui_FISCAL_confProgramarAvancoPapel.setObjectName("ui_FISCAL_confProgramarAvancoPapel")
        ui_FISCAL_confProgramarAvancoPapel.resize(297, 281)
        ui_FISCAL_confProgramarAvancoPapel.setMinimumSize(QtCore.QSize(297, 281))
        ui_FISCAL_confProgramarAvancoPapel.setMaximumSize(QtCore.QSize(297, 281))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_confProgramarAvancoPapel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ui_FISCAL_confProgramarAvancoPapel)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditSepEntreLinhas = QtGui.QLineEdit(ui_FISCAL_confProgramarAvancoPapel)
        self.lineEditSepEntreLinhas.setMaximumSize(QtCore.QSize(31, 20))
        self.lineEditSepEntreLinhas.setMaxLength(3)
        self.lineEditSepEntreLinhas.setObjectName("lineEditSepEntreLinhas")
        self.gridLayout.addWidget(self.lineEditSepEntreLinhas, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ui_FISCAL_confProgramarAvancoPapel)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditSepEntreDocumentos = QtGui.QLineEdit(ui_FISCAL_confProgramarAvancoPapel)
        self.lineEditSepEntreDocumentos.setMaximumSize(QtCore.QSize(31, 20))
        self.lineEditSepEntreDocumentos.setObjectName("lineEditSepEntreDocumentos")
        self.gridLayout.addWidget(self.lineEditSepEntreDocumentos, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ui_FISCAL_confProgramarAvancoPapel)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditLinhasGui = QtGui.QLineEdit(ui_FISCAL_confProgramarAvancoPapel)
        self.lineEditLinhasGui.setMaximumSize(QtCore.QSize(31, 20))
        self.lineEditLinhasGui.setObjectName("lineEditLinhasGui")
        self.gridLayout.addWidget(self.lineEditLinhasGui, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_confProgramarAvancoPapel)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonGuiDes = QtGui.QRadioButton(self.groupBox)
        self.radioButtonGuiDes.setObjectName("radioButtonGuiDes")
        self.verticalLayout_2.addWidget(self.radioButtonGuiDes)
        self.radioButtonGuiHab = QtGui.QRadioButton(self.groupBox)
        self.radioButtonGuiHab.setChecked(True)
        self.radioButtonGuiHab.setObjectName("radioButtonGuiHab")
        self.verticalLayout_2.addWidget(self.radioButtonGuiHab)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ui_FISCAL_confProgramarAvancoPapel)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButtonClicheHab = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonClicheHab.setObjectName("radioButtonClicheHab")
        self.verticalLayout_3.addWidget(self.radioButtonClicheHab)
        self.radioButtonClicheDes = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonClicheDes.setChecked(True)
        self.radioButtonClicheDes.setObjectName("radioButtonClicheDes")
        self.verticalLayout_3.addWidget(self.radioButtonClicheDes)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_confProgramarAvancoPapel)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_confProgramarAvancoPapel)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_confProgramarAvancoPapel)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_confProgramarAvancoPapel)

    def retranslateUi(self, ui_FISCAL_confProgramarAvancoPapel):
        ui_FISCAL_confProgramarAvancoPapel.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Método ConfProgramarAvancoPapel_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Separaçao entre linhas ( em Dots 25/216):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSepEntreLinhas.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Separaçao entre Documentos ( em linhas ):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSepEntreDocumentos.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Linhas de Acionamento da Guilhotina ( em linhas ):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditLinhasGui.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Guilhotina:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonGuiDes.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "0 - Desabilitada", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonGuiHab.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "1 - Habilitada", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Clichê:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonClicheHab.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "0 - Com impressao antecipada", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonClicheDes.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "1 - Sem impressao antecipada", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_confProgramarAvancoPapel", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

