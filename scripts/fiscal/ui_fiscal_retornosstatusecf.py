# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_fiscal_retornosstatusecf.ui'
#
# Created: Mon Nov 24 22:26:20 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ui_FISCAL_RetornosStatusECF(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_ui_FISCAL_RetornosStatusECF, self).__init__()

        self.setupUi(self)

        self.actionM_todo_rRetornarInformacao_ECF_Daruma.triggered.connect(self.on_rRetornarInformacao_ECF_Daruma_triggered)
        self.actionM_todo_rRetornarInformacaoSeparador_ECF_Daruma.triggered.connect(self.on_rRetornarInformacaoSeparador_ECF_Daruma_triggered)
        self.actionM_todo_rLerAliquotas_ECF_Daruma.triggered.connect(self.on_rLerAliquotas_ECF_Daruma_triggered)
        self.actionM_todo_rLerMeiosPagto_ECF_Daruma.triggered.connect(self.on_rLerMeiosPagto_ECF_Daruma_triggered)
        self.actionM_todo_rLerRG_ECF_Daruma.triggered.connect(self.on_rLerRG_ECF_Daruma_triggered)
        self.actionM_todo_rLerCNF_ECF_Daruma.triggered.connect(self.on_rLerCNF_ECF_Daruma_triggered)
        self.actionM_todo_rLerDecimais_ECF_Daruma.triggered.connect(self.on_rLerDecimais_ECF_Daruma_triggered)
        self.actionM_todo_rLerDecimaisInt_ECF_Daruma.triggered.connect(self.on_rLerDecimaisInt_ECF_Daruma_triggered)
        self.actionM_todo_rLerDecimaisStr_ECF_Daruma.triggered.connect(self.on_rLerDecimaisStr_ECF_Daruma_triggered)
        self.actionM_todo_rDataHoraImpressora_ECF_Daruma.triggered.connect(self.on_rDataHoraImpressora_ECF_Daruma_triggered)
        self.actionM_todo_rVerificaImpressoraLigada_ECF_Daruma.triggered.connect(self.on_rVerificaImpressoraLigada_ECF_Daruma_triggered)
        self.actionM_todo_rVerificarReducaoZ_ECF_Daruma.triggered.connect(self.on_rVerificarReducaoZ_ECF_Daruma_triggered)
        self.actionM_todo_rRetornarDadosReducaoZ_ECF_Daruma.triggered.connect(self.on_rRetornarDadosReducaoZ_ECF_Daruma_triggered)
        self.actionM_todo_rTipoUltimoDocumentoInt_ECF_Daruma.triggered.connect(self.on_rTipoUltimoDocumentoInt_ECF_Daruma_triggered)
        self.actionM_todo_rTipoUltimoDocumentoStr_ECF_Daruma.triggered.connect(self.on_rTipoUltimoDocumentoStr_ECF_Daruma_triggered)
        self.actionM_todo_rUltimoCMDEnviado_ECF_Daruma.triggered.connect(self.on_rUltimoCMDEnviado_ECF_Daruma_triggered)
        self.actionM_todo_rMinasLegal_ECF_Daruma.triggered.connect(self.on_rMinasLegal_ECF_Daruma_triggered)
        self.actionM_todo_rCFSaldoAPagar_ECF_Daruma.triggered.connect(self.on_rCFSaldoAPagar_ECF_Daruma_triggered)
        self.actionM_todo_rCFSubTotal_ECF_Daruma.triggered.connect(self.on_rCFSubTotal_ECF_Daruma_triggered)
        self.actionM_todo_rCFVerificarStatus_ECF_Daruma.triggered.connect(self.on_rCFVerificarStatus_ECF_Daruma_triggered)
        self.actionM_todo_rStatusImpressora_ECF_Daruma.triggered.connect(self.on_rStatusImpressora_ECF_Daruma_triggered)
        self.actionM_todo_rStatusImpressoraBinario_ECF_Daruma.triggered.connect(self.on_rStatusImpressoraBinario_ECF_Daruma_triggered)
        self.actionM_todo_rConsultaStatusImpressoraStr_ECF_Daruma.triggered.connect(self.on_rConsultaStatusImpressoraStr_ECF_Daruma_triggered)
        self.actionM_todo_rConsultaStatusImpressoraInt_ECF_Daruma.triggered.connect(self.on_rConsultaStatusImpressoraInt_ECF_Daruma_triggered)
        self.actionM_todo_rStatusUltimoCmd_ECF_Daruma.triggered.connect(self.on_rStatusUltimoCmd_ECF_Daruma_triggered)
        self.actionM_todo_rStatusUltimoCmdInt_ECF_Daruma.triggered.connect(self.on_rStatusUltimoCmdInt_ECF_Daruma_triggered)
        self.actionM_todo_rStatusUltimoCmdStr_ECF_Daruma.triggered.connect(self.on_rStatusUltimoCmdStr_ECF_Daruma_triggered)
        self.actionM_todo_rInfoEstendida_ECF_Daruma.triggered.connect(self.on_rInfoEstendida_ECF_Daruma_triggered)
        self.actionM_todo_rInfoEstendida1_ECF_Daruma.triggered.connect(self.on_rInfoEstendida1_ECF_Daruma_triggered)
        self.actionM_todo_rInfoEstendida2_ECF_Daruma.triggered.connect(self.on_rInfoEstendida2_ECF_Daruma_triggered)
        self.actionM_todo_rInfoEstendida3_ECF_Daruma.triggered.connect(self.on_rInfoEstendida3_ECF_Daruma_triggered)
        self.actionM_todo_rInfoEstendida4_ECF_Daruma.triggered.connect(self.on_rInfoEstendida4_ECF_Daruma_triggered)
        self.actionM_todo_rInfoEstendida5_ECF_Daruma.triggered.connect(self.on_rInfoEstendida5_ECF_Daruma_triggered)
        self.actionM_todo_eBuscarPortaVelocidade_ECF_Daruma.triggered.connect(self.on_eBuscarPortaVelocidade_ECF_Daruma_triggered)
        self.actionM_todo_eVerificarVersaoDLL_Daruma.triggered.connect(self.on_eVerificarVersaoDLL_Daruma_triggered)
        self.actionM_todo_eRetornarPortasCOM_ECF_Daruma.triggered.connect(self.on_eRetornarPortasCOM_ECF_Daruma_triggered)
        self.actionM_todo_iRelatorioConfiguracao_ECF_Daruma.triggered.connect(self.on_iRelatorioConfiguracao_ECF_Daruma_triggered)

    def on_rRetornarInformacao_ECF_Daruma_triggered(self):
        pass

    def on_rRetornarInformacaoSeparador_ECF_Daruma_triggered(self):
        pass

    def on_rLerAliquotas_ECF_Daruma_triggered(self):
        pass

    def on_rLerMeiosPagto_ECF_Daruma_triggered(self):
        pass

    def on_rLerRG_ECF_Daruma_triggered(self):
        pass

    def on_rLerCNF_ECF_Daruma_triggered(self):
        pass

    def on_rLerDecimais_ECF_Daruma_triggered(self):
        pass

    def on_rLerDecimaisInt_ECF_Daruma_triggered(self):
        pass

    def on_rLerDecimaisStr_ECF_Daruma_triggered(self):
        pass

    def on_rDataHoraImpressora_ECF_Daruma_triggered(self):
        pass

    def on_rVerificaImpressoraLigada_ECF_Daruma_triggered(self):
        pass

    def on_rVerificarReducaoZ_ECF_Daruma_triggered(self):
        pass

    def on_rRetornarDadosReducaoZ_ECF_Daruma_triggered(self):
        pass

    def on_rTipoUltimoDocumentoInt_ECF_Daruma_triggered(self):
        pass

    def on_rTipoUltimoDocumentoStr_ECF_Daruma_triggered(self):
        pass

    def on_rUltimoCMDEnviado_ECF_Daruma_triggered(self):
        pass

    def on_rMinasLegal_ECF_Daruma_triggered(self):
        pass

    def on_rCFSaldoAPagar_ECF_Daruma_triggered(self):
        pass

    def on_rCFSubTotal_ECF_Daruma_triggered(self):
        pass

    def on_rCFVerificarStatus_ECF_Daruma_triggered(self):
        pass

    def on_rStatusImpressora_ECF_Daruma_triggered(self):
        pass

    def on_rStatusImpressoraBinario_ECF_Daruma_triggered(self):
        pass

    def on_rConsultaStatusImpressoraStr_ECF_Daruma_triggered(self):
        pass

    def on_rConsultaStatusImpressoraInt_ECF_Daruma_triggered(self):
        pass

    def on_rStatusUltimoCmd_ECF_Daruma_triggered(self):
        pass

    def on_rStatusUltimoCmdInt_ECF_Daruma_triggered(self):
        pass

    def on_rStatusUltimoCmdStr_ECF_Daruma_triggered(self):
        pass

    def on_rInfoEstendida_ECF_Daruma_triggered(self):
        pass

    def on_rInfoEstendida1_ECF_Daruma_triggered(self):
        pass

    def on_rInfoEstendida2_ECF_Daruma_triggered(self):
        pass

    def on_rInfoEstendida3_ECF_Daruma_triggered(self):
        pass

    def on_rInfoEstendida4_ECF_Daruma_triggered(self):
        pass

    def on_rInfoEstendida5_ECF_Daruma_triggered(self):
        pass

    def on_eBuscarPortaVelocidade_ECF_Daruma_triggered(self):
        pass

    def on_eVerificarVersaoDLL_Daruma_triggered(self):
        pass

    def on_eRetornarPortasCOM_ECF_Daruma_triggered(self):
        pass

    def on_iRelatorioConfiguracao_ECF_Daruma_triggered(self):
        pass

    def setupUi(self, ui_FISCAL_RetornosStatusECF):
        ui_FISCAL_RetornosStatusECF.setObjectName("ui_FISCAL_RetornosStatusECF")
        ui_FISCAL_RetornosStatusECF.resize(576, 289)
        self.centralwidget = QtGui.QWidget(ui_FISCAL_RetornosStatusECF)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEditRetornos = QtGui.QTextEdit(self.groupBox)
        self.textEditRetornos.setObjectName("textEditRetornos")
        self.horizontalLayout.addWidget(self.textEditRetornos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        ui_FISCAL_RetornosStatusECF.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ui_FISCAL_RetornosStatusECF)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 21))
        self.menubar.setObjectName("menubar")
        self.menuM_todos_Retornos_do_ECF = QtGui.QMenu(self.menubar)
        self.menuM_todos_Retornos_do_ECF.setObjectName("menuM_todos_Retornos_do_ECF")
        self.menuRetorno_Cupom_Fiscal = QtGui.QMenu(self.menuM_todos_Retornos_do_ECF)
        self.menuRetorno_Cupom_Fiscal.setObjectName("menuRetorno_Cupom_Fiscal")
        self.menuM_todos_de_Status = QtGui.QMenu(self.menubar)
        self.menuM_todos_de_Status.setObjectName("menuM_todos_de_Status")
        self.menuM_todos_Especiais = QtGui.QMenu(self.menubar)
        self.menuM_todos_Especiais.setObjectName("menuM_todos_Especiais")
        ui_FISCAL_RetornosStatusECF.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ui_FISCAL_RetornosStatusECF)
        self.statusbar.setObjectName("statusbar")
        ui_FISCAL_RetornosStatusECF.setStatusBar(self.statusbar)
        self.actionM_todo_rRetornarInformacao_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rRetornarInformacao_ECF_Daruma.setObjectName("actionM_todo_rRetornarInformacao_ECF_Daruma")
        self.actionM_todo_rRetornarInformacaoSeparador_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rRetornarInformacaoSeparador_ECF_Daruma.setObjectName("actionM_todo_rRetornarInformacaoSeparador_ECF_Daruma")
        self.actionM_todo_rLerAliquotas_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerAliquotas_ECF_Daruma.setObjectName("actionM_todo_rLerAliquotas_ECF_Daruma")
        self.actionM_todo_rLerMeiosPagto_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerMeiosPagto_ECF_Daruma.setObjectName("actionM_todo_rLerMeiosPagto_ECF_Daruma")
        self.actionM_todo_rLerRG_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerRG_ECF_Daruma.setObjectName("actionM_todo_rLerRG_ECF_Daruma")
        self.actionM_todo_rLerCNF_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerCNF_ECF_Daruma.setObjectName("actionM_todo_rLerCNF_ECF_Daruma")
        self.actionM_todo_rLerDecimais_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerDecimais_ECF_Daruma.setObjectName("actionM_todo_rLerDecimais_ECF_Daruma")
        self.actionM_todo_rLerDecimaisInt_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerDecimaisInt_ECF_Daruma.setObjectName("actionM_todo_rLerDecimaisInt_ECF_Daruma")
        self.actionM_todo_rLerDecimaisStr_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rLerDecimaisStr_ECF_Daruma.setObjectName("actionM_todo_rLerDecimaisStr_ECF_Daruma")
        self.actionM_todo_rDataHoraImpressora_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rDataHoraImpressora_ECF_Daruma.setObjectName("actionM_todo_rDataHoraImpressora_ECF_Daruma")
        self.actionM_todo_rVerificaImpressoraLigada_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rVerificaImpressoraLigada_ECF_Daruma.setObjectName("actionM_todo_rVerificaImpressoraLigada_ECF_Daruma")
        self.actionM_todo_rVerificarReducaoZ_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rVerificarReducaoZ_ECF_Daruma.setObjectName("actionM_todo_rVerificarReducaoZ_ECF_Daruma")
        self.actionM_todo_rRetornarDadosReducaoZ_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rRetornarDadosReducaoZ_ECF_Daruma.setObjectName("actionM_todo_rRetornarDadosReducaoZ_ECF_Daruma")
        self.actionM_todo_rTipoUltimoDocumentoInt_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rTipoUltimoDocumentoInt_ECF_Daruma.setObjectName("actionM_todo_rTipoUltimoDocumentoInt_ECF_Daruma")
        self.actionM_todo_rTipoUltimoDocumentoStr_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rTipoUltimoDocumentoStr_ECF_Daruma.setObjectName("actionM_todo_rTipoUltimoDocumentoStr_ECF_Daruma")
        self.actionM_todo_rUltimoCMDEnviado_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rUltimoCMDEnviado_ECF_Daruma.setObjectName("actionM_todo_rUltimoCMDEnviado_ECF_Daruma")
        self.actionM_todo_rMinasLegal_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rMinasLegal_ECF_Daruma.setObjectName("actionM_todo_rMinasLegal_ECF_Daruma")
        self.actionM_todo_rCFSaldoAPagar_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rCFSaldoAPagar_ECF_Daruma.setObjectName("actionM_todo_rCFSaldoAPagar_ECF_Daruma")
        self.actionM_todo_rCFSubTotal_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rCFSubTotal_ECF_Daruma.setObjectName("actionM_todo_rCFSubTotal_ECF_Daruma")
        self.actionM_todo_rCFVerificarStatus_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rCFVerificarStatus_ECF_Daruma.setObjectName("actionM_todo_rCFVerificarStatus_ECF_Daruma")
        self.actionM_todo_rStatusImpressora_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rStatusImpressora_ECF_Daruma.setObjectName("actionM_todo_rStatusImpressora_ECF_Daruma")
        self.actionM_todo_rStatusImpressoraBinario_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rStatusImpressoraBinario_ECF_Daruma.setObjectName("actionM_todo_rStatusImpressoraBinario_ECF_Daruma")
        self.actionM_todo_rConsultaStatusImpressoraStr_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rConsultaStatusImpressoraStr_ECF_Daruma.setObjectName("actionM_todo_rConsultaStatusImpressoraStr_ECF_Daruma")
        self.actionM_todo_rConsultaStatusImpressoraInt_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rConsultaStatusImpressoraInt_ECF_Daruma.setObjectName("actionM_todo_rConsultaStatusImpressoraInt_ECF_Daruma")
        self.actionM_todo_rStatusUltimoCmd_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rStatusUltimoCmd_ECF_Daruma.setObjectName("actionM_todo_rStatusUltimoCmd_ECF_Daruma")
        self.actionM_todo_rStatusUltimoCmdInt_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rStatusUltimoCmdInt_ECF_Daruma.setObjectName("actionM_todo_rStatusUltimoCmdInt_ECF_Daruma")
        self.actionM_todo_rStatusUltimoCmdStr_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rStatusUltimoCmdStr_ECF_Daruma.setObjectName("actionM_todo_rStatusUltimoCmdStr_ECF_Daruma")
        self.actionM_todo_rInfoEstendida_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rInfoEstendida_ECF_Daruma.setObjectName("actionM_todo_rInfoEstendida_ECF_Daruma")
        self.actionM_todo_rInfoEstendida1_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rInfoEstendida1_ECF_Daruma.setObjectName("actionM_todo_rInfoEstendida1_ECF_Daruma")
        self.actionM_todo_rInfoEstendida2_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rInfoEstendida2_ECF_Daruma.setObjectName("actionM_todo_rInfoEstendida2_ECF_Daruma")
        self.actionM_todo_rInfoEstendida3_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rInfoEstendida3_ECF_Daruma.setObjectName("actionM_todo_rInfoEstendida3_ECF_Daruma")
        self.actionM_todo_rInfoEstendida4_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rInfoEstendida4_ECF_Daruma.setObjectName("actionM_todo_rInfoEstendida4_ECF_Daruma")
        self.actionM_todo_rInfoEstendida5_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_rInfoEstendida5_ECF_Daruma.setObjectName("actionM_todo_rInfoEstendida5_ECF_Daruma")
        self.actionM_todo_eBuscarPortaVelocidade_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_eBuscarPortaVelocidade_ECF_Daruma.setObjectName("actionM_todo_eBuscarPortaVelocidade_ECF_Daruma")
        self.actionM_todo_eVerificarVersaoDLL_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_eVerificarVersaoDLL_Daruma.setObjectName("actionM_todo_eVerificarVersaoDLL_Daruma")
        self.actionM_todo_eRetornarPortasCOM_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_eRetornarPortasCOM_ECF_Daruma.setObjectName("actionM_todo_eRetornarPortasCOM_ECF_Daruma")
        self.actionM_todo_iRelatorioConfiguracao_ECF_Daruma = QtGui.QAction(ui_FISCAL_RetornosStatusECF)
        self.actionM_todo_iRelatorioConfiguracao_ECF_Daruma.setObjectName("actionM_todo_iRelatorioConfiguracao_ECF_Daruma")
        self.menuRetorno_Cupom_Fiscal.addAction(self.actionM_todo_rCFSaldoAPagar_ECF_Daruma)
        self.menuRetorno_Cupom_Fiscal.addAction(self.actionM_todo_rCFSubTotal_ECF_Daruma)
        self.menuRetorno_Cupom_Fiscal.addAction(self.actionM_todo_rCFVerificarStatus_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rRetornarInformacao_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rRetornarInformacaoSeparador_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerAliquotas_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerMeiosPagto_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerRG_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerCNF_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerDecimais_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerDecimaisInt_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rLerDecimaisStr_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rDataHoraImpressora_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rVerificaImpressoraLigada_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rVerificarReducaoZ_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rRetornarDadosReducaoZ_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rTipoUltimoDocumentoInt_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rTipoUltimoDocumentoStr_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rUltimoCMDEnviado_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.actionM_todo_rMinasLegal_ECF_Daruma)
        self.menuM_todos_Retornos_do_ECF.addAction(self.menuRetorno_Cupom_Fiscal.menuAction())
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rStatusImpressora_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rStatusImpressoraBinario_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rConsultaStatusImpressoraStr_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rConsultaStatusImpressoraInt_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rStatusUltimoCmd_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rStatusUltimoCmdInt_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rStatusUltimoCmdStr_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rInfoEstendida_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rInfoEstendida1_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rInfoEstendida2_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rInfoEstendida3_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rInfoEstendida4_ECF_Daruma)
        self.menuM_todos_de_Status.addAction(self.actionM_todo_rInfoEstendida5_ECF_Daruma)
        self.menuM_todos_Especiais.addAction(self.actionM_todo_eBuscarPortaVelocidade_ECF_Daruma)
        self.menuM_todos_Especiais.addAction(self.actionM_todo_eVerificarVersaoDLL_Daruma)
        self.menuM_todos_Especiais.addAction(self.actionM_todo_eRetornarPortasCOM_ECF_Daruma)
        self.menuM_todos_Especiais.addAction(self.actionM_todo_iRelatorioConfiguracao_ECF_Daruma)
        self.menubar.addAction(self.menuM_todos_Retornos_do_ECF.menuAction())
        self.menubar.addAction(self.menuM_todos_de_Status.menuAction())
        self.menubar.addAction(self.menuM_todos_Especiais.menuAction())

        self.retranslateUi(ui_FISCAL_RetornosStatusECF)
        QtCore.QMetaObject.connectSlotsByName(ui_FISCAL_RetornosStatusECF)

    def retranslateUi(self, ui_FISCAL_RetornosStatusECF):
        ui_FISCAL_RetornosStatusECF.setWindowTitle(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Métodos para Retornos e Status do ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Retornos:", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditRetornos.setHtml(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_Retornos_do_ECF.setTitle(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Métodos Retornos do ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRetorno_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Retorno Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_de_Status.setTitle(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Métodos de Status", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_Especiais.setTitle(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Métodos Especiais", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rRetornarInformacao_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rRetornarInformacao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rRetornarInformacaoSeparador_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rRetornarInformacaoSeparador_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerAliquotas_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerAliquotas_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerMeiosPagto_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerMeiosPagto_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerRG_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerRG_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerCNF_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerCNF_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerDecimais_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerDecimais_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerDecimaisInt_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerDecimaisInt_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLerDecimaisStr_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rLerDecimaisStr_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rDataHoraImpressora_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rDataHoraImpressora_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rVerificaImpressoraLigada_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rVerificaImpressoraLigada_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rVerificarReducaoZ_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rVerificarReducaoZ_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rRetornarDadosReducaoZ_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rRetornarDadosReducaoZ_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rTipoUltimoDocumentoInt_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rTipoUltimoDocumentoInt_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rTipoUltimoDocumentoStr_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rTipoUltimoDocumentoStr_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rUltimoCMDEnviado_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rUltimoCMDEnviado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rMinasLegal_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rMinasLegal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rCFSaldoAPagar_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rCFSaldoAPagar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rCFSubTotal_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rCFSubTotal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rCFVerificarStatus_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rCFVerificarStatus_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusImpressora_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rStatusImpressora_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusImpressoraBinario_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rStatusImpressoraBinario_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rConsultaStatusImpressoraStr_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rConsultaStatusImpressoraStr_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rConsultaStatusImpressoraInt_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rConsultaStatusImpressoraInt_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusUltimoCmd_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rStatusUltimoCmd_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusUltimoCmdInt_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rStatusUltimoCmdInt_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusUltimoCmdStr_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rStatusUltimoCmdStr_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rInfoEstendida_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rInfoEstendida_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rInfoEstendida1_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rInfoEstendida1_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rInfoEstendida2_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rInfoEstendida2_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rInfoEstendida3_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rInfoEstendida3_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rInfoEstendida4_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rInfoEstendida4_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rInfoEstendida5_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método rInfoEstendida5_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eBuscarPortaVelocidade_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método eBuscarPortaVelocidade_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eVerificarVersaoDLL_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método eVerificarVersaoDLL_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eRetornarPortasCOM_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método eRetornarPortasCOM_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iRelatorioConfiguracao_ECF_Daruma.setText(QtGui.QApplication.translate("ui_FISCAL_RetornosStatusECF", "Método iRelatorioConfiguracao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))

