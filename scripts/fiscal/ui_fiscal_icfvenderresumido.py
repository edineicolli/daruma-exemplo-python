# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfvenderresumido.ui'
#
# Created: Mon Nov 24 22:25:51 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFVenderResumido_ECF_Daruma


class Ui_ui_FISCAL_iCFVenderResumido(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFVenderResumido, self).__init__()

        self.setupUi(self)
        self.pushButtoniCFVender_2.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar_2.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
         StrAliquota = self.lineEditAliquota.text()
         StrValorUnit = self.lineEditValotUnit.text()
         StrCodItem = self.lineEditCodItem.text()
         StrDescricao = self.lineEditDescricao.text()

         iCFVenderResumido_ECF_Daruma(StrAliquota,StrValorUnit,StrCodItem,StrDescricao)
         #tratarRetornoFsical(iCFVenderResumido_ECF_Daruma(StrAliquota,StrValorUnit,StrCodItem,StrDescricao), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFVenderResumido):
        ui_FISCAL_iCFVenderResumido.setObjectName("ui_FISCAL_iCFVenderResumido")
        ui_FISCAL_iCFVenderResumido.resize(251, 198)
        ui_FISCAL_iCFVenderResumido.setMinimumSize(QtCore.QSize(251, 198))
        ui_FISCAL_iCFVenderResumido.setMaximumSize(QtCore.QSize(251, 198))
        self.layoutWidget3 = QtGui.QWidget(ui_FISCAL_iCFVenderResumido)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 150, 204, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtoniCFVender_2 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButtoniCFVender_2.setObjectName("pushButtoniCFVender_2")
        self.horizontalLayout.addWidget(self.pushButtoniCFVender_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCancelar_2 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButtonCancelar_2.setObjectName("pushButtonCancelar_2")
        self.horizontalLayout.addWidget(self.pushButtonCancelar_2)
        self.layoutWidget4 = QtGui.QWidget(ui_FISCAL_iCFVenderResumido)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 210, 102))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelAliquota = QtGui.QLabel(self.layoutWidget4)
        self.labelAliquota.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAliquota.setWordWrap(False)
        self.labelAliquota.setOpenExternalLinks(False)
        self.labelAliquota.setObjectName("labelAliquota")
        self.gridLayout.addWidget(self.labelAliquota, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditAliquota = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEditAliquota.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditAliquota.setMaxLength(5)
        self.lineEditAliquota.setCursorPosition(0)
        self.lineEditAliquota.setObjectName("lineEditAliquota")
        self.verticalLayout.addWidget(self.lineEditAliquota)
        self.lineEditValotUnit = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEditValotUnit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEditValotUnit.setMaxLength(11)
        self.lineEditValotUnit.setCursorPosition(0)
        self.lineEditValotUnit.setObjectName("lineEditValotUnit")
        self.verticalLayout.addWidget(self.lineEditValotUnit)
        self.lineEditCodItem = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEditCodItem.setMaxLength(12)
        self.lineEditCodItem.setCursorPosition(12)
        self.lineEditCodItem.setObjectName("lineEditCodItem")
        self.verticalLayout.addWidget(self.lineEditCodItem)
        self.lineEditDescricao = QtGui.QLineEdit(self.layoutWidget4)
        self.lineEditDescricao.setInputMask("")
        self.lineEditDescricao.setMaxLength(200)
        self.lineEditDescricao.setCursorPosition(12)
        self.lineEditDescricao.setObjectName("lineEditDescricao")
        self.verticalLayout.addWidget(self.lineEditDescricao)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 4, 1)
        self.labelValorUnit = QtGui.QLabel(self.layoutWidget4)
        self.labelValorUnit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorUnit.setWordWrap(False)
        self.labelValorUnit.setOpenExternalLinks(False)
        self.labelValorUnit.setObjectName("labelValorUnit")
        self.gridLayout.addWidget(self.labelValorUnit, 1, 0, 1, 1)
        self.labelCodItem = QtGui.QLabel(self.layoutWidget4)
        self.labelCodItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCodItem.setWordWrap(False)
        self.labelCodItem.setOpenExternalLinks(False)
        self.labelCodItem.setObjectName("labelCodItem")
        self.gridLayout.addWidget(self.labelCodItem, 2, 0, 1, 1)
        self.labelDescricao = QtGui.QLabel(self.layoutWidget4)
        self.labelDescricao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDescricao.setWordWrap(False)
        self.labelDescricao.setOpenExternalLinks(False)
        self.labelDescricao.setObjectName("labelDescricao")
        self.gridLayout.addWidget(self.labelDescricao, 3, 0, 1, 1)

        self.retranslateUi(ui_FISCAL_iCFVenderResumido)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFVenderResumido)

    def retranslateUi(self, ui_FISCAL_iCFVenderResumido):
        ui_FISCAL_iCFVenderResumido.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Método iCFVenderResumido_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtoniCFVender_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Alíquota:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "I1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValotUnit.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCodItem.setInputMask(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "123456789012; ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCodItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "123456789012", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDescricao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "REFRIGERANTE", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorUnit.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Valor Unitário:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCodItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Código Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescricao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVenderResumido", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))

