# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_parametrizacaosintegra.ui'
#
# Created: Mon Nov 24 22:26:13 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import regAlterarValor_Daruma


class Ui_ui_FISCAL_ParametrizacaoSintegra(QtGui.QWidget):

    def __init__(self):
        super(Ui_ui_FISCAL_ParametrizacaoSintegra, self).__init__()

        self.setupUi(self)

        self.pushButtonFechar.clicked.connect(self.on_pushButtonFechar_clicked)
        self.pushButtonParametrizar.clicked.connect(self.on_pushButtonParametrizar_clicked)
        self.comboBoxFinalidade.currentIndexChanged['QString'].connect(self.on_comboBoxFinalidade_currentIndexChanged)
        self.comboBoxIdentificacaoConvenio.currentIndexChanged['QString'].connect(self.on_comboBoxIdentificacaoConvenio_currentIndexChanged)
        self.comboBoxNaturezaOperacao.currentIndexChanged['QString'].connect(self.on_comboBoxNaturezaOperacao_currentIndexChanged)

        #DEFINE VALORES DOS LINEEDIT
        self.lineEditEndereco.setText("Avenida Shishima Hifumi")
        self.lineEditNumero.setText("3911")
        self.lineEditComplemento.setText("Pq Tecnológico")
        self.lineEditBairro.setText("Urbanova")
        self.lineEditCEP.setText("12200-000")
        self.lineEditMunicipio.setText("São José dos Campos")
        self.lineEditTelefone.setText("12-33221122")
        self.lineEditFAX.setText("12-33221122")
        self.lineEditNomeContato.setText("João Oliveira")

        #DEFINE VALORES DAS COMBOBOX, USANDO QSTRINGLIST
        StrEstados = 'AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split()
        self.comboBoxUF.addItems(StrEstados)
        StrFinalidade = '1 2 3 4 5'.split()
        self.comboBoxFinalidade.addItems(StrFinalidade)
        StrIdentificacao = '1 2 3'.split()
        self.comboBoxIdentificacaoConvenio.addItems(StrIdentificacao)
        StrNatureza = '1 2 3'.split()
        self.comboBoxNaturezaOperacao.addItems(StrNatureza)
        
    def on_comboBoxFinalidade_currentIndexChanged(self):
        if(self.comboBoxFinalidade.currentText() == "1"):
            self.labelFinalidade.setText("Normal")
        if(self.comboBoxFinalidade.currentText() == "2"):
            self.labelFinalidade.setText("Retificação Total do Arquivo")
        if(self.comboBoxFinalidade.currentText() == "3"):
            self.labelFinalidade.setText("Retificação Aditiva do Arquivo")
        if(self.comboBoxFinalidade.currentText() == "4"):
            self.labelFinalidade.setText("Retificação Corretiva")
        if(self.comboBoxFinalidade.currentText() == "5"):
            self.labelFinalidade.setText("Desfazimento: arquivo de informação referente a operações/pretações não efetivadas")

    def on_comboBoxIdentificacaoConvenio_currentIndexChanged(self):
        if (self.comboBoxIdentificacaoConvenio.currentText() == "1"):
            self.labelIdentificacaoConvenio.setText("Convênio ICMS 31/99")
        if (self.comboBoxIdentificacaoConvenio.currentText() == "2"):
            self.labelIdentificacaoConvenio.setText("Convênio ICMS 69/02 e 142/02")
        if (self.comboBoxIdentificacaoConvenio.currentText() == "3"):
            self.labelIdentificacaoConvenio.setText("Convênio ICMS 76/03 e 20/04")
    
    def on_comboBoxNaturezaOperacao_currentIndexChanged(self):
        if(self.comboBoxNaturezaOperacao.currentText() == "1"):
            self.labelNaturezaOperacao.setText("Interestaduais somente com substituição tributária")
        if(self.comboBoxNaturezaOperacao.currentText() == "2"):
            self.labelNaturezaOperacao.setText("Interestaduais com ou sem substituição tributária")
        if(self.comboBoxNaturezaOperacao.currentText() == "3"):
            self.labelNaturezaOperacao.setText("Todas das operações do informante")

    def on_pushButtonParametrizar_clicked(self):
        StrEndereco = self.lineEditEndereco.text()
        StrNumero = self.lineEditNumero.text()
        StrComplemento = self.lineEditComplemento.text()
        StrBairro = self.lineEditBairro.text()
        StrCEP = self.lineEditCEP.text()
        StrMunicipio = self.lineEditMunicipio.text()
        StrUF = self.comboBoxUF.currentText()
        StrTelefone = self.lineEditTelefone.text()
        StrFAX = self.lineEditFAX.text()
        StrNome = self.lineEditNomeContato.text()
        StrFinalidade = self.comboBoxFinalidade.currentText()
        StrConvenio = self.comboBoxIdentificacaoConvenio.currentText()
        StrNatureza = self.comboBoxNaturezaOperacao.currentText()

        regAlterarValor_Daruma("ECF\\SINTEGRA\\Bairro",StrBairro)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\CEP",StrCEP)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Cod_Finalidade",StrFinalidade)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Cod_Convenio",StrConvenio)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Cod_Natureza",StrNatureza)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Complemento",StrComplemento)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Contato_Nome",StrNome)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Contato_Telefone",StrTelefone)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Fax",StrFAX)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Logradouro",StrEndereco)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Municipio",StrMunicipio)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\Numero",StrNumero)
        regAlterarValor_Daruma("ECF\\SINTEGRA\\UF",StrUF)
    
        QMessageBox.information(self,"DarumaFramework - Python/Qt","Parametrização Concluída.")
        self.close()
    
    
    def on_pushButtonFechar_clicked(self):
        self.close()

    def setupUi(self, ui_FISCAL_ParametrizacaoSintegra):
        ui_FISCAL_ParametrizacaoSintegra.setObjectName("ui_FISCAL_ParametrizacaoSintegra")
        ui_FISCAL_ParametrizacaoSintegra.resize(384, 418)
        self.gridLayout_3 = QtGui.QGridLayout(ui_FISCAL_ParametrizacaoSintegra)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(ui_FISCAL_ParametrizacaoSintegra)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 3, 1, 1)
        self.lineEditEndereco = QtGui.QLineEdit(self.groupBox)
        self.lineEditEndereco.setObjectName("lineEditEndereco")
        self.gridLayout_2.addWidget(self.lineEditEndereco, 1, 0, 1, 1)
        self.lineEditNumero = QtGui.QLineEdit(self.groupBox)
        self.lineEditNumero.setObjectName("lineEditNumero")
        self.gridLayout_2.addWidget(self.lineEditNumero, 1, 1, 1, 2)
        self.lineEditComplemento = QtGui.QLineEdit(self.groupBox)
        self.lineEditComplemento.setObjectName("lineEditComplemento")
        self.gridLayout_2.addWidget(self.lineEditComplemento, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 4, 1, 1)
        self.lineEditBairro = QtGui.QLineEdit(self.groupBox)
        self.lineEditBairro.setObjectName("lineEditBairro")
        self.gridLayout_2.addWidget(self.lineEditBairro, 3, 0, 1, 1)
        self.lineEditCEP = QtGui.QLineEdit(self.groupBox)
        self.lineEditCEP.setObjectName("lineEditCEP")
        self.gridLayout_2.addWidget(self.lineEditCEP, 3, 1, 1, 2)
        self.lineEditMunicipio = QtGui.QLineEdit(self.groupBox)
        self.lineEditMunicipio.setObjectName("lineEditMunicipio")
        self.gridLayout_2.addWidget(self.lineEditMunicipio, 3, 3, 1, 1)
        self.comboBoxUF = QtGui.QComboBox(self.groupBox)
        self.comboBoxUF.setMaximumSize(QtCore.QSize(51, 20))
        self.comboBoxUF.setObjectName("comboBoxUF")
        self.gridLayout_2.addWidget(self.comboBoxUF, 3, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 3, 1, 1)
        self.lineEditTelefone = QtGui.QLineEdit(self.groupBox)
        self.lineEditTelefone.setObjectName("lineEditTelefone")
        self.gridLayout_2.addWidget(self.lineEditTelefone, 5, 0, 1, 1)
        self.lineEditFAX = QtGui.QLineEdit(self.groupBox)
        self.lineEditFAX.setObjectName("lineEditFAX")
        self.gridLayout_2.addWidget(self.lineEditFAX, 5, 1, 1, 2)
        self.lineEditNomeContato = QtGui.QLineEdit(self.groupBox)
        self.lineEditNomeContato.setObjectName("lineEditNomeContato")
        self.gridLayout_2.addWidget(self.lineEditNomeContato, 5, 3, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.comboBoxFinalidade = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxFinalidade.setMaximumSize(QtCore.QSize(63, 20))
        self.comboBoxFinalidade.setObjectName("comboBoxFinalidade")
        self.gridLayout.addWidget(self.comboBoxFinalidade, 1, 0, 1, 1)
        self.labelFinalidade = QtGui.QLabel(self.groupBox_2)
        self.labelFinalidade.setMinimumSize(QtCore.QSize(151, 16))
        self.labelFinalidade.setText("")
        self.labelFinalidade.setObjectName("labelFinalidade")
        self.gridLayout.addWidget(self.labelFinalidade, 1, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.comboBoxIdentificacaoConvenio = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxIdentificacaoConvenio.setMaximumSize(QtCore.QSize(63, 20))
        self.comboBoxIdentificacaoConvenio.setObjectName("comboBoxIdentificacaoConvenio")
        self.gridLayout.addWidget(self.comboBoxIdentificacaoConvenio, 3, 0, 1, 1)
        self.labelIdentificacaoConvenio = QtGui.QLabel(self.groupBox_2)
        self.labelIdentificacaoConvenio.setMinimumSize(QtCore.QSize(181, 16))
        self.labelIdentificacaoConvenio.setText("")
        self.labelIdentificacaoConvenio.setObjectName("labelIdentificacaoConvenio")
        self.gridLayout.addWidget(self.labelIdentificacaoConvenio, 3, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.comboBoxNaturezaOperacao = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxNaturezaOperacao.setMaximumSize(QtCore.QSize(63, 20))
        self.comboBoxNaturezaOperacao.setObjectName("comboBoxNaturezaOperacao")
        self.gridLayout.addWidget(self.comboBoxNaturezaOperacao, 5, 0, 1, 1)
        self.labelNaturezaOperacao = QtGui.QLabel(self.groupBox_2)
        self.labelNaturezaOperacao.setMinimumSize(QtCore.QSize(191, 16))
        self.labelNaturezaOperacao.setText("")
        self.labelNaturezaOperacao.setObjectName("labelNaturezaOperacao")
        self.gridLayout.addWidget(self.labelNaturezaOperacao, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 6, 0, 1, 5)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.pushButtonFechar = QtGui.QPushButton(ui_FISCAL_ParametrizacaoSintegra)
        self.pushButtonFechar.setObjectName("pushButtonFechar")
        self.gridLayout_3.addWidget(self.pushButtonFechar, 4, 0, 1, 1)
        self.pushButtonParametrizar = QtGui.QPushButton(ui_FISCAL_ParametrizacaoSintegra)
        self.pushButtonParametrizar.setObjectName("pushButtonParametrizar")
        self.gridLayout_3.addWidget(self.pushButtonParametrizar, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)

        self.retranslateUi(ui_FISCAL_ParametrizacaoSintegra)
        self.comboBoxFinalidade.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_ParametrizacaoSintegra)

    def retranslateUi(self, ui_FISCAL_ParametrizacaoSintegra):
        ui_FISCAL_ParametrizacaoSintegra.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Parametrizaçao Sintegra", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Parametrização Registry - SINTEGRA", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Endereço:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Número:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Complemento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Bairro:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "CEP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Município:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "UF:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Telefone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "FAX:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Nome Contato:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Dados do Convênio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Finalidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Identificaçao do Convênio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Natureza da Operação:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFechar.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonParametrizar.setText(QtGui.QApplication.translate("ui_FISCAL_ParametrizacaoSintegra", "Parametrizar", None, QtGui.QApplication.UnicodeUTF8))

