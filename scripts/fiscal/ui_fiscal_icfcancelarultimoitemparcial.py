# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfcancelarultimoitemparcial.ui'
#
# Created: Mon Nov 24 22:25:41 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFCancelarUltimoItemParcial(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFCancelarUltimoItemParcial, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFCancelarUltimoItemParcial):
        ui_FISCAL_iCFCancelarUltimoItemParcial.setObjectName("ui_FISCAL_iCFCancelarUltimoItemParcial")
        ui_FISCAL_iCFCancelarUltimoItemParcial.resize(197, 126)
        ui_FISCAL_iCFCancelarUltimoItemParcial.setMinimumSize(QtCore.QSize(197, 126))
        ui_FISCAL_iCFCancelarUltimoItemParcial.setMaximumSize(QtCore.QSize(197, 126))
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFCancelarUltimoItemParcial)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.labelQuantidade = QtGui.QLabel(ui_FISCAL_iCFCancelarUltimoItemParcial)
        self.labelQuantidade.setObjectName("labelQuantidade")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelQuantidade)
        self.lineEditQuantidade = QtGui.QLineEdit(ui_FISCAL_iCFCancelarUltimoItemParcial)
        self.lineEditQuantidade.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditQuantidade.setMaxLength(14)
        self.lineEditQuantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditQuantidade)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFCancelarUltimoItemParcial)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout.addWidget(self.pushButtonEnviar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFCancelarUltimoItemParcial)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ui_FISCAL_iCFCancelarUltimoItemParcial)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFCancelarUltimoItemParcial)

    def retranslateUi(self, ui_FISCAL_iCFCancelarUltimoItemParcial):
        ui_FISCAL_iCFCancelarUltimoItemParcial.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarUltimoItemParcial", "Método iCFCancelarUltimoItemParcial", None, QtGui.QApplication.UnicodeUTF8))
        self.labelQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarUltimoItemParcial", "Quantidade Item: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarUltimoItemParcial", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarUltimoItemParcial", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFCancelarUltimoItemParcial", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

