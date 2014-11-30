# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icflancardescontoitem.ui'
#
# Created: Mon Nov 24 22:25:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFLancarDescontoItem(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFLancarDescontoItem, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFLancarDescontoItem):
        ui_FISCAL_iCFLancarDescontoItem.setObjectName("ui_FISCAL_iCFLancarDescontoItem")
        ui_FISCAL_iCFLancarDescontoItem.resize(306, 167)
        ui_FISCAL_iCFLancarDescontoItem.setMinimumSize(QtCore.QSize(306, 167))
        ui_FISCAL_iCFLancarDescontoItem.setMaximumSize(QtCore.QSize(306, 167))
        self.layoutWidget = QtGui.QWidget(ui_FISCAL_iCFLancarDescontoItem)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 288, 67))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonEnviar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancelar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.layoutWidget_2 = QtGui.QWidget(ui_FISCAL_iCFLancarDescontoItem)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 288, 76))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelNumeroItem = QtGui.QLabel(self.layoutWidget_2)
        self.labelNumeroItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNumeroItem.setObjectName("labelNumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelNumeroItem)
        self.lineEditNumeroItem = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditNumeroItem.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditNumeroItem.setMaxLength(3)
        self.lineEditNumeroItem.setObjectName("lineEditNumeroItem")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNumeroItem)
        self.labelTipoDesconto = QtGui.QLabel(self.layoutWidget_2)
        self.labelTipoDesconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTipoDesconto.setObjectName("labelTipoDesconto")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelTipoDesconto)
        self.comboBoxTipoDesconto = QtGui.QComboBox(self.layoutWidget_2)
        self.comboBoxTipoDesconto.setMinimumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoDesconto.setMaximumSize(QtCore.QSize(81, 20))
        self.comboBoxTipoDesconto.setObjectName("comboBoxTipoDesconto")
        self.comboBoxTipoDesconto.addItem("")
        self.comboBoxTipoDesconto.addItem("")
        self.comboBoxTipoDesconto.addItem("")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxTipoDesconto)
        self.labelValorDesconto = QtGui.QLabel(self.layoutWidget_2)
        self.labelValorDesconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorDesconto.setObjectName("labelValorDesconto")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelValorDesconto)
        self.lineEditValorDesconto = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditValorDesconto.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditValorDesconto.setMaxLength(10)
        self.lineEditValorDesconto.setObjectName("lineEditValorDesconto")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditValorDesconto)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.retranslateUi(ui_FISCAL_iCFLancarDescontoItem)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFLancarDescontoItem)

    def retranslateUi(self, ui_FISCAL_iCFLancarDescontoItem):
        ui_FISCAL_iCFLancarDescontoItem.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "iCFLancarDesconto_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "Número Item: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNumeroItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTipoDesconto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "Tipo Desconto: ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDesconto.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDesconto.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "D$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDesconto.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "D%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorDesconto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "Valor Desconto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorDesconto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFLancarDescontoItem", "1,00", None, QtGui.QApplication.UnicodeUTF8))

