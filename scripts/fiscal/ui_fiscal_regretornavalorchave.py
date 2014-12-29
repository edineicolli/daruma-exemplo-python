# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_regretornavalorchave.ui'
#
# Created: Mon Nov 24 22:26:20 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_regRetornaValorChave(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_regRetornaValorChave, self).__init__()

        self.setupUi(self)

        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        pass

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_regRetornaValorChave):
        ui_FISCAL_regRetornaValorChave.setObjectName("ui_FISCAL_regRetornaValorChave")
        ui_FISCAL_regRetornaValorChave.resize(341, 173)
        ui_FISCAL_regRetornaValorChave.setMaximumSize(QtCore.QSize(341, 173))
        self.verticalLayout_2 = QtGui.QVBoxLayout(ui_FISCAL_regRetornaValorChave)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(ui_FISCAL_regRetornaValorChave)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEditProduto = QtGui.QLineEdit(ui_FISCAL_regRetornaValorChave)
        self.lineEditProduto.setMaximumSize(QtCore.QSize(100, 100))
        self.lineEditProduto.setObjectName("lineEditProduto")
        self.horizontalLayout_4.addWidget(self.lineEditProduto)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(ui_FISCAL_regRetornaValorChave)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEditChave = QtGui.QLineEdit(ui_FISCAL_regRetornaValorChave)
        self.lineEditChave.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditChave.setObjectName("lineEditChave")
        self.horizontalLayout_3.addWidget(self.lineEditChave)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(ui_FISCAL_regRetornaValorChave)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelRetorno = QtGui.QLabel(ui_FISCAL_regRetornaValorChave)
        self.labelRetorno.setText("")
        self.labelRetorno.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRetorno.setObjectName("labelRetorno")
        self.horizontalLayout_2.addWidget(self.labelRetorno)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_regRetornaValorChave)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_regRetornaValorChave)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_regRetornaValorChave)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_regRetornaValorChave)

    def retranslateUi(self, ui_FISCAL_regRetornaValorChave):
        ui_FISCAL_regRetornaValorChave.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_regRetornaValorChave", "Método regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_regRetornaValorChave", "Produto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_regRetornaValorChave", "Chave:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_regRetornaValorChave", "Valor Retornado:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_regRetornaValorChave", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_regRetornaValorChave", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

