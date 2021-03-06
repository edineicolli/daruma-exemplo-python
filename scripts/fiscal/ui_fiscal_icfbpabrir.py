# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_icfbpabrir.ui'
#
# Created: Mon Nov 24 22:25:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import iCFBPAbrir_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal


class Ui_ui_FISCAL_iCFBPAbrir(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_iCFBPAbrir, self).__init__()

        self.setupUi(self)
        self.pushButtonEnviar.clicked.connect(self.on_pushButtonEnviar_clicked)
        self.pushButtonCancelar.clicked.connect(self.on_pushButtonCancelar_clicked)

    def on_pushButtonEnviar_clicked(self):
        StrOrigem = self.lineEditOrigem.text()
        StrDestino = self.lineEditDestino.text()
        StrUFDestino = self.lineEditUFDestino.text()
        #QString UFOrigem = ui->lineEditUFOrigem->text()
        StrPrestadora = self.lineEditPrestadora.text()
        StrPercurso = self.lineEditPercurso.text()
        StrPlataforma = self.lineEditPlataforma.text()
        StrPoltrona = self.lineEditPoltrona.text()
        StrDTEmbarque = self.lineEditDTEmbarque.text()
        StrRGPassageiro = self.lineEditRGPassageiro.text()
        StrNomePassageiro = self.lineEditNomePassageiro.text()
        StrEndPassageiro = self.lineEditEndPassageiro.text()
        iModalidade = self.comboBoxModalidade.currentIndex()
        iCategoria = self.comboBoxCategoria.currentIndex()

        # Converte as variaveis inteiras para QString
        StrCategoria = iCategoria.tostr()
        StrModalidade = iModalidade.tostr()

        tratarRetornoFiscal(iCFBPAbrir_ECF_Daruma(StrOrigem,StrDestino,StrUFDestino,StrPercurso,StrPrestadora,StrPlataforma,StrPoltrona,StrModalidade,StrCategoria,StrDTEmbarque,StrRGPassageiro,StrNomePassageiro,StrEndPassageiro), self)

    def on_pushButtonCancelar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_iCFBPAbrir):
        ui_FISCAL_iCFBPAbrir.setObjectName("ui_FISCAL_iCFBPAbrir")
        ui_FISCAL_iCFBPAbrir.resize(382, 323)
        self.verticalLayout = QtGui.QVBoxLayout(ui_FISCAL_iCFBPAbrir)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEditOrigem = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditOrigem.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditOrigem.setMaxLength(32772)
        self.lineEditOrigem.setObjectName("lineEditOrigem")
        self.gridLayout.addWidget(self.lineEditOrigem, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.lineEditUFOrigem = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditUFOrigem.setEnabled(False)
        self.lineEditUFOrigem.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEditUFOrigem.setMaxLength(4)
        self.lineEditUFOrigem.setReadOnly(True)
        self.lineEditUFOrigem.setObjectName("lineEditUFOrigem")
        self.gridLayout.addWidget(self.lineEditUFOrigem, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_4 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditDestino = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditDestino.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditDestino.setObjectName("lineEditDestino")
        self.gridLayout_13.addWidget(self.lineEditDestino, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_13.addWidget(self.label_7, 0, 2, 1, 1)
        self.lineEditUFDestino = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditUFDestino.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEditUFDestino.setMaxLength(4)
        self.lineEditUFDestino.setObjectName("lineEditUFDestino")
        self.gridLayout_13.addWidget(self.lineEditUFDestino, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_13)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditPercurso = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditPercurso.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEditPercurso.setObjectName("lineEditPercurso")
        self.gridLayout_2.addWidget(self.lineEditPercurso, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditPrestadora = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditPrestadora.setObjectName("lineEditPrestadora")
        self.gridLayout_3.addWidget(self.lineEditPrestadora, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.lineEditPoltrona = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditPoltrona.setMaximumSize(QtCore.QSize(41, 20))
        self.lineEditPoltrona.setObjectName("lineEditPoltrona")
        self.horizontalLayout.addWidget(self.lineEditPoltrona)
        self.label_2 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditPlataforma = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditPlataforma.setMaximumSize(QtCore.QSize(51, 20))
        self.lineEditPlataforma.setObjectName("lineEditPlataforma")
        self.horizontalLayout.addWidget(self.lineEditPlataforma)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBoxCategoria = QtGui.QComboBox(ui_FISCAL_iCFBPAbrir)
        self.comboBoxCategoria.setObjectName("comboBoxCategoria")
        self.comboBoxCategoria.addItem("")
        self.comboBoxCategoria.addItem("")
        self.comboBoxCategoria.addItem("")
        self.comboBoxCategoria.addItem("")
        self.gridLayout_4.addWidget(self.comboBoxCategoria, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 2, 1, 1)
        self.comboBoxModalidade = QtGui.QComboBox(ui_FISCAL_iCFBPAbrir)
        self.comboBoxModalidade.setObjectName("comboBoxModalidade")
        self.comboBoxModalidade.addItem("")
        self.comboBoxModalidade.addItem("")
        self.comboBoxModalidade.addItem("")
        self.comboBoxModalidade.addItem("")
        self.gridLayout_4.addWidget(self.comboBoxModalidade, 0, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEditDTEmbarque = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditDTEmbarque.setObjectName("lineEditDTEmbarque")
        self.gridLayout_8.addWidget(self.lineEditDTEmbarque, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_8)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_11 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)
        self.lineEditNomePassageiro = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditNomePassageiro.setObjectName("lineEditNomePassageiro")
        self.gridLayout_9.addWidget(self.lineEditNomePassageiro, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_9)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_12 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEditEndPassageiro = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditEndPassageiro.setObjectName("lineEditEndPassageiro")
        self.gridLayout_10.addWidget(self.lineEditEndPassageiro, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_10)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lineEditRGPassageiro = QtGui.QLineEdit(ui_FISCAL_iCFBPAbrir)
        self.lineEditRGPassageiro.setObjectName("lineEditRGPassageiro")
        self.gridLayout_11.addWidget(self.lineEditRGPassageiro, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(ui_FISCAL_iCFBPAbrir)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_11)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButtonEnviar = QtGui.QPushButton(ui_FISCAL_iCFBPAbrir)
        self.pushButtonEnviar.setObjectName("pushButtonEnviar")
        self.horizontalLayout_2.addWidget(self.pushButtonEnviar)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButtonCancelar = QtGui.QPushButton(ui_FISCAL_iCFBPAbrir)
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayout_2.addWidget(self.pushButtonCancelar)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ui_FISCAL_iCFBPAbrir)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_iCFBPAbrir)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditOrigem, self.lineEditUFOrigem)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditUFOrigem, self.lineEditDestino)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditDestino, self.lineEditUFDestino)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditUFDestino, self.lineEditPercurso)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditPercurso, self.lineEditPrestadora)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditPrestadora, self.lineEditPoltrona)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditPoltrona, self.lineEditPlataforma)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditPlataforma, self.comboBoxCategoria)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.comboBoxCategoria, self.comboBoxModalidade)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.comboBoxModalidade, self.lineEditDTEmbarque)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditDTEmbarque, self.lineEditNomePassageiro)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditNomePassageiro, self.lineEditEndPassageiro)
        ui_FISCAL_iCFBPAbrir.setTabOrder(self.lineEditEndPassageiro, self.lineEditRGPassageiro)

    def retranslateUi(self, ui_FISCAL_iCFBPAbrir):
        ui_FISCAL_iCFBPAbrir.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Método iCFBPAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Origem:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditOrigem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "São José dos Campos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "UF:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditUFOrigem.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Destino:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDestino.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "São Paulo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "UF:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditUFDestino.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "SP", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Percurso:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPercurso.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "80KM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Prestadora:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPrestadora.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Pássaro Marron", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Poltrona:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPoltrona.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Plataforma:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPlataforma.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "09", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Categoria:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCategoria.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCategoria.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "1 - Rodoviário", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCategoria.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "2 - Ferroviário", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxCategoria.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "3 - Hidroviário", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Modalidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxModalidade.setItemText(0, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Selecione...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxModalidade.setItemText(1, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "1 - Interestadual", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxModalidade.setItemText(2, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "2 - Intermunicipal", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxModalidade.setItemText(3, QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "3 - Internacional", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Data/Hora Embarque:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditDTEmbarque.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "01012012180000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Nome Passageiro:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNomePassageiro.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Figueiredo Alencar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Endereço do Passageiro:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEndPassageiro.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Shishima Hifumi 2911", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditRGPassageiro.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "120984436", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "RG Passageiro:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnviar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Enviar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("ui_FISCAL_iCFBPAbrir", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

