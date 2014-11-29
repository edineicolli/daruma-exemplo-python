# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icflancaracrescimoultimoitem.ui'
#
# Created: Mon Nov 24 22:25:47 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFLancarAcrescimoUltimoItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFLancarAcrescimoUltimoItem, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFLancarAcrescimoUltimoItem):
        ui_FISCAL_iCFLancarAcrescimoUltimoItem.setObjectName("ui_FISCAL_iCFLancarAcrescimoUltimoItem")
        ui_FISCAL_iCFLancarAcrescimoUltimoItem.resize(267, 117)
        ui_FISCAL_iCFLancarAcrescimoUltimoItem.setMinimumSize(QtCore.QSize(267, 117))
        ui_FISCAL_iCFLancarAcrescimoUltimoItem.setMaximumSize(QtCore.QSize(267, 117))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.labelTipoAcrescimo = QtGui.QLabel(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.labelTipoAcrescimo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTipoAcrescimo.setObjectName("labelTipoAcrescimo")
        self.gridLayout.addWidget(self.labelTipoAcrescimo, 0, 1, 1, 1)
        self.comboBoxTipoAcrescimo = QtGui.QComboBox(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.comboBoxTipoAcrescimo.setMinimumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoAcrescimo.setMaximumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoAcrescimo.setObjectName("comboBoxTipoAcrescimo")
        self.comboBoxTipoAcrescimo.addItem("")
        self.comboBoxTipoAcrescimo.addItem("")
        self.comboBoxTipoAcrescimo.addItem("")
        self.gridLayout.addWidget(self.comboBoxTipoAcrescimo, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.labelValorAcrescimo = QtGui.QLabel(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.labelValorAcrescimo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorAcrescimo.setObjectName("labelValorAcrescimo")
        self.gridLayout.addWidget(self.labelValorAcrescimo, 1, 1, 1, 1)
        self.lineEditValorAcrescimo = QtGui.QLineEdit(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.lineEditValorAcrescimo.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditValorAcrescimo.setMaxLength(10)
        self.lineEditValorAcrescimo.setObjectName("lineEditValorAcrescimo")
        self.gridLayout.addWidget(self.lineEditValorAcrescimo, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFLancarAcrescimoUltimoItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFLancarAcrescimoUltimoItem)

    def retranslateUi(self, ui_FISCAL_iCFLancarAcrescimoUltimoItem):
        ui_FISCAL_iCFLancarAcrescimoUltimoItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "Método iCFLancarAcrescimoUltimoItem", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTipoAcrescimo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "Tipo Acréscimo: ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcrescimo.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcrescimo.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "A$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoAcrescimo.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "A%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorAcrescimo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "Valor Acréscimo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorAcrescimo.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarAcrescimoUltimoItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

