# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfvender.ui'
#
# Created: Mon Nov 24 22:25:50 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_iCFVender(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFVender, self).__init__()

        self.setupUi(self)

    def setupUi(self, ui_FISCAL_iCFVender):
        ui_FISCAL_iCFVender.setObjectName("ui_FISCAL_iCFVender")
        ui_FISCAL_iCFVender.resize(309, 296)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFVender)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Aliquota = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.label_Aliquota.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Aliquota.setObjectName("label_Aliquota")
        self.gridLayout.addWidget(self.label_Aliquota, 0, 0, 1, 1)
        self.lineEditAliquota = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditAliquota.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditAliquota.setMaxLength(5)
        self.lineEditAliquota.setObjectName("lineEditAliquota")
        self.gridLayout.addWidget(self.lineEditAliquota, 0, 1, 1, 1)
        self.label_Quantidade = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.label_Quantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Quantidade.setObjectName("label_Quantidade")
        self.gridLayout.addWidget(self.label_Quantidade, 1, 0, 1, 1)
        self.lineEditQuantidade = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditQuantidade.setMaximumSize(QtCore.QSize(80, 25))
        self.lineEditQuantidade.setObjectName("lineEditQuantidade")
        self.gridLayout.addWidget(self.lineEditQuantidade, 1, 1, 1, 1)
        self.labelValorUnitario = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.labelValorUnitario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorUnitario.setObjectName("labelValorUnitario")
        self.gridLayout.addWidget(self.labelValorUnitario, 2, 0, 1, 1)
        self.lineEditValorUnit = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditValorUnit.setMaximumSize(QtCore.QSize(80, 25))
        self.lineEditValorUnit.setObjectName("lineEditValorUnit")
        self.gridLayout.addWidget(self.lineEditValorUnit, 2, 1, 1, 1)
        self.labelTipoDescAcres = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.labelTipoDescAcres.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTipoDescAcres.setObjectName("labelTipoDescAcres")
        self.gridLayout.addWidget(self.labelTipoDescAcres, 3, 0, 1, 1)
        self.comboBoxTipoDescAcres = QtGui.QComboBox(ui_FISCAL_iCFVender)
        self.comboBoxTipoDescAcres.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBoxTipoDescAcres.setObjectName("comboBoxTipoDescAcres")
        self.comboBoxTipoDescAcres.addItem("")
        self.comboBoxTipoDescAcres.addItem("")
        self.comboBoxTipoDescAcres.addItem("")
        self.comboBoxTipoDescAcres.addItem("")
        self.gridLayout.addWidget(self.comboBoxTipoDescAcres, 3, 1, 1, 1)
        self.labelValorDescAcresc = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.labelValorDescAcresc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelValorDescAcresc.setObjectName("labelValorDescAcresc")
        self.gridLayout.addWidget(self.labelValorDescAcresc, 4, 0, 1, 1)
        self.lineEditValorDescAcres = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditValorDescAcres.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEditValorDescAcres.setObjectName("lineEditValorDescAcres")
        self.gridLayout.addWidget(self.lineEditValorDescAcres, 4, 1, 1, 1)
        self.labelCodigoItem = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.labelCodigoItem.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCodigoItem.setObjectName("labelCodigoItem")
        self.gridLayout.addWidget(self.labelCodigoItem, 5, 0, 1, 1)
        self.lineEditCodItem = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditCodItem.setMaximumSize(QtCore.QSize(100, 25))
        self.lineEditCodItem.setMaxLength(14)
        self.lineEditCodItem.setObjectName("lineEditCodItem")
        self.gridLayout.addWidget(self.lineEditCodItem, 5, 1, 1, 1)
        self.labelUnidadeMedida = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.labelUnidadeMedida.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelUnidadeMedida.setObjectName("labelUnidadeMedida")
        self.gridLayout.addWidget(self.labelUnidadeMedida, 6, 0, 1, 1)
        self.lineEditUnidade = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditUnidade.setMaximumSize(QtCore.QSize(50, 25))
        self.lineEditUnidade.setMaxLength(3)
        self.lineEditUnidade.setObjectName("lineEditUnidade")
        self.gridLayout.addWidget(self.lineEditUnidade, 6, 1, 1, 1)
        self.labelDescricaoProduto = QtGui.QLabel(ui_FISCAL_iCFVender)
        self.labelDescricaoProduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDescricaoProduto.setObjectName("labelDescricaoProduto")
        self.gridLayout.addWidget(self.labelDescricaoProduto, 7, 0, 1, 1)
        self.lineEditDescricao = QtGui.QLineEdit(ui_FISCAL_iCFVender)
        self.lineEditDescricao.setMaxLength(200)
        self.lineEditDescricao.setObjectName("lineEditDescricao")
        self.gridLayout.addWidget(self.lineEditDescricao, 7, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pushButtoniCFVender = QtGui.QPushButton(ui_FISCAL_iCFVender)
        self.pushButtoniCFVender.setObjectName("pushButtoniCFVender")
        self.horizontalLayout_8.addWidget(self.pushButtoniCFVender)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFVender)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_8.addWidget(self.pushButtonCancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(ui_FISCAL_iCFVender)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFVender)

    def retranslateUi(self, ui_FISCAL_iCFVender):
        ui_FISCAL_iCFVender.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "Método iCFVender_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Aliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "                  Alíquota:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAliquota.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "I1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Quantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "             Quantidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditQuantidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorUnitario.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "           Valor Unitario:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorUnit.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "1,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTipoDescAcres.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "    Tipo Desc/Acresc:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDescAcres.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFVender", "D%", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDescAcres.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFVender", "D$", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDescAcres.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFVender", "A%", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDescAcres.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCFVender", "A$", None, QtGui.QApplication.UnicodeUTF8))
        self.labelValorDescAcresc.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "    Valor Desc/Acresc:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditValorDescAcres.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "0,00", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCodigoItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "        Código do Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditCodItem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "123456789012", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUnidadeMedida.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "  Unidade de Medida:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditUnidade.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "UN", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescricaoProduto.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "   Descr. do Produto: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDescricao.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "REFRIGERANTE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtoniCFVender.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFVender", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
