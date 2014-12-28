# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfvendersemdesc.ui'
#
# Created: Mon Nov 24 22:25:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFVenderSemDesc_ECF_Daruma


class Ui_ui_FISCAL_iCFVenderSemDesc(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFVenderSemDesc, self).__init__()

        self.setupUi(self)
        self.pushButtoniCFVender_2.clicked.connect(self.on_pushButtoniCFVender_2_clicked)
        self.pushButtonCancelar_2.clicked.connect(self.on_pushButtonCancelar_2_clicked)
        self.pushButtoniCFVender_3.clicked.connect(self.on_pushButtoniCFVender_3_clicked)
        self.pushButtonCancelar_3.clicked.connect(self.on_pushButtonCancelar_3_clicked)

    def on_pushButtoniCFVender_2_clicked(self):
        StrAliquota = self.lineEditAliquota.text()
        StrQuantidade = self.lineEditQuantidade.text()
        StrValorUnit = self.lineEditValotUnit.text()
        StrCodItem = self.lineEditCodItem.text()
        StrUnidade = self.lineEditUnidade.text()
        StrDescricao = self.lineEditDescricao.text()

        iCFVenderSemDesc_ECF_Daruma(StrAliquota,StrQuantidade,StrValorUnit,StrCodItem,StrUnidade,StrDescricao)
        #tratarRetornoFiscal(iCFVenderSemDesc_ECF_Daruma(StrAliquota,StrQuantidade,StrValorUnit,StrCodItem,StrUnidade,StrDescricao), self)

    def on_pushButtonCancelar_2_clicked(self):
        self.close()

    def on_pushButtoniCFVender_3_clicked(self):
        pass

    def on_pushButtonCancelar_3_clicked(self):
        pass

    def setupUi(self, ui_FISCAL_iCFVenderSemDesc):
        ui_FISCAL_iCFVenderSemDesc.setObjectName("ui_FISCAL_iCFVenderSemDesc")
        ui_FISCAL_iCFVenderSemDesc.resize(245, 224)
        ui_FISCAL_iCFVenderSemDesc.setMinimumSize(QtCore.QSize(245, 224))
        ui_FISCAL_iCFVenderSemDesc.setMaximumSize(QtCore.QSize(245, 224))
        self.layoutWidget3 = QtGui.QWidget(ui_FISCAL_iCFVenderSemDesc)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 170, 204, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButtoniCFVender_2 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButtoniCFVender_2.setObjectName("pushButtoniCFVender_2")
        self.horizontalLayout_9.addWidget(self.pushButtoniCFVender_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.pushButtonCancelar_2 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButtonCancelar_2.setObjectName("pushButtonCancelar_2")
        self.horizontalLayout_9.addWidget(self.pushButtonCancelar_2)
        self.layoutWidget4 = QtGui.QWidget(ui_FISCAL_iCFVenderSemDesc)
        self.layoutWidget4.setGeometry(QtCore.QRect(150, 480, 204, 25))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButtoniCFVender_3 = QtGui.QPushButton(self.layoutWidget4)
        self.pushButtoniCFVender_3.setObjectName("pushButtoniCFVender_3")
        self.horizontalLayout_10.addWidget(self.pushButtoniCFVender_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.pushButtonCancelar_3 = QtGui.QPushButton(self.layoutWidget4)
        self.pushButtonCancelar_3.setObjectName("pushButtonCancelar_3")
        self.horizontalLayout_10.addWidget(self.pushButtonCancelar_3)
        self.layoutWidget5 = QtGui.QWidget(ui_FISCAL_iCFVenderSemDesc)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 10, 225, 154))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelAliquota = QtGui.QLabel(self.layoutWidget5)
        self.labelAliquota.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAliquota.setWordWrap(False)
        self.labelAliquota.setOpenExternalLinks(False)
        self.labelAliquota.setObjectName("labelAliquota")
        self.verticalLayout.addWidget(self.labelAliquota)
        self.labelQuantidade = QtGui.QLabel(self.layoutWidget5)
        self.labelQuantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelQuantidade.setWordWrap(False)
        self.labelQuantidade.setOpenExternalLinks(False)
        self.labelQuantidade.setObjectName("labelQuantidade")
        self.verticalLayout.addWidget(self.labelQuantidade)
        self.labelValorUnit = QtGui.QLabel(self.layoutWidget5)
        self.labelValorUnit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorUnit.setWordWrap(False)
        self.labelValorUnit.setOpenExternalLinks(False)
        self.labelValorUnit.setObjectName("labelValorUnit")
        self.verticalLayout.addWidget(self.labelValorUnit)
        self.labelCodItem = QtGui.QLabel(self.layoutWidget5)
        self.labelCodItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCodItem.setWordWrap(False)
        self.labelCodItem.setOpenExternalLinks(False)
        self.labelCodItem.setObjectName("labelCodItem")
        self.verticalLayout.addWidget(self.labelCodItem)
        self.labelUnidade = QtGui.QLabel(self.layoutWidget5)
        self.labelUnidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelUnidade.setWordWrap(False)
        self.labelUnidade.setOpenExternalLinks(False)
        self.labelUnidade.setObjectName("labelUnidade")
        self.verticalLayout.addWidget(self.labelUnidade)
        self.labelDescricao = QtGui.QLabel(self.layoutWidget5)
        self.labelDescricao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDescricao.setWordWrap(False)
        self.labelDescricao.setOpenExternalLinks(False)
        self.labelDescricao.setObjectName("labelDescricao")
        self.verticalLayout.addWidget(self.labelDescricao)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEditAliquota = QtGui.QLineEdit(self.layoutWidget5)
        self.lineEditAliquota.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditAliquota.setMaxLength(5)
        self.lineEditAliquota.setObjectName("lineEditAliquota")
        self.verticalLayout_5.addWidget(self.lineEditAliquota)
        self.lineEditQuantidade = QtGui.QLineEdit(self.layoutWidget5)
        self.lineEditQuantidade.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        self.verticalLayout_5.addWidget(self.lineEditQuantidade)
        self.lineEditValotUnit = QtGui.QLineEdit(self.layoutWidget5)
        self.lineEditValotUnit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEditValotUnit.setObjectName("lineEditValotUnit")
        self.verticalLayout_5.addWidget(self.lineEditValotUnit)
        self.lineEditCodItem = QtGui.QLineEdit(self.layoutWidget5)
        self.lineEditCodItem.setMaxLength(14)
        self.lineEditCodItem.setObjectName("lineEditCodItem")
        self.verticalLayout_5.addWidget(self.lineEditCodItem)
        self.lineEditUnidade = QtGui.QLineEdit(self.layoutWidget5)
        self.lineEditUnidade.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEditUnidade.setMaxLength(3)
        self.lineEditUnidade.setObjectName("lineEditUnidade")
        self.verticalLayout_5.addWidget(self.lineEditUnidade)
        self.lineEditDescricao = QtGui.QLineEdit(self.layoutWidget5)
        self.lineEditDescricao.setCursorPosition(0)
        self.lineEditDescricao.setObjectName("lineEditDescricao")
        self.verticalLayout_5.addWidget(self.lineEditDescricao)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.retranslateUi(ui_FISCAL_iCFVenderSemDesc)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFVenderSemDesc)

    def retranslateUi(self, ui_FISCAL_iCFVenderSemDesc):
        ui_FISCAL_iCFVenderSemDesc.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtoniCFVender_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtoniCFVender_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Alíquota:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Quantidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorUnit.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Valor Unitário:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCodItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Código Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUnidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Unidade Medida:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescricao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "I1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValotUnit.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCodItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "1234567890", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditUnidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "UN", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDescricao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderSemDesc", "REFRIGERANTE", None, QtGui.QApplication.UnicodeUTF8))

