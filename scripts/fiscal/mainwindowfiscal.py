# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowfiscal.ui'
#
# Created: Mon Nov 24 22:25:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import iCFAbrirPadrao_ECF_Daruma, iCFCancelarAcrescimoUltimoItem_ECF_Daruma, \
    iCFCancelarDescontoUltimoItem_ECF_Daruma, iCFCancelarUltimoItem_ECF_Daruma, iCCDAbrirPadrao_ECF_Daruma, \
    iCCDFechar_ECF_Daruma, iCCDEstornarPadrao_ECF_Daruma, iCCDSegundaVia_ECF_Daruma, iTEF_Fechar_ECF_Daruma, \
    iCNFAbrirPadrao_ECF_Daruma, iCNFCancelarUltimoItem_ECF_Daruma, iCNFCancelarAcrescimoUltimoItem_ECF_Daruma, \
    iCNFCancelarDescontoUltimoItem_ECF_Daruma, iCNFTotalizarComprovantePadrao_ECF_Daruma, \
    iCNFCancelarDescontoSubtotal_ECF_Daruma, iCNFCancelarAcrescimoSubtotal_ECF_Daruma, \
    iCNFEfetuarPagamentoPadrao_ECF_Daruma, iCNFEncerrarPadrao_ECF_Daruma, iCNFCancelar_ECF_Daruma, \
    iRGAbrirPadrao_ECF_Daruma, iRGFechar_ECF_Daruma, rLeituraX_ECF_Daruma, iLeituraX_ECF_Daruma, iReducaoZ_ECF_Daruma, \
    iSangriaPadrao_ECF_Daruma, iSuprimentoPadrao_ECF_Daruma, confHabilitarHorarioVerao_ECF_Daruma, \
    confDesabilitarHorarioVerao_ECF_Daruma, confHabilitarModoPreVenda_ECF_Daruma, confDesabilitarModoPreVenda_ECF_Daruma, \
    eAbrirGaveta_ECF_Daruma, iCFTotalizarCupomPadrao_ECF_Daruma, iCFCancelarAcrescimoSubtotal_ECF_Daruma, \
    iCFCancelarDescontoSubtotal_ECF_Daruma, iCFEncerrar_ECF_Daruma, iCFAbrir_ECF_Daruma, iCFVender_ECF_Daruma, \
    iCFTotalizarCupom_ECF_Daruma, iCFEfetuarPagamento_ECF_Daruma, iCFCancelar_ECF_Daruma, \
    iCFEmitirCupomAdicional_ECF_Daruma, iCFEncerrarResumido_ECF_Daruma, iCFEncerrarPadrao_ECF_Daruma, \
    iCFEfetuarPagamentoPadrao_ECF_Daruma, rCMEfetuarCalculo_ECF_Daruma, iCFVenderResumido_ECF_Daruma, \
    regAlterarValor_Daruma, iTEF_ImprimirResposta_ECF_Daruma, iCCDImprimirTexto_ECF_Daruma, iCNFAbrir_ECF_Daruma, \
    iCNFReceber_ECF_Daruma, iCNFTotalizarComprovante_ECF_Daruma, iCNFEfetuarPagamento_ECF_Daruma, \
    iCNFEncerrar_ECF_Daruma, rStatusGaveta_ECF_Daruma
from scripts.fiscal.retornofiscal import tratarRetornoFiscal
from scripts.fiscal.ui_fiscal_confcadastrarpadrao import Ui_ui_FISCAL_confCadastrarPadrao
from scripts.fiscal.ui_fiscal_confcfbpprogramaruf import Ui_ui_FISCAL_confCFBPProgramarUF
from scripts.fiscal.ui_fiscal_configuracaocupommania import Ui_ui_FISCAL_ConfiguracaoCupomMania
from scripts.fiscal.ui_fiscal_confprogramaravancopapel import Ui_ui_FISCAL_confProgramarAvancoPapel
from scripts.fiscal.ui_fiscal_confprogramaridloja import Ui_ui_FISCAL_confProgramarIDLoja
from scripts.fiscal.ui_fiscal_confprogramaroperador import Ui_ui_FISCAL_confProgramarOperador
from scripts.fiscal.ui_fiscal_eacionarguilhotina import Ui_ui_FISCAL_eAcionarGuilhotina
from scripts.fiscal.ui_fiscal_ecarregarbitmappromocional import Ui_ui_FISCAL_eCarregarBitmapPromocional
from scripts.fiscal.ui_fiscal_edefinirmodoregistro import Ui_ui_FISCAL_eDefinirModoRegistro
from scripts.fiscal.ui_fiscal_edefinirproduto import Ui_ui_FISCAL_eDefinirProduto
from scripts.fiscal.ui_fiscal_ememoriafiscal import Ui_ui_FISCAL_eMemoriaFiscal
from scripts.fiscal.ui_fiscal_ersaassinararquivo import Ui_ui_FISCAL_eRSAAssinarArquivo
from scripts.fiscal.ui_fiscal_etef_esperararquivo import Ui_ui_FISCAL_eTEF_EsperarArquivo
from scripts.fiscal.ui_fiscal_etef_setarfoco import Ui_ui_FISCAL_eTEF_SetarFoco
from scripts.fiscal.ui_fiscal_etef_travarteclado import Ui_ui_FISCAL_eTEF_TravarTeclado
from scripts.fiscal.ui_fiscal_iccdabrir import Ui_ui_FISCAL_iCCDAbrir
from scripts.fiscal.ui_fiscal_iccdabrirsimplificado import Ui_ui_FISCAL_iCCDAbrirSimplificado
from scripts.fiscal.ui_fiscal_iccdestornar import Ui_ui_FISCAL_iCCDEstornar
from scripts.fiscal.ui_fiscal_iccdimprimirarquivo import Ui_ui_FISCAL_iCCDImprimirArquivo
from scripts.fiscal.ui_fiscal_iccdimprimirtexto import Ui_ui_FISCAL_iCCDImprimirTexto
from scripts.fiscal.ui_fiscal_icfabrir import Ui_ui_FISCAL_iCFAbrir
from scripts.fiscal.ui_fiscal_icfbpabrir import Ui_ui_FISCAL_iCFBPAbrir
from scripts.fiscal.ui_fiscal_icfbpvender import Ui_ui_FISCAL_iCFBPVender
from scripts.fiscal.ui_fiscal_icfcancelaracrescimoitem import Ui_ui_FISCAL_iCFCancelarAcrescimoItem
from scripts.fiscal.ui_fiscal_icfcancelardescontoitem import Ui_ui_FISCAL_iCFCancelarDescontoItem
from scripts.fiscal.ui_fiscal_icfcancelaritem import Ui_ui_FISCAL_iCFCancelarItem
from scripts.fiscal.ui_fiscal_icfcancelaritemparcial import Ui_ui_FISCAL_iCFCancelarItemParcial
from scripts.fiscal.ui_fiscal_icfcancelarultimoitemparcial import Ui_ui_FISCAL_iCFCancelarUltimoItemParcial
from scripts.fiscal.ui_fiscal_icfefetuarpagamento import Ui_ui_FISCAL_iCFEfetuarPagamento
from scripts.fiscal.ui_fiscal_icfefetuarpagamentoformatado import Ui_ui_FISCAL_iCFEfetuarPagamentoFormatado
from scripts.fiscal.ui_fiscal_icfencerrar import Ui_ui_FISCAL_iCFEncerrar
from scripts.fiscal.ui_fiscal_icfencerrarconfigmsg import Ui_ui_FISCAL_iCFEncerrarConfigMsg
from scripts.fiscal.ui_fiscal_icfidentificarconsumidor import Ui_ui_FISCAL_iCFIdentificarConsumidor
from scripts.fiscal.ui_fiscal_icflancaracrescimoitem import Ui_ui_FISCAL_iCFLancarAcrescimoItem
from scripts.fiscal.ui_fiscal_icflancaracrescimoultimoitem import Ui_ui_FISCAL_iCFLancarAcrescimoUltimoItem
from scripts.fiscal.ui_fiscal_icflancardescontoitem import Ui_ui_FISCAL_iCFLancarDescontoItem
from scripts.fiscal.ui_fiscal_icflancardescontoultimoitem import Ui_ui_FISCAL_iCFLancarDescontoUltimoItem
from scripts.fiscal.ui_fiscal_icftotalizarcupom import Ui_ui_FISCAL_iCFTotalizarCupom
from scripts.fiscal.ui_fiscal_icfvender import Ui_ui_FISCAL_iCFVender
from scripts.fiscal.ui_fiscal_icfvenderresumido import Ui_ui_FISCAL_iCFVenderResumido
from scripts.fiscal.ui_fiscal_icfvendersemdesc import Ui_ui_FISCAL_iCFVenderSemDesc
from scripts.fiscal.ui_fiscal_ichequeimprimir import Ui_ui_FISCAL_iChequeImprimir
from scripts.fiscal.ui_fiscal_icnfabrir import Ui_ui_FISCAL_iCNFAbrir
from scripts.fiscal.ui_fiscal_icnfcancelaracrescimoitem import Ui_ui_FISCAL_iCNFCancelarAcrescimoItem
from scripts.fiscal.ui_fiscal_icnfcancelardescontoitem import Ui_ui_FISCAL_iCNFCancelarDescontoItem
from scripts.fiscal.ui_fiscal_icnfcancelaritem import Ui_ui_FISCAL_iCNFCancelarItem
from scripts.fiscal.ui_fiscal_icnfefetuarpagamento import Ui_ui_FISCAL_iCNFEfetuarPagamento
from scripts.fiscal.ui_fiscal_icnfefetuarpagamentoformatado import Ui_ui_FISCAL_iCNFEfetuarPagamentoFormatado
from scripts.fiscal.ui_fiscal_icnfencerrar import Ui_ui_FISCAL_iCNFEncerrar
from scripts.fiscal.ui_fiscal_icnfreceber import Ui_ui_FISCAL_iCNFReceber
from scripts.fiscal.ui_fiscal_icnfrecebersemdesc import Ui_ui_FISCAL_iCNFReceberSemDesc
from scripts.fiscal.ui_fiscal_icnftotalizarcomprovante import Ui_ui_FISCAL_iCNFTotalizarComprovante
from scripts.fiscal.ui_fiscal_iestornarpagamento import Ui_ui_FISCAL_iEstornarPagamento
from scripts.fiscal.ui_fiscal_iimprimircodigobarras import Ui_ui_FISCAL_iImprimirCodigoBarras
from scripts.fiscal.ui_fiscal_imfler import Ui_ui_FISCAL_iMFLer
from scripts.fiscal.ui_fiscal_imflerserial import Ui_ui_FISCAL_iMFLerSerial
from scripts.fiscal.ui_fiscal_irgabrir import Ui_ui_FISCAL_iRGAbrir
from scripts.fiscal.ui_fiscal_irgabririndice import Ui_ui_FISCAL_iRGAbrirIndice
from scripts.fiscal.ui_fiscal_irgimprimirtexto import Ui_ui_FISCAL_iRGImprimirTexto
from scripts.fiscal.ui_fiscal_isangria import Ui_ui_FISCAL_iSangria
from scripts.fiscal.ui_fiscal_isuprimento import Ui_ui_FISCAL_iSuprimento
from scripts.fiscal.ui_fiscal_itef_imprimirresposta import Ui_ui_FISCAL_iTEF_ImprimirResposta
from scripts.fiscal.ui_fiscal_itef_imprimirrespostacartao import Ui_ui_FISCAL_iTEF_ImprimirRespostaCartao
from scripts.fiscal.ui_fiscal_menufiscal import Ui_ui_FISCAL_MenuFiscal
from scripts.fiscal.ui_fiscal_menufiscal_arqmfd import Ui_ui_FISCAL_MenuFiscal_ArqMFD
from scripts.fiscal.ui_fiscal_menufiscal_lmfc import Ui_ui_FISCAL_MenuFiscal_LMFC
from scripts.fiscal.ui_fiscal_menufiscal_lmfs import Ui_ui_FISCAL_MenuFiscal_LMFS
from scripts.fiscal.ui_fiscal_rcalcularmd5 import Ui_ui_FISCAL_rCalcularMD5
from scripts.fiscal.ui_fiscal_rcodigomodelofiscal import Ui_ui_FISCAL_rCodigoModeloFiscal
from scripts.fiscal.ui_fiscal_regalterarvalor import Ui_ui_FISCAL_regAlterarValor
from scripts.fiscal.ui_fiscal_regcfcupomadicionaldllconfig import Ui_ui_FISCAL_regCFCupomAdicionalDllConfig
from scripts.fiscal.ui_fiscal_regretornavalorchave import Ui_ui_FISCAL_regRetornaValorChave
from scripts.fiscal.ui_fiscal_retornosstatusecf import Ui_ui_FISCAL_RetornosStatusECF
from scripts.fiscal.ui_fiscal_rgerarespelhomfd import Ui_ui_FISCAL_rGerarEspelhoMFD
from scripts.fiscal.ui_fiscal_rgerarmf import Ui_ui_FISCAL_rGerarMF
from scripts.fiscal.ui_fiscal_rgerarmfd import Ui_ui_FISCAL_rGerarMFD
from scripts.fiscal.ui_fiscal_rgerarnfp import Ui_ui_FISCAL_rGerarNFP
from scripts.fiscal.ui_fiscal_rgerarrelatorio import Ui_ui_FISCAL_rGerarRelatorio
from scripts.fiscal.ui_fiscal_rgerarrelatoriooffline import Ui_ui_FISCAL_rGerarRelatorioOffline
from scripts.fiscal.ui_fiscal_rgerarsintegra import Ui_ui_FISCAL_rGerarSINTEGRA
from scripts.fiscal.ui_fiscal_rgerarsped import Ui_ui_FISCAL_rGerarSPED
from scripts.fiscal.ui_fiscal_rgerartdm import Ui_ui_FISCAL_rGerarTDM
from scripts.fiscal.ui_fiscal_rleituraxcustomizada import Ui_ui_FISCAL_rLeituraXCustomizada
from scripts.fiscal.ui_fiscal_rretornargtcodificado import Ui_ui_FISCAL_rRetornarGTCodificado
from scripts.fiscal.ui_fiscal_rretornarnumeroseriecodificado import Ui_ui_FISCAL_rRetornarNumeroSerieCodificado
from scripts.fiscal.ui_fiscal_rrsachavepublica import Ui_ui_FISCAL_rRSAChavePublica
from scripts.fiscal.ui_fiscal_rverificargtcodificado import Ui_ui_FISCAL_rVerificarGTCodificado
from scripts.fiscal.ui_fiscal_rverificarnumeroseriecodificado import Ui_ui_FISCAL_rVerificarNumeroSerieCodificado
from scripts.fiscal.ui_fiscal_testedevendasempararbufferizando import Ui_ui_FISCAL_TesteDeVendaSemPararBufferizando
from scripts.fiscal.ui_fiscal_confcadastrar import Ui_ui_FISCAL_confCadastrar
from scripts.ui_geral_contatossuporte import Ui_ui_Geral_ContatosSuporte


class Ui_MainWindowFISCAL(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindowFISCAL, self).__init__()

        self.setupUi(self)

        self.pushButtonEncerrar.clicked.connect(self.on_pushButtonEncerrar_clicked)
        self.pushButtonContatos.clicked.connect(self.on_pushButtonContatos_clicked)
        self.actionM_todos_para_Retornos_e_Status.triggered.connect(self.on_retorno_e_Status_triggered)
        self.actionM_todo_iCFAbrir_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFAbrir_ECF_Daruma_triggered)
        self.actionM_todo_iCFAbrirPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFAbrirPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCFVender_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFVender_ECF_Daruma_triggered)
        self.actionM_todo_iCFVenderSemDesc_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFVenderSemDesc_ECF_Daruma_triggered)
        self.actionM_todo_iCFVenderResumido_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFVenderResumido_ECF_Daruma_triggered)
        self.actionM_todo_iCFLancarDescontoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFLancarDescontoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarItemParcial_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarItemParcial_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarDescontoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarDescontoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCFTotalizarCupom_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFTotalizarCupom_ECF_Daruma_triggered)
        self.actionM_todo_iCFTotalizarPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFTotalizarPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma_triggered)
        self.actionM_todo_iCFEfetuarPagamento_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEfetuarPagamento_ECF_Daruma_triggered)
        self.actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma_triggered)
        self.actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCFEncerrarPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEncerrarPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCFEncerrarResumido_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEncerrarResumido_ECF_Daruma_triggered)
        self.actionM_todo_iCFEncerrar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEncerrar_ECF_Daruma_triggered)
        self.actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma_triggered)
        self.actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma_triggered)
        self.actionM_todo_iCFCancelar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFCancelar_ECF_Daruma_triggered)
        self.actionM_todo_iCFIdentificarConsumidor_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFIdentificarConsumidor_ECF_Daruma_triggered)
        self.actionConfigurac_o_Cupom_Mania.triggered.connect(self.on_actionConfigurac_o_Cupom_Mania_triggered)
        self.actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania.triggered.connect(self.on_actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania_triggered)
        self.actionM_todo_iEstornarPagamento_ECF_Daruma.triggered.connect(self.on_actionM_todo_iEstornarPagamento_ECF_Daruma_triggered)
        self.actionTeste_de_Venda_de_Itens_Sem_Parar.triggered.connect(self.on_actionTeste_de_Venda_de_Itens_Sem_Parar_triggered)
        self.actionCupom_Fiscal_Completo.triggered.connect(self.on_actionCupom_Fiscal_Completo_triggered)
        self.actionCupom_Fiscal_Resumido.triggered.connect(self.on_actionCupom_Fiscal_Resumido_triggered)
        self.actionCupom_Fiscal_Pr_Venda.triggered.connect(self.on_actionCupom_Fiscal_Pr_Venda_triggered)
        self.actionM_todo_iCCDAbrir_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDAbrir_ECF_Daruma_triggered)
        self.actionM_todo_iCCDAbrirPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDAbrirPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCCDAbrirSimplificado_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDAbrirSimplificado_ECF_Daruma_triggered)
        self.actionM_todo_iCCDImprimirTexto_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDImprimirTexto_ECF_Daruma_triggered)
        self.actionM_todo_iCCDImprimirArquivo_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDImprimirArquivo_ECF_Daruma_triggered)
        self.actionM_todo_iCCDFechar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDFechar_ECF_Daruma_triggered)
        self.actionM_todo_iCCDEstornar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDEstornar_ECF_Daruma_triggered)
        self.actionM_todo_iCCDEstornarPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCCDEstornarPadrao_ECF_Daruma_triggered)
        self.action2_Via_de_CCD.triggered.connect(self.on_action2_Via_de_CCD_triggered)
        self.actionExemplo_CCD_Completo.triggered.connect(self.on_actionExemplo_CCD_Completo_triggered)
        self.actionExemplo_Completo_TEF.triggered.connect(self.on_actionExemplo_Completo_TEF_triggered)
        self.actionM_todo_eTEF_EsperarArquivo_ECF_Daruma.triggered.connect(self.on_actionM_todo_eTEF_EsperarArquivo_ECF_Daruma_triggered)
        self.actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma_triggered)
        self.actionM_todo_iTEF_ImprimirResposta_ECF_Daruma.triggered.connect(self.on_actionM_todo_iTEF_ImprimirResposta_ECF_Daruma_triggered)
        self.actionM_todo_eTEF_TravarTeclado_ECF_Daruma.triggered.connect(self.on_actionM_todo_eTEF_TravarTeclado_ECF_Daruma_triggered)
        self.actionM_todo_iTEF_Fechar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iTEF_Fechar_ECF_Daruma_triggered)
        self.actionM_todo_eTEF_SetarFoco_ECF_Daruma.triggered.connect(self.on_actionM_todo_eTEF_SetarFoco_ECF_Daruma_triggered)
        self.actionM_todo_iCNFAbrir_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFAbrir_ECF_Daruma_triggered)
        self.actionM_todo_iCNFAbrirPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFAbrirPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCNFReceber_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFReceber_ECF_Daruma_triggered)
        self.actionM_todo_iCNFReceberSemDesc_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFReceberSemDesc_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarItem_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma_triggered)
        self.actionM_todo_iCNFTotalizarComprovante_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFTotalizarComprovante_ECF_Daruma_triggered)
        self.actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma_triggered)
        self.actionM_todo_iCNFEfetuarPagamento_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFEfetuarPagamento_ECF_Daruma_triggered)
        self.actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma_triggered)
        self.actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCNFEncerrar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFEncerrar_ECF_Daruma_triggered)
        self.actionM_todo_iCNFEncerrarPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFEncerrarPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iCNFCancelar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCNFCancelar_ECF_Daruma_triggered)
        self.actionExemplo_CNF_Detalhado.triggered.connect(self.on_actionExemplo_CNF_Detalhado_triggered)
        self.actionM_todo_iRGAbrir_ECF_Daruma.triggered.connect(self.on_actionM_todo_iRGAbrir_ECF_Daruma_triggered)
        self.actionM_todo_iRGAbrirIndice_ECF_Daruma.triggered.connect(self.on_actionM_todo_iRGAbrirIndice_ECF_Daruma_triggered)
        self.actionM_todo_iRGAbrirPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iRGAbrirPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iRGImprimirTexto_ECF_Daruma.triggered.connect(self.on_actionM_todo_iRGImprimirTexto_ECF_Daruma_triggered)
        self.actionM_todo_iRGFechar_ECF_Daruma.triggered.connect(self.on_actionM_todo_iRGFechar_ECF_Daruma_triggered)
        self.actionM_todo_iLeituraX_ECF_Daruma.triggered.connect(self.on_actionM_todo_iLeituraX_ECF_Daruma_triggered)
        self.actionM_todo_rLeituraX_ECF_Daruma.triggered.connect(self.on_actionM_todo_rLeituraX_ECF_Daruma_triggered)
        self.actionM_todo_rLeituraXCustomizada_ECF_Daruma.triggered.connect(self.on_actionM_todo_rLeituraXCustomizada_ECF_Daruma_triggered)
        self.actionM_todo_iReducaoZ_ECF_Daruma.triggered.connect(self.on_actionM_todo_iReducaoZ_ECF_Daruma_triggered)
        self.actionM_todo_iSangria_ECF_Daruma.triggered.connect(self.on_actionM_todo_iSangria_ECF_Daruma_triggered)
        self.actionM_todo_iSangriaPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iSangriaPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iSuprimento_ECF_Daruma.triggered.connect(self.on_actionM_todo_iSuprimento_ECF_Daruma_triggered)
        self.actionM_todo_iSuprimentoPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_iSuprimentoPadrao_ECF_Daruma_triggered)
        self.actionM_todo_iMFLer_ECF_Daruma.triggered.connect(self.on_actionM_todo_iMFLer_ECF_Daruma_triggered)
        self.actionM_todo_iMFLerSerial_ECF_Daruma.triggered.connect(self.on_actionM_todo_iMFLerSerial_ECF_Daruma_triggered)
        self.actionM_todo_confCadastrar_ECF_Daruma.triggered.connect(self.on_actionM_todo_confCadastrar_ECF_Daruma_triggered)
        self.actionM_todo_confCadastrarPadrao_ECF_Daruma.triggered.connect(self.on_actionM_todo_confCadastrarPadrao_ECF_Daruma_triggered)
        self.actionLoja.triggered.connect(self.on_actionLoja_triggered)
        self.actionHabilitarHVerao.triggered.connect(self.on_actionHabilitarHVerao_triggered)
        self.actionDesabilitarHVerao.triggered.connect(self.on_actionDesabilitarHVerao_triggered)
        self.actionHabilitarMPreVenda.triggered.connect(self.on_actionHabilitarMPreVenda_triggered)
        self.actionDesabilitarMPreVenda.triggered.connect(self.on_actionDesabilitarMPreVenda_triggered)
        self.actionAvan_o_de_Papel.triggered.connect(self.on_actionAvan_o_de_Papel_triggered)
        self.actionConfOperador.triggered.connect(self.on_actionConfOperador_triggered)
        self.actionM_todos_para_Retornos_e_Status.triggered.connect(self.on_actionM_todos_para_Retornos_e_Status_triggered)
        self.actionM_todo_iCFBPAbrir_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFBPAbrir_ECF_Daruma_triggered)
        self.actionM_todo_iCFBPVender_ECF_Daruma.triggered.connect(self.on_actionM_todo_iCFBPVender_ECF_Daruma_triggered)
        self.actionM_todo_confCFBPProgramarUF_ECF_Daruma.triggered.connect(self.on_actionM_todo_confCFBPProgramarUF_ECF_Daruma_triggered)
        self.actionM_todo_eAcionarGuilhotina_ECF_Daruma.triggered.connect(self.on_actionM_todo_eAcionarGuilhotina_ECF_Daruma_triggered)
        self.actionM_todo_eAbrirGaveta_ECF_Daruma.triggered.connect(self.on_actionM_todo_eAbrirGaveta_ECF_Daruma_triggered)
        self.actionM_todo_rStatusGaveta_ECF_Daruma.triggered.connect(self.on_actionM_todo_rStatusGaveta_ECF_Daruma_triggered)
        self.actionM_todo_eCarregarBitmapPromocional_ECF_Daruma.triggered.connect(self.on_actionM_todo_eCarregarBitmapPromocional_ECF_Daruma_triggered)
        self.actionM_todo_iImprimirCodigoBarras_ECF_Daruma.triggered.connect(self.on_actionM_todo_iImprimirCodigoBarras_ECF_Daruma_triggered)
        self.actionM_todo_regRetornaValorChave_DarumaFramework.triggered.connect(self.on_actionM_todo_regRetornaValorChave_DarumaFramework_triggered)
        self.actionM_todo_regAlterarValor_Daruma.triggered.connect(self.on_actionM_todo_regAlterarValor_Daruma_triggered)
        self.actionM_todo_eDefinirProduto_Daruma.triggered.connect(self.on_actionM_todo_eDefinirProduto_Daruma_triggered)
        self.actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma.triggered.connect(self.on_actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma_triggered)
        self.actionM_todo_eDefinirModoRegistro_Daruma.triggered.connect(self.on_actionM_todo_eDefinirModoRegistro_Daruma_triggered)
        self.actionM_todo_iChequeImprimir_FS2100_Daruma.triggered.connect(self.on_actionM_todo_iChequeImprimir_FS2100_Daruma_triggered)
        self.actionRGerarEspelhoMFD_ECF_Daruma.triggered.connect(self.on_actionRGerarEspelhoMFD_ECF_Daruma_triggered)
        self.actionM_todo_rGerarRelatorio_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarRelatorio_ECF_Daruma_triggered)
        self.actionM_todo_rGerarRelatorioOffline_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarRelatorioOffline_ECF_Daruma_triggered)
        self.actionM_todo_rGerarMF_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarMF_ECF_Daruma_triggered)
        self.actionM_todo_rGerarMFD_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarMFD_ECF_Daruma_triggered)
        self.actionM_todo_rGerarTDM_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarTDM_ECF_Daruma_triggered)
        self.actionM_todo_rGerarSPED_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarSPED_ECF_Daruma_triggered)
        self.actionM_todo_rGerarSINTEGRA_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarSINTEGRA_ECF_Daruma_triggered)
        self.actionM_todo_rGerarNFP_ECF_Daruma.triggered.connect(self.on_actionM_todo_rGerarNFP_ECF_Daruma_triggered)
        self.actionM_todo_rCalcularMD5_ECF_Daruma.triggered.connect(self.on_actionM_todo_rCalcularMD5_ECF_Daruma_triggered)
        self.actionM_todo_rRetornarGTCodificado_ECF_Daruma.triggered.connect(self.on_actionM_todo_rRetornarGTCodificado_ECF_Daruma_triggered)
        self.actionM_todo_rVerificarGTCodificado_ECF_Daruma.triggered.connect(self.on_actionM_todo_rVerificarGTCodificado_ECF_Daruma_triggered)
        self.actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma.triggered.connect(self.on_actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma_triggered)
        self.actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma.triggered.connect(self.on_actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma_triggered)
        self.actionM_todo_rCodigoModeloFiscal_ECF_Daruma.triggered.connect(self.on_actionM_todo_rCodigoModeloFiscal_ECF_Daruma_triggered)
        self.actionM_todo_eRSAAssinarArquivo_ECF_Daruma.triggered.connect(self.on_actionM_todo_eRSAAssinarArquivo_ECF_Daruma_triggered)
        self.actionM_todo_rRSAChavePublica_ECF_Daruma.triggered.connect(self.on_actionM_todo_rRSAChavePublica_ECF_Daruma_triggered)
        self.actionM_todo_eMemoriaFiscal_ECF_Daruma.triggered.connect(self.on_actionM_todo_eMemoriaFiscal_ECF_Daruma_triggered)
        self.action_MenuFiscal_LX.triggered.connect(self.on_action_MenuFiscal_LX_triggered)
        self.action_MenuFiscal_LMFC.triggered.connect(self.on_action_MenuFiscal_LMFC_triggered)
        self.action_MenuFiscal_LMFS.triggered.connect(self.on_action_MenuFiscal_LMFS_triggered)
        self.action_MenuFiscal_Arq_MFD.triggered.connect(self.on_action_MenuFiscal_Arq_MFD_triggered)
        self.action_MenuFiscal_Espelho_MFD.triggered.connect(self.on_action_MenuFiscal_Espelho_MFD_triggered)
        self.action_MenuFiscal_Tab_Produto.triggered.connect(self.on_action_MenuFiscal_Tab_Produto_triggered)
        self.action_MenuFiscal_Estoque.triggered.connect(self.on_action_MenuFiscal_Estoque_triggered)
        self.action_MenuFiscal_Movimento_por_ECF.triggered.connect(self.on_action_MenuFiscal_Movimento_por_ECF_triggered)
        self.action_MenuFiscal_Meios_de_Pgto.triggered.connect(self.on_action_MenuFiscal_Meios_de_Pgto_triggered)
        self.action_MenuFiscal_Vendas_por_Per_odo.triggered.connect(self.on_action_MenuFiscal_Vendas_por_Per_odo_triggered)
        self.action_MenuFiscal_Identifica_ao_do_PAF_ECF.triggered.connect(self.on_action_MenuFiscal_Identifica_ao_do_PAF_ECF_triggered)
        self.action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o.triggered.connect(self.on_action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o_triggered)
        self.action_MenuFiscal_DAV_Emitidos.triggered.connect(self.on_action_MenuFiscal_DAV_Emitidos_triggered)
        self.action_MenuFiscal_Encerrantes.triggered.connect(self.on_action_MenuFiscal_Encerrantes_triggered)
        self.action_MenuFiscal_Transf_Mesas.triggered.connect(self.on_action_MenuFiscal_Transf_Mesas_triggered)
        self.action_MenuFiscal_Manifesto_Fiscal_de_Viagem.triggered.connect(self.on_action_MenuFiscal_Manifesto_Fiscal_de_Viagem_triggered)
        self.action_MenuFiscal_Cupom_de_Embarque.triggered.connect(self.on_action_MenuFiscal_Cupom_de_Embarque_triggered)
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque.triggered.connect(self.on_action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque_triggered)
        self.action_MenuFiscal_Cupons_de_Embarque_Gratuidade.triggered.connect(self.on_action_MenuFiscal_Cupons_de_Embarque_Gratuidade_triggered)
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade.triggered.connect(self.on_action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade_triggered)
        self.action_MenuFiscal_Ped_gios.triggered.connect(self.on_action_MenuFiscal_Ped_gios_triggered)
        self.action_MenuFiscal_Manuten_ao_de_Bombas.triggered.connect(self.on_action_MenuFiscal_Manuten_ao_de_Bombas_triggered)

        '''
        #CHAMA A FUNÇAO PARA CARREGAR A BIBLIOTECA DARUMAFRAMEWORK
        carregarDarumaFramework(self)
        #CHAMA A FUNÇAO DE EXECUÇAO DE PARAMETROS INICIAIS PARA EXECUÇÃO DO EXEMPLO, É TOTALMENTE OPCIONAL.
        ConfiguracoesIniciaisECF()
        #CHAMA A FUNÇÃO DE VERIFICAÇÃO DE IMPRESSORA LIGADA E IMPRIME RESULTADO NA TELA, UTILIZANDO O QMESSAGEBOX. TAMBÉM É OPCIONAL
        VerificaImpressoraLigada(self)
        '''

    def on_retorno_e_Status_triggered(self):
        self.form_FISCAL_RetornosStatusECF = Ui_ui_FISCAL_RetornosStatusECF()
        self.form_FISCAL_RetornosStatusECF.show()

    def on_actionM_todo_iCFAbrir_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFAbrir = Ui_ui_FISCAL_iCFAbrir()
        self.form_FISCAL_iCFAbrir.show()

    def on_actionM_todo_iCFAbrirPadrao_ECF_Daruma_triggered(self):
        tratarRetornoFiscal(iCFAbrirPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCFVender_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFVender = Ui_ui_FISCAL_iCFVender()
        self.form_FISCAL_iCFVender.show()

    def on_actionM_todo_iCFVenderSemDesc_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFVenderSemDesc = Ui_ui_FISCAL_iCFVenderSemDesc()
        self.form_FISCAL_iCFVenderSemDesc.show()

    def on_actionM_todo_iCFVenderResumido_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFVenderResumido = Ui_ui_FISCAL_iCFVenderResumido()
        self.form_FISCAL_iCFVenderResumido.show()

    def on_actionM_todo_iCFLancarDescontoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFLancarDescontoItem = Ui_ui_FISCAL_iCFLancarDescontoItem()
        self.form_FISCAL_iCFLancarDescontoItem.show()

    def on_actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFLancarAcrescimoItem = Ui_ui_FISCAL_iCFLancarAcrescimoItem()
        self.form_FISCAL_iCFLancarAcrescimoItem.show()

    def on_actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFLancarAcrescimoUltimoItem = Ui_ui_FISCAL_iCFLancarAcrescimoUltimoItem()
        self.form_FISCAL_iCFLancarAcrescimoUltimoItem.show()

    def on_actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFLancarDescontoUltimoItem = Ui_ui_FISCAL_iCFLancarDescontoUltimoItem()
        self.form_FISCAL_iCFLancarDescontoUltimoItem.show()

    def on_actionM_todo_iCFCancelarItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFCancelarItem = Ui_ui_FISCAL_iCFCancelarItem()
        self.form_FISCAL_iCFCancelarItem.show()

    def on_actionM_todo_iCFCancelarUltimoItem_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFCancelarUltimoItem_ECF_Daruma(), self)

    def on_actionM_todo_iCFCancelarItemParcial_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFCancelarItemParcial = Ui_ui_FISCAL_iCFCancelarItemParcial()
        self.form_FISCAL_iCFCancelarItemParcial.show()

    def on_actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFCancelarUltimoItemParcial = Ui_ui_FISCAL_iCFCancelarUltimoItemParcial()
        self.form_FISCAL_iCFCancelarUltimoItemParcial.show()

    def on_actionM_todo_iCFCancelarDescontoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFCancelarDescontoItem = Ui_ui_FISCAL_iCFCancelarDescontoItem()
        self.form_FISCAL_iCFCancelarDescontoItem.show()

    def on_actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFCancelarAcrescimoItem = Ui_ui_FISCAL_iCFCancelarAcrescimoItem()
        self.form_FISCAL_iCFCancelarAcrescimoItem.show()

    def on_actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFCancelarAcrescimoUltimoItem_ECF_Daruma(), self)

    def on_actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFCancelarDescontoUltimoItem_ECF_Daruma(), self)

    def on_actionM_todo_iCFTotalizarCupom_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFTotalizarCupom = Ui_ui_FISCAL_iCFTotalizarCupom()
        self.form_FISCAL_iCFTotalizarCupom.show()

    def on_actionM_todo_iCFTotalizarPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFTotalizarCupomPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFCancelarAcrescimoSubtotal_ECF_Daruma(), self)

    def on_actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFCancelarDescontoSubtotal_ECF_Daruma(), self)

    def on_actionM_todo_iCFEfetuarPagamento_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFEfetuarPagamento = Ui_ui_FISCAL_iCFEfetuarPagamento()
        self.form_FISCAL_iCFEfetuarPagamento.show()

    def on_actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFEfetuarPagamentoFormatado = Ui_ui_FISCAL_iCFEfetuarPagamentoFormatado()
        self.form_FISCAL_iCFEfetuarPagamentoFormatado.show()

    def on_actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFEfetuarPagamentoPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCFEncerrarPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFEncerrarPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCFEncerrarResumido_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFEncerrarResumido_ECF_Daruma(), self)

    def on_actionM_todo_iCFEncerrar_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFEncerrar = Ui_ui_FISCAL_iCFEncerrar()
        self.form_FISCAL_iCFEncerrar.show()

    def on_actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFEncerrarConfigMsg = Ui_ui_FISCAL_iCFEncerrarConfigMsg()
        self.form_FISCAL_iCFEncerrarConfigMsg.show()

    def on_actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFEmitirCupomAdicional_ECF_Daruma(), self)

    def on_actionM_todo_iCFCancelar_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCFCancelar_ECF_Daruma(), self)

    def on_actionM_todo_iCFIdentificarConsumidor_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFIdentificarConsumidor = Ui_ui_FISCAL_iCFIdentificarConsumidor()
        self.form_FISCAL_iCFIdentificarConsumidor.show()

    def on_actionConfigurac_o_Cupom_Mania_triggered(self):
        self.form_FISCAL_ConfiguracaoCupomMania = Ui_ui_FISCAL_ConfiguracaoCupomMania()
        self.form_FISCAL_ConfiguracaoCupomMania.show()

    def on_actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania_triggered(self):
        cISS = b''
        cICMS = b''

        rCMEfetuarCalculo_ECF_Daruma(cISS, cICMS)

        # MONTO A STRING PARA APRESENTAÇÃO NO QMESSAGEBOX
        StrTotalImposto = ''.join(["Total ISS: ", cISS.decode(), "\n", "Total ICMS: ", cICMS.decode()])

        QMessageBox.information(self, "DarumaFramework - Python/Qt", StrTotalImposto)

    def on_actionM_todo_iEstornarPagamento_ECF_Daruma_triggered(self):
        self.form_FISCAL_iEstornarPagamento = Ui_ui_FISCAL_iEstornarPagamento()
        self.form_FISCAL_iEstornarPagamento.show()

    def on_actionTeste_de_Venda_de_Itens_Sem_Parar_triggered(self):
        self.form_FISCAL_TesteDeVendaSemPararBufferizando = Ui_ui_FISCAL_TesteDeVendaSemPararBufferizando()
        self.form_FISCAL_TesteDeVendaSemPararBufferizando.show()

    def on_actionCupom_Fiscal_Completo_triggered(self):

        # Exemplo de Cupom Fiscal usando as funçoes mais completas, com mais recursos.

        iCFAbrir_ECF_Daruma("111.111.111.11","Daruma Developers Community","Avenida Shishima Hifumi,2910")
        iCFVender_ECF_Daruma("F1","1,00","1,00","D$","0,00","12345678901234","UN","REFRIGERANTE")
        iCFVender_ECF_Daruma("F1","1,00","1,00","D$","0,10","12345678901234","UN","REFRIGERANTE")
        iCFVender_ECF_Daruma("F1","1,00","1,00","D%","10,00","12345678901234","UN","REFRIGERANTE")
        iCFVender_ECF_Daruma("F1","1,00","1,00","A$","0,10","12345678901234","UN","REFRIGERANTE")
        iCFVender_ECF_Daruma("F1","1,00","1,00","A%","10,00","12345678901234","UN","REFRIGERANTE")
        iCFTotalizarCupom_ECF_Daruma("A%","10,00")
        iCFEfetuarPagamento_ECF_Daruma("Dinheiro","10,00","Pagamento Efetuado")
        iRetorno = iCFEncerrar_ECF_Daruma("0","Mensagem Promocional com até 8 linhas")
        tratarRetornoFiscal(iRetorno, self)

    def on_actionCupom_Fiscal_Resumido_triggered(self):

        iCFAbrirPadrao_ECF_Daruma()
        iCFVenderResumido_ECF_Daruma("F1","1,00","12345678901234","REFRIGERANTE")
        iCFTotalizarCupomPadrao_ECF_Daruma()

        # Utilizarei a funçao iCFEncerrarResumido_ECF_Daruma que já passa a forma de pagamento padrão, não sendo
        # necessário eu enviar a forma de pagamento antes.
        iCFEfetuarPagamentoPadrao_ECF_Daruma()

        iRetorno = iCFEncerrarResumido_ECF_Daruma()
        tratarRetornoFiscal(iRetorno, self)

    def on_actionCupom_Fiscal_Pr_Venda_triggered(self):


        StrMensagemAviso = "Importante: \n"+"Funcionalidade disponível apenas no ECF MACH1 e MACH2."

        QMessageBox.information(self, "DarumaFramework - Python/Qt", StrMensagemAviso)

        #ALTERA O XML PARA HABILITAR O MODO PRÉ VENDA
        regAlterarValor_Daruma("ECF\\CF\\ModoPreVenda","1")

        #INICIA A IMPRESSAO DO CUPOM FISCAL
        iCFAbrir_ECF_Daruma("111.111.111.11","Daruma Developers Community","Avenida Shishima Hifumi,2910")

        for i in range(0, 50):
            iCFVender_ECF_Daruma("F1","1,00","1,00","D$","0,00","12345678901234","UN","ITE.")

        iCFTotalizarCupomPadrao_ECF_Daruma()
        iCFEfetuarPagamentoPadrao_ECF_Daruma()
        iRetorno = iCFEncerrar_ECF_Daruma("0","MENSAGEM PROMOCIONAL COM ATE 8 LINHAS")
        tratarRetornoFiscal(iRetorno, self)

        #ALTERA O XML PARA DESABILITAR O MODO PRÉ VENDA
        regAlterarValor_Daruma("ECF\\CF\\ModoPreVen.","0")

    # FIM
    # MÉTODOS DE CUPOM FISCAL



    # CCD / COMPROVANTE DÉBIDO CRÉDITO - TEF
    # INICIO

    def on_actionM_todo_iCCDAbrir_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCCDAbrir = Ui_ui_FISCAL_iCCDAbrir()
        self.form_FISCAL_iCCDAbrir.show()

    def on_actionM_todo_iCCDAbrirPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCCDAbrirPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCCDAbrirSimplificado_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCCDAbrirSimplificado = Ui_ui_FISCAL_iCCDAbrirSimplificado()
        self.form_FISCAL_iCCDAbrirSimplificado.show()

    def on_actionM_todo_iCCDImprimirTexto_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCCDImprimirTexto = Ui_ui_FISCAL_iCCDImprimirTexto()
        self.form_FISCAL_iCCDImprimirTexto.show()

    def on_actionM_todo_iCCDImprimirArquivo_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCCDImprimirArquivo = Ui_ui_FISCAL_iCCDImprimirArquivo()
        self.form_FISCAL_iCCDImprimirArquivo.show()

    def on_actionM_todo_iCCDFechar_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCCDFechar_ECF_Daruma(), self)

    def on_actionM_todo_iCCDEstornar_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCCDEstornar = Ui_ui_FISCAL_iCCDEstornar()
        self.form_FISCAL_iCCDEstornar.show()

    def on_actionM_todo_iCCDEstornarPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCCDEstornarPadrao_ECF_Daruma(), self)

    def on_action2_Via_de_CCD_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCCDSegundaVia_ECF_Daruma(), self)

    def on_actionExemplo_CCD_Completo_triggered(self):

        QMessageBox.information(self, "DarumaFramework - Python/Qt","Procedimento necessita de Forma de Pagamento -CARTÃO- cadastrado no ECF.\n Caso não tenha esta forma cadastrada, o pagamento será efetuado como DINHEIRO e o vinculado não sera impresso.")

        iRetorno = iCFAbrir_ECF_Daruma("111.111.111.11","Daruma Developers Community","Avenida Shishima Hifumi,2910")
        if(iRetorno != 1):
            tratarRetornoFiscal(iRetorno, self)
            iCFCancelar_ECF_Daruma()

        for i in range(0, 10):
            iCFVender_ECF_Daruma("F1","1,00","1,00","D$","0,00","12345678901234","UN","ITEM")

        iCFTotalizarCupom_ECF_Daruma("A%","10,00")
        iCFEfetuarPagamento_ECF_Daruma("TEF","10,00","Pagamento Efetuado")
        iCFEncerrar_ECF_Daruma("0","Mensagem Promocional com até 8 linhas")

        iRetorno = iCCDAbrirPadrao_ECF_Daruma()
        if(iRetorno != 1):
            tratarRetornoFiscal(iRetorno, self)
            iCFCancelar_ECF_Daruma()

        iCCDImprimirTexto_ECF_Daruma("Imprimindo Texto Livre em CCD")
        iCCDImprimirTexto_ECF_Daruma("Imprimindo Texto Livre em CCD")
        iCCDImprimirTexto_ECF_Daruma("Imprimindo Texto Livre em CCD")
        iCCDImprimirTexto_ECF_Daruma("Imprimindo Texto Livre em CCD")
        iRetorno = iCCDFechar_ECF_Daruma()
        tratarRetornoFiscal(iRetorno, self)

    def on_actionExemplo_Completo_TEF_triggered(self):
        QMessageBox.information(self,"DarumaFramework - Python/Qt","Procedimento necessita de Forma de Pagamento -CARTÃO- cadastrado no ECF.")
        QMessageBox.information(self,"DarumaFramework - Qt/Ptyhon","É necessario que exista o arquivo IntPos.001 no destino C:\\")

        iCFAbrir_ECF_Daruma("111.111.111.11","Daruma Developers Community","Avenida Shishima Hifumi,2910")

        for i in range(0, 50):
            iCFVender_ECF_Daruma("F1","1,00","1,00","D$","0,00","12345678901234","UN","ITE.")

        iCFTotalizarCupom_ECF_Daruma("A%","10,00")
        iCFEfetuarPagamento_ECF_Daruma("CARTÃO","10,00","Pagamento Efetuado")
        iCFEncerrar_ECF_Daruma("0","Mensagem Promocional com até 8 linhas")

        QMessageBox.information(self, "DarumaFramework - Python/Qt","Vou travar o teclado ate encontrar o arquivo! Caminho do Arquivo: C:\\IntPos.001")
        iRetorno = iTEF_ImprimirResposta_ECF_Daruma("C:\IntPos.001", True, "CARTAO","10,00")
        if (iRetorno == 0):
            QMessageBox.information(self, "DarumaFramework - Python/Qt","Erro na Leitura do Arquivo IntPos.001")

        tratarRetornoFiscal(iTEF_Fechar_ECF_Daruma(), self)

    def on_actionM_todo_eTEF_EsperarArquivo_ECF_Daruma_triggered(self):
        self.form_FISCAL_eTEF_EsperarArquivo = Ui_ui_FISCAL_eTEF_EsperarArquivo()
        self.form_FISCAL_eTEF_EsperarArquivo.show()

    def on_actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma_triggered(self):
        self.form_FISCAL_iTEF_ImprimirRespostaCartao = Ui_ui_FISCAL_iTEF_ImprimirRespostaCartao()
        self.form_FISCAL_iTEF_ImprimirRespostaCartao.show()

    def on_actionM_todo_iTEF_ImprimirResposta_ECF_Daruma_triggered(self):
        self.form_FISCAL_iTEF_ImprimirResposta = Ui_ui_FISCAL_iTEF_ImprimirResposta()
        self.form_FISCAL_iTEF_ImprimirResposta.show()

    def on_actionM_todo_eTEF_TravarTeclado_ECF_Daruma_triggered(self):
        self.form_FISCAL_eTEF_TravarTeclado = Ui_ui_FISCAL_eTEF_TravarTeclado()
        self.form_FISCAL_eTEF_TravarTeclado.show()

    def on_actionM_todo_iTEF_Fechar_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iTEF_Fechar_ECF_Daruma(), self)

    def on_actionM_todo_eTEF_SetarFoco_ECF_Daruma_triggered(self):
        self.form_FISCAL_eTEF_SetarFoco = Ui_ui_FISCAL_eTEF_SetarFoco()
        self.form_FISCAL_eTEF_SetarFoco.show()
    # FIM
    # CCD / COMPROVANTE DÉBIDO CRÉDITO - TEF

    # COMPROVANTE NÃO FISCAL
    # INICIO

    def on_actionM_todo_iCNFAbrir_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFAbrir = Ui_ui_FISCAL_iCNFAbrir()
        self.form_FISCAL_iCNFAbrir.show()

    def on_actionM_todo_iCNFAbrirPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE
        tratarRetornoFiscal(iCNFAbrirPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCNFReceber_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFReceber = Ui_ui_FISCAL_iCNFReceber()
        self.form_FISCAL_iCNFReceber.show()

    def on_actionM_todo_iCNFReceberSemDesc_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFReceberSemDesc = Ui_ui_FISCAL_iCNFReceberSemDesc()
        self.form_FISCAL_iCNFReceberSemDesc.show()

    def on_actionM_todo_iCNFCancelarItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFCancelarItem = Ui_ui_FISCAL_iCNFCancelarItem()
        self.form_FISCAL_iCNFCancelarItem.show()

    def on_actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFCancelarUltimoItem_ECF_Daruma(), self)

    def on_actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFCancelarAcrescimoItem = Ui_ui_FISCAL_iCNFCancelarAcrescimoItem()
        self.form_FISCAL_iCNFCancelarAcrescimoItem.show()

    def on_actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFCancelarAcrescimoUltimoItem_ECF_Daruma(), self)

    def on_actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFCancelarDescontoItem = Ui_ui_FISCAL_iCNFCancelarDescontoItem()
        self.form_FISCAL_iCNFCancelarDescontoItem.show()

    def on_actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFCancelarDescontoUltimoItem_ECF_Daruma(), self)

    def on_actionM_todo_iCNFTotalizarComprovante_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFTotalizarComprovante = Ui_ui_FISCAL_iCNFTotalizarComprovante()
        self.form_FISCAL_iCNFTotalizarComprovante.show()

    def on_actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFTotalizarComprovantePadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFCancelarAcrescimoSubtotal_ECF_Daruma(), self)

    def on_actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFCancelarDescontoSubtotal_ECF_Daruma(), self)

    def on_actionM_todo_iCNFEfetuarPagamento_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFEfetuarPagamento = Ui_ui_FISCAL_iCNFEfetuarPagamento()
        self.form_FISCAL_iCNFEfetuarPagamento.show()

    def on_actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFEfetuarPagamentoFormatado = Ui_ui_FISCAL_iCNFEfetuarPagamentoFormatado()
        self.form_FISCAL_iCNFEfetuarPagamentoFormatado.show()

    def on_actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFEfetuarPagamentoPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCNFEncerrar_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCNFEncerrar = Ui_ui_FISCAL_iCNFEncerrar()
        self.form_FISCAL_iCNFEncerrar.show()

    def on_actionM_todo_iCNFEncerrarPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFEncerrarPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iCNFCancelar_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iCNFCancelar_ECF_Daruma(), self)

    def on_actionExemplo_CNF_Detalhado_triggered(self):

        QMessageBox.warning(self, "DarumaFramework - Python/Qt",("É necessário ter pelo menos um Totalizador Não Fiscal Cadastrado. Caso nao possua, o Comprovante sairá cancelado."))

        iretAbrir = iCNFAbrir_ECF_Daruma("111.111.111-11","Daruma Developers Community","Av Shishima Hifumi")
        iretReceber = iCNFReceber_ECF_Daruma("03","5,00","A%","10,00")
        iretTotalizar = iCNFTotalizarComprovante_ECF_Daruma("D%","10,00")
        iretPagamento = iCNFEfetuarPagamento_ECF_Daruma("Dinheiro","10,00","Efetuar Pagamento Com Mensagem")
        iretEncerrar = iCNFEncerrar_ECF_Daruma("Mensagem Promocional no Encerramento com até 8 linhas!")

        if((iretAbrir != 1) and (iretReceber != 1) and (iretTotalizar != 1) and (iretPagamento != 1) and (iretEncerrar != 1)):
            iCNFCancelar_ECF_Daruma()
            QMessageBox.warning(self, "DarumaFramework - Python/Qt","Ocorreu um Erro. O Cupom foi Cancelado")

    # FIM
    # COMPROVANTE NÃO FISCAL




    #/* ****** MÉTODOS PARA RELATORIO GERENCIAL ******* */
    # INICIO

    def on_actionM_todo_iRGAbrir_ECF_Daruma_triggered(self):
        self.form_FISCAL_iRGAbrir = Ui_ui_FISCAL_iRGAbrir()
        self.form_FISCAL_iRGAbrir.show()

    def on_actionM_todo_iRGAbrirIndice_ECF_Daruma_triggered(self):
        self.form_FISCAL_iRGAbrirIndice = Ui_ui_FISCAL_iRGAbrirIndice()
        self.form_FISCAL_iRGAbrirIndice.show()

    def on_actionM_todo_iRGAbrirPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iRGAbrirPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iRGImprimirTexto_ECF_Daruma_triggered(self):
        self.form_FISCAL_iRGImprimirTexto = Ui_ui_FISCAL_iRGImprimirTexto()
        self.form_FISCAL_iRGImprimirTexto.show()
    def on_actionM_todo_iRGFechar_ECF_Daruma_triggered(self):
        tratarRetornoFiscal(iRGFechar_ECF_Daruma(), self)

    # FIM
    # MÉTODOS PARA RELATORIO GERENCIAL




    #/* ****** RELATÓRIOS FISCAIS ******* */
    # INICIO

    def on_actionM_todo_iLeituraX_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iLeituraX_ECF_Daruma(), self)

    def on_actionM_todo_rLeituraX_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(rLeituraX_ECF_Daruma(), self)

    def on_actionM_todo_rLeituraXCustomizada_ECF_Daruma_triggered(self):
        self.form_FISCAL_rLeituraXCustomizada = Ui_ui_FISCAL_rLeituraXCustomizada()
        self.form_FISCAL_rLeituraXCustomizada.show()

    def on_actionM_todo_iReducaoZ_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iReducaoZ_ECF_Daruma("",""), self)

    def on_actionM_todo_iSangria_ECF_Daruma_triggered(self):
        self.form_FISCAL_iSangria = Ui_ui_FISCAL_iSangria()
        self.form_FISCAL_iSangria.show()

    def on_actionM_todo_iSangriaPadrao_ECF_Daruma_triggered(self):
        tratarRetornoFiscal(iSangriaPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iSuprimento_ECF_Daruma_triggered(self):
        self.form_FISCAL_iSuprimento = Ui_ui_FISCAL_iSuprimento()
        self.form_FISCAL_iSuprimento.show()

    def on_actionM_todo_iSuprimentoPadrao_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(iSuprimentoPadrao_ECF_Daruma(), self)

    def on_actionM_todo_iMFLer_ECF_Daruma_triggered(self):
        self.form_FISCAL_iMFLer = Ui_ui_FISCAL_iMFLer()
        self.form_FISCAL_iMFLer.show()

    def on_actionM_todo_iMFLerSerial_ECF_Daruma_triggered(self):
        self.form_FISCAL_iMFLerSerial = Ui_ui_FISCAL_iMFLerSerial()
        self.form_FISCAL_iMFLerSerial.show()

    # FIM
    #/* ****** RELATÓRIOS FISCAIS ******* */




    #/* ****** CONFIGURAÇAO DO ECF ******* */
    # INICIO

    def on_actionM_todo_confCadastrar_ECF_Daruma_triggered(self):
        self.form_FISCAL_confCadastrar = Ui_ui_FISCAL_confCadastrar()
        self.form_FISCAL_confCadastrar.show()

    def on_actionM_todo_confCadastrarPadrao_ECF_Daruma_triggered(self):
        self.form_FISCAL_confCadastrarPadrao = Ui_ui_FISCAL_confCadastrarPadrao()
        self.form_FISCAL_confCadastrarPadrao.show()

    def on_actionLoja_triggered(self):
        self.form_FISCAL_confProgramarIDLoja = Ui_ui_FISCAL_confProgramarIDLoja()
        self.form_FISCAL_confProgramarIDLoja.show()

    def on_actionHabilitarHVerao_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(confHabilitarHorarioVerao_ECF_Daruma(), self)

    def on_actionDesabilitarHVerao_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(confDesabilitarHorarioVerao_ECF_Daruma(), self)

    def on_actionHabilitarMPreVenda_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(confHabilitarModoPreVenda_ECF_Daruma(), self)

    def on_actionDesabilitarMPreVenda_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(confDesabilitarModoPreVenda_ECF_Daruma(), self)

    def on_menuModo_Pr_Venda_triggered(self):
        #//AVISO PARA PRÉ VENDA
        QMessageBox.information(self, "DarumaFramework - Python/Qt","Importante: A Configuraçao de Modo Pré-Venda é funcional apenas nas impressoras MACH1 e MACH2. Caso seu ECF seja diferente destes dois modelos, a configuração não terá efeito.")

    def on_actionAvan_o_de_Papel_triggered(self):
        self.form_FISCAL_confProgramarAvancoPapel = Ui_ui_FISCAL_confProgramarAvancoPapel()
        self.form_FISCAL_confProgramarAvancoPapel.show()

    def on_actionConfOperador_triggered(self):
        self.form_FISCAL_confProgramarOperador = Ui_ui_FISCAL_confProgramarOperador()
        self.form_FISCAL_confProgramarOperador.show()


    # FIM
    #/* ****** CONFIGURAÇAO DO ECF ******* */




    #/* ****** RETORNOS E STATUS DO ECF ******* */
    # INICIO

    def on_actionM_todos_para_Retornos_e_Status_triggered(self):
        self.form_FISCAL_RetornosStatusECF = Ui_ui_FISCAL_RetornosStatusECF()
        self.form_FISCAL_RetornosStatusECF.show()

    # FIM
    #/* ****** RETORNOS E STATUS DO ECF ******* */


    #/* ****** BILHETE DE PASSAGEM ******* */
    # INICIO
    def on_actionM_todo_iCFBPAbrir_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFBPAbrir = Ui_ui_FISCAL_iCFBPAbrir()
        self.form_FISCAL_iCFBPAbrir.show()

    def on_actionM_todo_iCFBPVender_ECF_Daruma_triggered(self):
        self.form_FISCAL_iCFBPVender = Ui_ui_FISCAL_iCFBPVender()
        self.form_FISCAL_iCFBPVender.show()

    def on_actionM_todo_confCFBPProgramarUF_ECF_Daruma_triggered(self):
        self.form_FISCAL_confCFBPProgramarUF = Ui_ui_FISCAL_confCFBPProgramarUF()
        self.form_FISCAL_confCFBPProgramarUF.show()
    # FIM
    #/* ****** BILHETE DE PASSAGEM ******* */


    #/* ****** ESPECIAIS ******* */
    # INICIO

    def on_actionM_todo_eAcionarGuilhotina_ECF_Daruma_triggered(self):
        self.form_FISCAL_eAcionarGuilhotina = Ui_ui_FISCAL_eAcionarGuilhotina()
        self.form_FISCAL_eAcionarGuilhotina.show()

    def on_actionM_todo_eAbrirGaveta_ECF_Daruma_triggered(self):
        # MÉTODO SEM PARAMETROS, PODE SER CHAMADO DIRETAMENTE.
        tratarRetornoFiscal(eAbrirGaveta_ECF_Daruma(), self)

    def on_actionM_todo_rStatusGaveta_ECF_Daruma_triggered(self):

        iStatus = None
        tratarRetornoFiscal(rStatusGaveta_ECF_Daruma(iStatus), self)

        if (iStatus == 0):
            QMessageBox.information(self, "DarumaFramework - Python/Qt", "Gaveta Fechada")
        if (iStatus == 1):
            QMessageBox.information(self, "DarumaFramework - Python/Qt", "Gaveta aberta")

    def on_actionM_todo_eCarregarBitmapPromocional_ECF_Daruma_triggered(self):
        self.form_FISCAL_eCarregarBitmapPromocional = Ui_ui_FISCAL_eCarregarBitmapPromocional()
        self.form_FISCAL_eCarregarBitmapPromocional.show()

    def on_actionM_todo_iImprimirCodigoBarras_ECF_Daruma_triggered(self):
        self.form_FISCAL_iImprimirCodigoBarras = Ui_ui_FISCAL_iImprimirCodigoBarras()
        self.form_FISCAL_iImprimirCodigoBarras.show()

    def on_actionM_todo_regRetornaValorChave_DarumaFramework_triggered(self):
        self.form_FISCAL_regRetornaValorChave = Ui_ui_FISCAL_regRetornaValorChave()
        self.form_FISCAL_regRetornaValorChave.show()

    def on_actionM_todo_regAlterarValor_Daruma_triggered(self):
        self.form_FISCAL_regAlterarValor = Ui_ui_FISCAL_regAlterarValor()
        self.form_FISCAL_regAlterarValor.show()

    def on_actionM_todo_eDefinirProduto_Daruma_triggered(self):
        self.form_FISCAL_eDefinirProduto = Ui_ui_FISCAL_eDefinirProduto()
        self.form_FISCAL_eDefinirProduto.show()

    def on_actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma_triggered(self):
        self.form_FISCAL_regCFCupomAdicionalDllConfig = Ui_ui_FISCAL_regCFCupomAdicionalDllConfig()
        self.form_FISCAL_regCFCupomAdicionalDllConfig.show()

    def on_actionM_todo_eDefinirModoRegistro_Daruma_triggered(self):
        self.form_FISCAL_eDefinirModoRegistro = Ui_ui_FISCAL_eDefinirModoRegistro()
        self.form_FISCAL_eDefinirModoRegistro.show()
    # FIM
    #/* ****** ESPECIAIS ******* */

    #/* ****** CHEQUE ******* */
    # INICIO

    def on_actionM_todo_iChequeImprimir_FS2100_Daruma_triggered(self):
        self.form_FISCAL_iChequeImprimir = Ui_ui_FISCAL_iChequeImprimir()
        self.form_FISCAL_iChequeImprimir.show()

    # FIM
    #/* ****** CHEQUE ******* */

    #/* ****** GERAÇAO DE ARQUIVO ******* */
    # INICIO
    def on_actionRGerarEspelhoMFD_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarEspelhoMFD = Ui_ui_FISCAL_rGerarEspelhoMFD()
        self.form_FISCAL_rGerarEspelhoMFD.show()

    def on_actionM_todo_rGerarRelatorio_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarRelatorio = Ui_ui_FISCAL_rGerarRelatorio()
        self.form_FISCAL_rGerarRelatorio.show()

    def on_actionM_todo_rGerarRelatorioOffline_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarRelatorioOffline = Ui_ui_FISCAL_rGerarRelatorioOffline()
        self.form_FISCAL_rGerarRelatorioOffline.show()

    def on_actionM_todo_rGerarMF_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarMF = Ui_ui_FISCAL_rGerarMF()
        self.form_FISCAL_rGerarMF.show()

    def on_actionM_todo_rGerarMFD_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarMFD = Ui_ui_FISCAL_rGerarMFD()
        self.form_FISCAL_rGerarMFD.show()

    def on_actionM_todo_rGerarTDM_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarTDM = Ui_ui_FISCAL_rGerarTDM()
        self.form_FISCAL_rGerarTDM.show()

    def on_actionM_todo_rGerarSPED_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarSPED = Ui_ui_FISCAL_rGerarSPED()
        self.form_FISCAL_rGerarSPED.show()

    def on_actionM_todo_rGerarSINTEGRA_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarSINTEGRA = Ui_ui_FISCAL_rGerarSINTEGRA()
        self.form_FISCAL_rGerarSINTEGRA.show()

    def on_actionM_todo_rGerarNFP_ECF_Daruma_triggered(self):
        self.form_FISCAL_rGerarNFP = Ui_ui_FISCAL_rGerarNFP()
        self.form_FISCAL_rGerarNFP.show()
    # FIM
    #/* ****** GERAÇAO DE ARQUIVO ******* */

    #/* ****** PAF-ECF ******* */
    # INICIO
    def on_actionM_todo_rCalcularMD5_ECF_Daruma_triggered(self):
        self.form_FISCAL_rCalcularMD5 = Ui_ui_FISCAL_rCalcularMD5()
        self.form_FISCAL_rCalcularMD5.show()

    def on_actionM_todo_rRetornarGTCodificado_ECF_Daruma_triggered(self):
        self.form_FISCAL_rRetornarGTCodificado = Ui_ui_FISCAL_rRetornarGTCodificado()
        self.form_FISCAL_rRetornarGTCodificado.show()

    def on_actionM_todo_rVerificarGTCodificado_ECF_Daruma_triggered(self):
        self.form_FISCAL_rVerificarGTCodificado = Ui_ui_FISCAL_rVerificarGTCodificado()
        self.form_FISCAL_rVerificarGTCodificado.show()

    def on_actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma_triggered(self):
        self.form_FISCAL_rRetornarNumeroSerieCodificado = Ui_ui_FISCAL_rRetornarNumeroSerieCodificado()
        self.form_FISCAL_rRetornarNumeroSerieCodificado.show()

    def on_actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma_triggered(self):
        self.form_FISCAL_rVerificarNumeroSerieCodificado = Ui_ui_FISCAL_rVerificarNumeroSerieCodificado()
        self.form_FISCAL_rVerificarNumeroSerieCodificado.show()

    def on_actionM_todo_rCodigoModeloFiscal_ECF_Daruma_triggered(self):
        self.form_FISCAL_rCodigoModeloFiscal = Ui_ui_FISCAL_rCodigoModeloFiscal()
        self.form_FISCAL_rCodigoModeloFiscal.show()

    def on_actionM_todo_eRSAAssinarArquivo_ECF_Daruma_triggered(self):
        self.form_FISCAL_eRSAAssinarArquivo = Ui_ui_FISCAL_eRSAAssinarArquivo()
        self.form_FISCAL_eRSAAssinarArquivo.show()

    def on_actionM_todo_rRSAChavePublica_ECF_Daruma_triggered(self):
        self.form_FISCAL_rRSAChavePublica = Ui_ui_FISCAL_rRSAChavePublica()
        self.form_FISCAL_rRSAChavePublica.show()
    # FIM
    #/* ****** PAF-ECF ******* */

    #/* ****** MENU FISCAL ******* */
    # INICIO
    def on_actionM_todo_eMemoriaFiscal_ECF_Daruma_triggered(self):
        self.form_FISCAL_eMemoriaFiscal = Ui_ui_FISCAL_eMemoriaFiscal()
        self.form_FISCAL_eMemoriaFiscal.show()

    def on_action_MenuFiscal_LX_triggered(self):
        tratarRetornoFiscal(iLeituraX_ECF_Daruma(), self)

    def on_action_MenuFiscal_LMFC_triggered(self):
        self.form_FISCAL_MenuFiscal_LMFC = Ui_ui_FISCAL_MenuFiscal_LMFC()
        self.form_FISCAL_MenuFiscal_LMFC.show()

    def on_action_MenuFiscal_LMFS_triggered(self):
        self.form_FISCAL_MenuFiscal_LMFS = Ui_ui_FISCAL_MenuFiscal_LMFS()
        self.form_FISCAL_MenuFiscal_LMFS.show()

    def on_action_MenuFiscal_Arq_MFD_triggered(self):
        self.form_FISCAL_MenuFiscal_ArqMFD = Ui_ui_FISCAL_MenuFiscal_ArqMFD()
        self.form_FISCAL_MenuFiscal_ArqMFD.show()

    def on_action_MenuFiscal_Espelho_MFD_triggered(self):
        self.form_FISCAL_rGerarEspelhoMFD = Ui_ui_FISCAL_rGerarEspelhoMFD()
        self.form_FISCAL_rGerarEspelhoMFD.show()

    def on_action_MenuFiscal_Tab_Produto_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Estoque_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Movimento_por_ECF_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Meios_de_Pgto_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Vendas_por_Per_odo_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Identifica_ao_do_PAF_ECF_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_DAV_Emitidos_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Encerrantes_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Transf_Mesas_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Manifesto_Fiscal_de_Viagem_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Cupom_de_Embarque_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Cupons_de_Embarque_Gratuidade_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Ped_gios_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()

    def on_action_MenuFiscal_Manuten_ao_de_Bombas_triggered(self):
        self.form_FISCAL_MenuFiscal = Ui_ui_FISCAL_MenuFiscal()
        self.form_FISCAL_MenuFiscal.show()
    # FIM
    #/* ****** MENU FISCAL ******* */

    def on_pushButtonEncerrar_clicked(self):
        self.close()

    def on_pushButtonContatos_clicked(self):
        self.form_Geral_ContatosSuporte = Ui_ui_Geral_ContatosSuporte()
        self.form_Geral_ContatosSuporte.show()

    def setupUi(self, MainWindowFISCAL):
        MainWindowFISCAL.setObjectName("MainWindowFISCAL")
        MainWindowFISCAL.resize(1037, 423)
        MainWindowFISCAL.setMinimumSize(QtCore.QSize(772, 423))
        MainWindowFISCAL.setAcceptDrops(False)
        MainWindowFISCAL.setToolTip("")
        self.centralwidget = QtGui.QWidget(MainWindowFISCAL)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 164, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 167))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(195, 89))
        self.label_2.setMaximumSize(QtCore.QSize(195, 89))
        self.label_2.setStyleSheet("background-image: url(:/Recursos/Imagens/logo_daruma_developers.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonContatos = QtGui.QPushButton(self.frame)
        self.pushButtonContatos.setMinimumSize(QtCore.QSize(191, 101))
        self.pushButtonContatos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonContatos.setStyleSheet("background-image: url(:/Recursos/Imagens/avatar.png);")
        self.pushButtonContatos.setText("")
        self.pushButtonContatos.setObjectName("pushButtonContatos")
        self.horizontalLayout.addWidget(self.pushButtonContatos)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButtonEncerrar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEncerrar.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButtonEncerrar.setObjectName("pushButtonEncerrar")
        self.horizontalLayout_2.addWidget(self.pushButtonEncerrar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindowFISCAL.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowFISCAL)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 18))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.menubar.setFont(font)
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setObjectName("menubar")
        self.menuCupom_Fiscal = QtGui.QMenu(self.menubar)
        self.menuCupom_Fiscal.setObjectName("menuCupom_Fiscal")
        self.menuAbertura_de_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuAbertura_de_Cupom_Fiscal.setObjectName("menuAbertura_de_Cupom_Fiscal")
        self.menuRegistro_de_Item = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuRegistro_de_Item.setObjectName("menuRegistro_de_Item")
        self.menuDesconto_ou_Acr_scimo_em_Item = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuDesconto_ou_Acr_scimo_em_Item.setObjectName("menuDesconto_ou_Acr_scimo_em_Item")
        self.menuCancelamento_Total_de_Item_em_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCancelamento_Total_de_Item_em_Cupom_Fiscal.setObjectName("menuCancelamento_Total_de_Item_em_Cupom_Fiscal")
        self.menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal.setObjectName("menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal")
        self.menuCancelamento_de_Desconto_em_Item = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCancelamento_de_Desconto_em_Item.setObjectName("menuCancelamento_de_Desconto_em_Item")
        self.menuCancelamento_de_Acr_scimo_em_Item = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCancelamento_de_Acr_scimo_em_Item.setObjectName("menuCancelamento_de_Acr_scimo_em_Item")
        self.menuTotaliza_o_do_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuTotaliza_o_do_Cupom_Fiscal.setObjectName("menuTotaliza_o_do_Cupom_Fiscal")
        self.menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF.setObjectName("menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF")
        self.menuDescri_o_da_Forma_de_Pagamento = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuDescri_o_da_Forma_de_Pagamento.setObjectName("menuDescri_o_da_Forma_de_Pagamento")
        self.menuEncerramento_de_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuEncerramento_de_Cupom_Fiscal.setObjectName("menuEncerramento_de_Cupom_Fiscal")
        self.menuCancelamento_de_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCancelamento_de_Cupom_Fiscal.setObjectName("menuCancelamento_de_Cupom_Fiscal")
        self.menuIdentificac_o_de_Consumidor_no_Rodap_do_Cupom_Fiscal = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuIdentificac_o_de_Consumidor_no_Rodap_do_Cupom_Fiscal.setObjectName("menuIdentificac_o_de_Consumidor_no_Rodap_do_Cupom_Fiscal")
        self.menuCupom_Mania_para_Estado_do_RJ = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuCupom_Mania_para_Estado_do_RJ.setObjectName("menuCupom_Mania_para_Estado_do_RJ")
        self.menuEstorno_Meio_de_Pagamento = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuEstorno_Meio_de_Pagamento.setObjectName("menuEstorno_Meio_de_Pagamento")
        self.menuExemplos = QtGui.QMenu(self.menuCupom_Fiscal)
        self.menuExemplos.setObjectName("menuExemplos")
        self.menuRelat_rios_Fiscais = QtGui.QMenu(self.menubar)
        self.menuRelat_rios_Fiscais.setObjectName("menuRelat_rios_Fiscais")
        self.menuLeitura_X = QtGui.QMenu(self.menuRelat_rios_Fiscais)
        self.menuLeitura_X.setObjectName("menuLeitura_X")
        self.menuRedu_ao_Z = QtGui.QMenu(self.menuRelat_rios_Fiscais)
        self.menuRedu_ao_Z.setObjectName("menuRedu_ao_Z")
        self.menuSangria = QtGui.QMenu(self.menuRelat_rios_Fiscais)
        self.menuSangria.setObjectName("menuSangria")
        self.menuSuprimento = QtGui.QMenu(self.menuRelat_rios_Fiscais)
        self.menuSuprimento.setObjectName("menuSuprimento")
        self.menuLeitura_da_Mem_ria_Fiscal = QtGui.QMenu(self.menuRelat_rios_Fiscais)
        self.menuLeitura_da_Mem_ria_Fiscal.setObjectName("menuLeitura_da_Mem_ria_Fiscal")
        self.menuCCD_TEF = QtGui.QMenu(self.menubar)
        self.menuCCD_TEF.setObjectName("menuCCD_TEF")
        self.menuAbertura_de_CCD = QtGui.QMenu(self.menuCCD_TEF)
        self.menuAbertura_de_CCD.setObjectName("menuAbertura_de_CCD")
        self.menuImpress_o_de_Texto = QtGui.QMenu(self.menuCCD_TEF)
        self.menuImpress_o_de_Texto.setObjectName("menuImpress_o_de_Texto")
        self.menuEncerramento_de_CCD = QtGui.QMenu(self.menuCCD_TEF)
        self.menuEncerramento_de_CCD.setObjectName("menuEncerramento_de_CCD")
        self.menuEstorno_de_CCD = QtGui.QMenu(self.menuCCD_TEF)
        self.menuEstorno_de_CCD.setObjectName("menuEstorno_de_CCD")
        self.menuTEF = QtGui.QMenu(self.menuCCD_TEF)
        self.menuTEF.setEnabled(True)
        self.menuTEF.setObjectName("menuTEF")
        self.menuComprovante_N_o_Fiscal = QtGui.QMenu(self.menubar)
        self.menuComprovante_N_o_Fiscal.setObjectName("menuComprovante_N_o_Fiscal")
        self.menuAbertura_de_Comprovante_N_o_Fiscal = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuAbertura_de_Comprovante_N_o_Fiscal.setObjectName("menuAbertura_de_Comprovante_N_o_Fiscal")
        self.menuRecebimento_de_Itens = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuRecebimento_de_Itens.setObjectName("menuRecebimento_de_Itens")
        self.menuCancelamento_de_Item = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuCancelamento_de_Item.setObjectName("menuCancelamento_de_Item")
        self.menuCancelamento_de_Acr_scimo_em_Item_2 = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuCancelamento_de_Acr_scimo_em_Item_2.setObjectName("menuCancelamento_de_Acr_scimo_em_Item_2")
        self.menuCancelamento_de_Desconto_em_Item_2 = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuCancelamento_de_Desconto_em_Item_2.setObjectName("menuCancelamento_de_Desconto_em_Item_2")
        self.menuTotaliza_ao_de_CNF = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuTotaliza_ao_de_CNF.setObjectName("menuTotaliza_ao_de_CNF")
        self.menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF.setObjectName("menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF")
        self.menuEncerramento_de_CNF = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuEncerramento_de_CNF.setObjectName("menuEncerramento_de_CNF")
        self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF.setObjectName("menuDescri_ao_dos_Meios_de_Pagamento_de_CNF")
        self.menuCancelamento_de_CNF = QtGui.QMenu(self.menuComprovante_N_o_Fiscal)
        self.menuCancelamento_de_CNF.setObjectName("menuCancelamento_de_CNF")
        self.menuRelat_rio_Gerencial = QtGui.QMenu(self.menubar)
        self.menuRelat_rio_Gerencial.setObjectName("menuRelat_rio_Gerencial")
        self.menuAbertura_de_Relat_rio_Gerencial = QtGui.QMenu(self.menuRelat_rio_Gerencial)
        self.menuAbertura_de_Relat_rio_Gerencial.setTearOffEnabled(False)
        self.menuAbertura_de_Relat_rio_Gerencial.setObjectName("menuAbertura_de_Relat_rio_Gerencial")
        self.menuTexto_para_Impress_o = QtGui.QMenu(self.menuRelat_rio_Gerencial)
        self.menuTexto_para_Impress_o.setObjectName("menuTexto_para_Impress_o")
        self.menuEncerramento_do_Relat_rio_Gerencial = QtGui.QMenu(self.menuRelat_rio_Gerencial)
        self.menuEncerramento_do_Relat_rio_Gerencial.setObjectName("menuEncerramento_do_Relat_rio_Gerencial")
        self.menuPrograma_o_do_ECF = QtGui.QMenu(self.menubar)
        self.menuPrograma_o_do_ECF.setObjectName("menuPrograma_o_do_ECF")
        self.menuECF = QtGui.QMenu(self.menuPrograma_o_do_ECF)
        self.menuECF.setObjectName("menuECF")
        self.menuEspeciais = QtGui.QMenu(self.menuPrograma_o_do_ECF)
        self.menuEspeciais.setObjectName("menuEspeciais")
        self.menuHor_rio_de_Ver_o = QtGui.QMenu(self.menuPrograma_o_do_ECF)
        self.menuHor_rio_de_Ver_o.setObjectName("menuHor_rio_de_Ver_o")
        self.menuModo_Pr_Venda = QtGui.QMenu(self.menuPrograma_o_do_ECF)
        self.menuModo_Pr_Venda.setObjectName("menuModo_Pr_Venda")
        self.menuRetornos_e_Status_do_ECF = QtGui.QMenu(self.menubar)
        self.menuRetornos_e_Status_do_ECF.setObjectName("menuRetornos_e_Status_do_ECF")
        self.menuBilhete_de_Passagem = QtGui.QMenu(self.menubar)
        self.menuBilhete_de_Passagem.setObjectName("menuBilhete_de_Passagem")
        self.menuGaveta_Autentica_e_Outros = QtGui.QMenu(self.menubar)
        self.menuGaveta_Autentica_e_Outros.setObjectName("menuGaveta_Autentica_e_Outros")
        self.menuCheque = QtGui.QMenu(self.menubar)
        self.menuCheque.setObjectName("menuCheque")
        self.menuC_digo_de_Barras = QtGui.QMenu(self.menubar)
        self.menuC_digo_de_Barras.setObjectName("menuC_digo_de_Barras")
        self.menuRegistry = QtGui.QMenu(self.menubar)
        self.menuRegistry.setObjectName("menuRegistry")
        self.menuGera_ao_de_Arquivos = QtGui.QMenu(self.menubar)
        self.menuGera_ao_de_Arquivos.setObjectName("menuGera_ao_de_Arquivos")
        self.menuPAF_ECF = QtGui.QMenu(self.menubar)
        self.menuPAF_ECF.setObjectName("menuPAF_ECF")
        self.menuMenu_Fiscal = QtGui.QMenu(self.menubar)
        self.menuMenu_Fiscal.setObjectName("menuMenu_Fiscal")
        MainWindowFISCAL.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowFISCAL)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindowFISCAL.setStatusBar(self.statusbar)
        self.actionM_todo_iLeituraX_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iLeituraX_ECF_Daruma.setObjectName("actionM_todo_iLeituraX_ECF_Daruma")
        self.actionM_todo_rLeituraX_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rLeituraX_ECF_Daruma.setObjectName("actionM_todo_rLeituraX_ECF_Daruma")
        self.actionM_todo_iCFAbrir_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFAbrir_ECF_Daruma.setObjectName("actionM_todo_iCFAbrir_ECF_Daruma")
        self.actionM_todo_iCFAbrirPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFAbrirPadrao_ECF_Daruma.setObjectName("actionM_todo_iCFAbrirPadrao_ECF_Daruma")
        self.actionM_todo_iCFVender_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFVender_ECF_Daruma.setObjectName("actionM_todo_iCFVender_ECF_Daruma")
        self.actionM_todo_iCFVenderSemDesc_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFVenderSemDesc_ECF_Daruma.setObjectName("actionM_todo_iCFVenderSemDesc_ECF_Daruma")
        self.actionM_todo_iCFVenderResumido_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFVenderResumido_ECF_Daruma.setObjectName("actionM_todo_iCFVenderResumido_ECF_Daruma")
        self.actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma")
        self.actionM_todo_iCFLancarDescontoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFLancarDescontoItem_ECF_Daruma.setObjectName("actionM_todo_iCFLancarDescontoItem_ECF_Daruma")
        self.actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma")
        self.actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma")
        self.actionM_todo_iCFCancelarItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarItem_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarItem_ECF_Daruma")
        self.actionM_todo_iCFCancelarUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarUltimoItem_ECF_Daruma")
        self.actionM_todo_iCFCancelarItemParcial_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarItemParcial_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarItemParcial_ECF_Daruma")
        self.actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma")
        self.actionM_todo_iCFCancelarDescontoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarDescontoItem_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarDescontoItem_ECF_Daruma")
        self.actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma")
        self.actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma")
        self.actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma")
        self.actionM_todo_iCFTotalizarCupom_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFTotalizarCupom_ECF_Daruma.setObjectName("actionM_todo_iCFTotalizarCupom_ECF_Daruma")
        self.actionM_todo_iCFTotalizarPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFTotalizarPadrao_ECF_Daruma.setObjectName("actionM_todo_iCFTotalizarPadrao_ECF_Daruma")
        self.actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma")
        self.actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma.setObjectName("actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma")
        self.actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma.setObjectName("actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma")
        self.actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma.setObjectName("actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma")
        self.actionM_todo_iCFEfetuarPagamento_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEfetuarPagamento_ECF_Daruma.setObjectName("actionM_todo_iCFEfetuarPagamento_ECF_Daruma")
        self.actionM_todo_iCFEncerrarPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEncerrarPadrao_ECF_Daruma.setObjectName("actionM_todo_iCFEncerrarPadrao_ECF_Daruma")
        self.actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma.setObjectName("actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma")
        self.actionM_todo_iCFEncerrarResumido_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEncerrarResumido_ECF_Daruma.setObjectName("actionM_todo_iCFEncerrarResumido_ECF_Daruma")
        self.actionM_todo_iCFEncerrar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEncerrar_ECF_Daruma.setObjectName("actionM_todo_iCFEncerrar_ECF_Daruma")
        self.actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma.setObjectName("actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma")
        self.actionM_todo_iCFCancelar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFCancelar_ECF_Daruma.setObjectName("actionM_todo_iCFCancelar_ECF_Daruma")
        self.actionM_todo_iCFIdentificarConsumidor_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFIdentificarConsumidor_ECF_Daruma.setObjectName("actionM_todo_iCFIdentificarConsumidor_ECF_Daruma")
        self.actionConfigurac_o_Cupom_Mania = QtGui.QAction(MainWindowFISCAL)
        self.actionConfigurac_o_Cupom_Mania.setObjectName("actionConfigurac_o_Cupom_Mania")
        self.actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania = QtGui.QAction(MainWindowFISCAL)
        self.actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania.setObjectName("actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania")
        self.actionM_todo_iEstornarPagamento_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iEstornarPagamento_ECF_Daruma.setObjectName("actionM_todo_iEstornarPagamento_ECF_Daruma")
        self.actionTeste_de_Venda_de_Itens_Sem_Parar = QtGui.QAction(MainWindowFISCAL)
        self.actionTeste_de_Venda_de_Itens_Sem_Parar.setObjectName("actionTeste_de_Venda_de_Itens_Sem_Parar")
        self.actionCupom_Fiscal_Completo = QtGui.QAction(MainWindowFISCAL)
        self.actionCupom_Fiscal_Completo.setObjectName("actionCupom_Fiscal_Completo")
        self.actionCupom_Fiscal_Resumido = QtGui.QAction(MainWindowFISCAL)
        self.actionCupom_Fiscal_Resumido.setObjectName("actionCupom_Fiscal_Resumido")
        self.actionCupom_Fiscal_Pr_Venda = QtGui.QAction(MainWindowFISCAL)
        self.actionCupom_Fiscal_Pr_Venda.setObjectName("actionCupom_Fiscal_Pr_Venda")
        self.actionExemplo_CCD_Completo = QtGui.QAction(MainWindowFISCAL)
        self.actionExemplo_CCD_Completo.setCheckable(False)
        self.actionExemplo_CCD_Completo.setEnabled(True)
        self.actionExemplo_CCD_Completo.setObjectName("actionExemplo_CCD_Completo")
        self.actionM_todo_iCCDAbrir_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDAbrir_ECF_Daruma.setObjectName("actionM_todo_iCCDAbrir_ECF_Daruma")
        self.actionM_todo_iCCDAbrirPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDAbrirPadrao_ECF_Daruma.setObjectName("actionM_todo_iCCDAbrirPadrao_ECF_Daruma")
        self.actionM_todo_iCCDAbrirSimplificado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDAbrirSimplificado_ECF_Daruma.setObjectName("actionM_todo_iCCDAbrirSimplificado_ECF_Daruma")
        self.actionM_todo_iCCDImprimirTexto_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDImprimirTexto_ECF_Daruma.setObjectName("actionM_todo_iCCDImprimirTexto_ECF_Daruma")
        self.actionM_todo_iCCDImprimirArquivo_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDImprimirArquivo_ECF_Daruma.setObjectName("actionM_todo_iCCDImprimirArquivo_ECF_Daruma")
        self.actionM_todo_iCCDFechar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDFechar_ECF_Daruma.setObjectName("actionM_todo_iCCDFechar_ECF_Daruma")
        self.actionM_todo_iCCDEstornar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDEstornar_ECF_Daruma.setObjectName("actionM_todo_iCCDEstornar_ECF_Daruma")
        self.actionM_todo_iCCDEstornarPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCCDEstornarPadrao_ECF_Daruma.setObjectName("actionM_todo_iCCDEstornarPadrao_ECF_Daruma")
        self.action2_Via_de_CCD = QtGui.QAction(MainWindowFISCAL)
        self.action2_Via_de_CCD.setObjectName("action2_Via_de_CCD")
        self.actionM_todo_eTEF_EsperarArquivo_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eTEF_EsperarArquivo_ECF_Daruma.setObjectName("actionM_todo_eTEF_EsperarArquivo_ECF_Daruma")
        self.actionExemplo_CNF_Detalhado = QtGui.QAction(MainWindowFISCAL)
        self.actionExemplo_CNF_Detalhado.setObjectName("actionExemplo_CNF_Detalhado")
        self.actionM_todo_iCNFAbrir_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFAbrir_ECF_Daruma.setObjectName("actionM_todo_iCNFAbrir_ECF_Daruma")
        self.actionM_todo_iCNFAbrirPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFAbrirPadrao_ECF_Daruma.setObjectName("actionM_todo_iCNFAbrirPadrao_ECF_Daruma")
        self.actionM_todo_iCNFReceber_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFReceber_ECF_Daruma.setObjectName("actionM_todo_iCNFReceber_ECF_Daruma")
        self.actionM_todo_iCNFReceberSemDesc_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFReceberSemDesc_ECF_Daruma.setObjectName("actionM_todo_iCNFReceberSemDesc_ECF_Daruma")
        self.actionM_todo_iCNFCancelarItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarItem_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarItem_ECF_Daruma")
        self.actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma")
        self.actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma")
        self.actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma")
        self.actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma")
        self.actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma")
        self.actionM_todo_iCNFTotalizarComprovante_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFTotalizarComprovante_ECF_Daruma.setObjectName("actionM_todo_iCNFTotalizarComprovante_ECF_Daruma")
        self.actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma.setObjectName("actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma")
        self.actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma")
        self.actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma")
        self.actionM_todo_iCNFEfetuarPagamento_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFEfetuarPagamento_ECF_Daruma.setObjectName("actionM_todo_iCNFEfetuarPagamento_ECF_Daruma")
        self.actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma.setObjectName("actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma")
        self.actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma.setObjectName("actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma")
        self.actionM_todo_iCNFEncerrar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFEncerrar_ECF_Daruma.setObjectName("actionM_todo_iCNFEncerrar_ECF_Daruma")
        self.actionM_todo_iCNFEncerrarPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFEncerrarPadrao_ECF_Daruma.setObjectName("actionM_todo_iCNFEncerrarPadrao_ECF_Daruma")
        self.actionM_todo_iCNFCancelar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCNFCancelar_ECF_Daruma.setObjectName("actionM_todo_iCNFCancelar_ECF_Daruma")
        self.actionM_todo_iRGAbrir_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iRGAbrir_ECF_Daruma.setObjectName("actionM_todo_iRGAbrir_ECF_Daruma")
        self.actionM_todo_iRGAbrirIndice_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iRGAbrirIndice_ECF_Daruma.setObjectName("actionM_todo_iRGAbrirIndice_ECF_Daruma")
        self.actionM_todo_iRGAbrirPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iRGAbrirPadrao_ECF_Daruma.setObjectName("actionM_todo_iRGAbrirPadrao_ECF_Daruma")
        self.actionM_todo_iRGImprimirTexto_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iRGImprimirTexto_ECF_Daruma.setObjectName("actionM_todo_iRGImprimirTexto_ECF_Daruma")
        self.actionM_todo_iRGFechar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iRGFechar_ECF_Daruma.setObjectName("actionM_todo_iRGFechar_ECF_Daruma")
        self.actionM_todo_rLeituraXCustomizada_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rLeituraXCustomizada_ECF_Daruma.setObjectName("actionM_todo_rLeituraXCustomizada_ECF_Daruma")
        self.actionM_todo_iReducaoZ_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iReducaoZ_ECF_Daruma.setObjectName("actionM_todo_iReducaoZ_ECF_Daruma")
        self.actionM_todo_iSangria_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iSangria_ECF_Daruma.setObjectName("actionM_todo_iSangria_ECF_Daruma")
        self.actionM_todo_iSangriaPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iSangriaPadrao_ECF_Daruma.setObjectName("actionM_todo_iSangriaPadrao_ECF_Daruma")
        self.actionM_todo_iSuprimento_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iSuprimento_ECF_Daruma.setObjectName("actionM_todo_iSuprimento_ECF_Daruma")
        self.actionM_todo_iSuprimentoPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iSuprimentoPadrao_ECF_Daruma.setObjectName("actionM_todo_iSuprimentoPadrao_ECF_Daruma")
        self.actionM_todo_iMFLer_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iMFLer_ECF_Daruma.setObjectName("actionM_todo_iMFLer_ECF_Daruma")
        self.actionM_todo_iMFLerSerial_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iMFLerSerial_ECF_Daruma.setObjectName("actionM_todo_iMFLerSerial_ECF_Daruma")
        self.actionM_todo_confCadastrar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_confCadastrar_ECF_Daruma.setObjectName("actionM_todo_confCadastrar_ECF_Daruma")
        self.actionM_todo_confCadastrarPadrao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_confCadastrarPadrao_ECF_Daruma.setObjectName("actionM_todo_confCadastrarPadrao_ECF_Daruma")
        self.actionM_todo_eEnviarComando_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eEnviarComando_ECF_Daruma.setEnabled(False)
        self.actionM_todo_eEnviarComando_ECF_Daruma.setObjectName("actionM_todo_eEnviarComando_ECF_Daruma")
        self.actionHabilitarHVerao = QtGui.QAction(MainWindowFISCAL)
        self.actionHabilitarHVerao.setObjectName("actionHabilitarHVerao")
        self.actionDesabilitarHVerao = QtGui.QAction(MainWindowFISCAL)
        self.actionDesabilitarHVerao.setObjectName("actionDesabilitarHVerao")
        self.actionHabilitarMPreVenda = QtGui.QAction(MainWindowFISCAL)
        self.actionHabilitarMPreVenda.setObjectName("actionHabilitarMPreVenda")
        self.actionDesabilitarMPreVenda = QtGui.QAction(MainWindowFISCAL)
        self.actionDesabilitarMPreVenda.setObjectName("actionDesabilitarMPreVenda")
        self.actionAvan_o_de_Papel = QtGui.QAction(MainWindowFISCAL)
        self.actionAvan_o_de_Papel.setObjectName("actionAvan_o_de_Papel")
        self.actionLoja = QtGui.QAction(MainWindowFISCAL)
        self.actionLoja.setEnabled(True)
        self.actionLoja.setObjectName("actionLoja")
        self.actionConfOperador = QtGui.QAction(MainWindowFISCAL)
        self.actionConfOperador.setObjectName("actionConfOperador")
        self.actionM_todos_para_Retornos_e_Status = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todos_para_Retornos_e_Status.setObjectName("actionM_todos_para_Retornos_e_Status")
        self.actionM_todo_iCFBPAbrir_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFBPAbrir_ECF_Daruma.setObjectName("actionM_todo_iCFBPAbrir_ECF_Daruma")
        self.actionM_todo_iCFBPVender_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iCFBPVender_ECF_Daruma.setObjectName("actionM_todo_iCFBPVender_ECF_Daruma")
        self.actionM_todo_confCFBPProgramarUF_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_confCFBPProgramarUF_ECF_Daruma.setObjectName("actionM_todo_confCFBPProgramarUF_ECF_Daruma")
        self.actionM_todo_eAcionarGuilhotina_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eAcionarGuilhotina_ECF_Daruma.setObjectName("actionM_todo_eAcionarGuilhotina_ECF_Daruma")
        self.actionM_todo_eAbrirGaveta_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eAbrirGaveta_ECF_Daruma.setObjectName("actionM_todo_eAbrirGaveta_ECF_Daruma")
        self.actionM_todo_rStatusGaveta_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rStatusGaveta_ECF_Daruma.setObjectName("actionM_todo_rStatusGaveta_ECF_Daruma")
        self.actionM_todo_eCarregarBitmapPromocional_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eCarregarBitmapPromocional_ECF_Daruma.setObjectName("actionM_todo_eCarregarBitmapPromocional_ECF_Daruma")
        self.actionM_todo_iChequeImprimir_FS2100_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iChequeImprimir_FS2100_Daruma.setObjectName("actionM_todo_iChequeImprimir_FS2100_Daruma")
        self.actionM_todo_iImprimirCodigoBarras_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iImprimirCodigoBarras_ECF_Daruma.setObjectName("actionM_todo_iImprimirCodigoBarras_ECF_Daruma")
        self.actionregRetornaValorChave_DarumaFramework = QtGui.QAction(MainWindowFISCAL)
        self.actionregRetornaValorChave_DarumaFramework.setObjectName("actionregRetornaValorChave_DarumaFramework")
        self.actionM_todo_regAlterarValor_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_regAlterarValor_ECF_Daruma.setObjectName("actionM_todo_regAlterarValor_ECF_Daruma")
        self.actionRGerarEspelhoMFD_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionRGerarEspelhoMFD_ECF_Daruma.setObjectName("actionRGerarEspelhoMFD_ECF_Daruma")
        self.actionM_todo_regRetornaValorChave_DarumaFramework = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_regRetornaValorChave_DarumaFramework.setObjectName("actionM_todo_regRetornaValorChave_DarumaFramework")
        self.actionM_todo_regAlterarValor_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_regAlterarValor_Daruma.setObjectName("actionM_todo_regAlterarValor_Daruma")
        self.actionM_todo_rGerarRelatorio_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarRelatorio_ECF_Daruma.setObjectName("actionM_todo_rGerarRelatorio_ECF_Daruma")
        self.actionM_todo_rGerarRelatorioOffline_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarRelatorioOffline_ECF_Daruma.setObjectName("actionM_todo_rGerarRelatorioOffline_ECF_Daruma")
        self.actionM_todo_rGerarMF_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarMF_ECF_Daruma.setObjectName("actionM_todo_rGerarMF_ECF_Daruma")
        self.actionM_todo_rGerarMFD_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarMFD_ECF_Daruma.setObjectName("actionM_todo_rGerarMFD_ECF_Daruma")
        self.actionM_todo_rGerarTDM_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarTDM_ECF_Daruma.setObjectName("actionM_todo_rGerarTDM_ECF_Daruma")
        self.actionM_todo_eTEF_TravarTeclado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eTEF_TravarTeclado_ECF_Daruma.setObjectName("actionM_todo_eTEF_TravarTeclado_ECF_Daruma")
        self.actionM_todo_eTEF_SetarFoco_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eTEF_SetarFoco_ECF_Daruma.setObjectName("actionM_todo_eTEF_SetarFoco_ECF_Daruma")
        self.actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma.setObjectName("actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma")
        self.actionM_todo_iTEF_ImprimirResposta_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iTEF_ImprimirResposta_ECF_Daruma.setObjectName("actionM_todo_iTEF_ImprimirResposta_ECF_Daruma")
        self.actionM_todo_iTEF_Fechar_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_iTEF_Fechar_ECF_Daruma.setObjectName("actionM_todo_iTEF_Fechar_ECF_Daruma")
        self.actionExemplo_Completo_TEF = QtGui.QAction(MainWindowFISCAL)
        self.actionExemplo_Completo_TEF.setObjectName("actionExemplo_Completo_TEF")
        self.actionM_todo_eDefinirProduto_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eDefinirProduto_Daruma.setObjectName("actionM_todo_eDefinirProduto_Daruma")
        self.actionM_todo_eDefinirModoRegistro_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eDefinirModoRegistro_Daruma.setObjectName("actionM_todo_eDefinirModoRegistro_Daruma")
        self.actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma.setObjectName("actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma")
        self.actionM_todo_rCalcularMD5_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rCalcularMD5_ECF_Daruma.setObjectName("actionM_todo_rCalcularMD5_ECF_Daruma")
        self.actionM_todo_rRetornarGTCodificado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rRetornarGTCodificado_ECF_Daruma.setObjectName("actionM_todo_rRetornarGTCodificado_ECF_Daruma")
        self.actionM_todo_rVerificarGTCodificado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rVerificarGTCodificado_ECF_Daruma.setObjectName("actionM_todo_rVerificarGTCodificado_ECF_Daruma")
        self.actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma.setObjectName("actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma")
        self.actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma.setObjectName("actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma")
        self.actionM_todo_rCodigoModeloFiscal_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rCodigoModeloFiscal_ECF_Daruma.setObjectName("actionM_todo_rCodigoModeloFiscal_ECF_Daruma")
        self.actionM_todo_eRSAAssinarArquivo_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eRSAAssinarArquivo_ECF_Daruma.setObjectName("actionM_todo_eRSAAssinarArquivo_ECF_Daruma")
        self.actionM_todo_rRSAChavePublica_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rRSAChavePublica_ECF_Daruma.setObjectName("actionM_todo_rRSAChavePublica_ECF_Daruma")
        self.actionM_todo_eMemoriaFiscal_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_eMemoriaFiscal_ECF_Daruma.setObjectName("actionM_todo_eMemoriaFiscal_ECF_Daruma")
        self.action_MenuFiscal_LX = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_LX.setObjectName("action_MenuFiscal_LX")
        self.action_MenuFiscal_LMFC = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_LMFC.setObjectName("action_MenuFiscal_LMFC")
        self.action_MenuFiscal_LMFS = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_LMFS.setObjectName("action_MenuFiscal_LMFS")
        self.action_MenuFiscal_Espelho_MFD = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Espelho_MFD.setObjectName("action_MenuFiscal_Espelho_MFD")
        self.action_MenuFiscal_Arq_MFD = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Arq_MFD.setObjectName("action_MenuFiscal_Arq_MFD")
        self.action_MenuFiscal_Tab_Produto = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Tab_Produto.setObjectName("action_MenuFiscal_Tab_Produto")
        self.action_MenuFiscal_Estoque = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Estoque.setObjectName("action_MenuFiscal_Estoque")
        self.action_MenuFiscal_Movimento_por_ECF = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Movimento_por_ECF.setObjectName("action_MenuFiscal_Movimento_por_ECF")
        self.action_MenuFiscal_Meios_de_Pgto = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Meios_de_Pgto.setObjectName("action_MenuFiscal_Meios_de_Pgto")
        self.action_MenuFiscal_Vendas_por_Per_odo = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Vendas_por_Per_odo.setObjectName("action_MenuFiscal_Vendas_por_Per_odo")
        self.action_MenuFiscal_Identifica_ao_do_PAF_ECF = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Identifica_ao_do_PAF_ECF.setObjectName("action_MenuFiscal_Identifica_ao_do_PAF_ECF")
        self.action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o.setObjectName("action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o")
        self.action_MenuFiscal_DAV_Emitidos = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_DAV_Emitidos.setObjectName("action_MenuFiscal_DAV_Emitidos")
        self.action_MenuFiscal_Encerrantes = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Encerrantes.setObjectName("action_MenuFiscal_Encerrantes")
        self.action_MenuFiscal_Transf_Mesas = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Transf_Mesas.setObjectName("action_MenuFiscal_Transf_Mesas")
        self.action_MenuFiscal_Manifesto_Fiscal_de_Viagem = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Manifesto_Fiscal_de_Viagem.setObjectName("action_MenuFiscal_Manifesto_Fiscal_de_Viagem")
        self.action_MenuFiscal_Cupom_de_Embarque = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Cupom_de_Embarque.setObjectName("action_MenuFiscal_Cupom_de_Embarque")
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque.setObjectName("action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque")
        self.action_MenuFiscal_Cupons_de_Embarque_Gratuidade = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Cupons_de_Embarque_Gratuidade.setObjectName("action_MenuFiscal_Cupons_de_Embarque_Gratuidade")
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade.setObjectName("action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade")
        self.action_MenuFiscal_Ped_gios = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Ped_gios.setObjectName("action_MenuFiscal_Ped_gios")
        self.action_MenuFiscal_Manuten_ao_de_Bombas = QtGui.QAction(MainWindowFISCAL)
        self.action_MenuFiscal_Manuten_ao_de_Bombas.setObjectName("action_MenuFiscal_Manuten_ao_de_Bombas")
        self.actionM_todo_rGerarSPED_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarSPED_ECF_Daruma.setObjectName("actionM_todo_rGerarSPED_ECF_Daruma")
        self.actionM_todo_rGerarSINTEGRA_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarSINTEGRA_ECF_Daruma.setObjectName("actionM_todo_rGerarSINTEGRA_ECF_Daruma")
        self.actionM_todo_rGerarNFP_ECF_Daruma = QtGui.QAction(MainWindowFISCAL)
        self.actionM_todo_rGerarNFP_ECF_Daruma.setObjectName("actionM_todo_rGerarNFP_ECF_Daruma")
        self.menuAbertura_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFAbrir_ECF_Daruma)
        self.menuAbertura_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFAbrirPadrao_ECF_Daruma)
        self.menuRegistro_de_Item.addAction(self.actionM_todo_iCFVender_ECF_Daruma)
        self.menuRegistro_de_Item.addAction(self.actionM_todo_iCFVenderSemDesc_ECF_Daruma)
        self.menuRegistro_de_Item.addAction(self.actionM_todo_iCFVenderResumido_ECF_Daruma)
        self.menuDesconto_ou_Acr_scimo_em_Item.addAction(self.actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma)
        self.menuDesconto_ou_Acr_scimo_em_Item.addAction(self.actionM_todo_iCFLancarDescontoItem_ECF_Daruma)
        self.menuDesconto_ou_Acr_scimo_em_Item.addAction(self.actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma)
        self.menuDesconto_ou_Acr_scimo_em_Item.addAction(self.actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma)
        self.menuCancelamento_Total_de_Item_em_Cupom_Fiscal.addAction(self.actionM_todo_iCFCancelarItem_ECF_Daruma)
        self.menuCancelamento_Total_de_Item_em_Cupom_Fiscal.addAction(self.actionM_todo_iCFCancelarUltimoItem_ECF_Daruma)
        self.menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal.addAction(self.actionM_todo_iCFCancelarItemParcial_ECF_Daruma)
        self.menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal.addAction(self.actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma)
        self.menuCancelamento_de_Desconto_em_Item.addAction(self.actionM_todo_iCFCancelarDescontoItem_ECF_Daruma)
        self.menuCancelamento_de_Desconto_em_Item.addAction(self.actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma)
        self.menuCancelamento_de_Acr_scimo_em_Item.addAction(self.actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma)
        self.menuCancelamento_de_Acr_scimo_em_Item.addAction(self.actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma)
        self.menuTotaliza_o_do_Cupom_Fiscal.addAction(self.actionM_todo_iCFTotalizarCupom_ECF_Daruma)
        self.menuTotaliza_o_do_Cupom_Fiscal.addAction(self.actionM_todo_iCFTotalizarPadrao_ECF_Daruma)
        self.menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF.addAction(self.actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma)
        self.menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF.addAction(self.actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma)
        self.menuDescri_o_da_Forma_de_Pagamento.addAction(self.actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma)
        self.menuDescri_o_da_Forma_de_Pagamento.addAction(self.actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma)
        self.menuDescri_o_da_Forma_de_Pagamento.addAction(self.actionM_todo_iCFEfetuarPagamento_ECF_Daruma)
        self.menuEncerramento_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFEncerrarPadrao_ECF_Daruma)
        self.menuEncerramento_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma)
        self.menuEncerramento_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFEncerrarResumido_ECF_Daruma)
        self.menuEncerramento_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFEncerrar_ECF_Daruma)
        self.menuEncerramento_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma)
        self.menuCancelamento_de_Cupom_Fiscal.addAction(self.actionM_todo_iCFCancelar_ECF_Daruma)
        self.menuIdentificac_o_de_Consumidor_no_Rodap_do_Cupom_Fiscal.addAction(self.actionM_todo_iCFIdentificarConsumidor_ECF_Daruma)
        self.menuCupom_Mania_para_Estado_do_RJ.addAction(self.actionConfigurac_o_Cupom_Mania)
        self.menuCupom_Mania_para_Estado_do_RJ.addAction(self.actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania)
        self.menuEstorno_Meio_de_Pagamento.addAction(self.actionM_todo_iEstornarPagamento_ECF_Daruma)
        self.menuExemplos.addAction(self.actionCupom_Fiscal_Completo)
        self.menuExemplos.addAction(self.actionCupom_Fiscal_Resumido)
        self.menuExemplos.addAction(self.actionCupom_Fiscal_Pr_Venda)
        self.menuCupom_Fiscal.addAction(self.menuAbertura_de_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuRegistro_de_Item.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuDesconto_ou_Acr_scimo_em_Item.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCancelamento_Total_de_Item_em_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCancelamento_de_Acr_scimo_em_Item.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCancelamento_de_Desconto_em_Item.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuTotaliza_o_do_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuDescri_o_da_Forma_de_Pagamento.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuEncerramento_de_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCancelamento_de_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuIdentificac_o_de_Consumidor_no_Rodap_do_Cupom_Fiscal.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuCupom_Mania_para_Estado_do_RJ.menuAction())
        self.menuCupom_Fiscal.addAction(self.menuEstorno_Meio_de_Pagamento.menuAction())
        self.menuCupom_Fiscal.addSeparator()
        self.menuCupom_Fiscal.addAction(self.actionTeste_de_Venda_de_Itens_Sem_Parar)
        self.menuCupom_Fiscal.addAction(self.menuExemplos.menuAction())
        self.menuLeitura_X.addAction(self.actionM_todo_iLeituraX_ECF_Daruma)
        self.menuLeitura_X.addAction(self.actionM_todo_rLeituraX_ECF_Daruma)
        self.menuLeitura_X.addAction(self.actionM_todo_rLeituraXCustomizada_ECF_Daruma)
        self.menuRedu_ao_Z.addAction(self.actionM_todo_iReducaoZ_ECF_Daruma)
        self.menuSangria.addAction(self.actionM_todo_iSangria_ECF_Daruma)
        self.menuSangria.addAction(self.actionM_todo_iSangriaPadrao_ECF_Daruma)
        self.menuSuprimento.addAction(self.actionM_todo_iSuprimento_ECF_Daruma)
        self.menuSuprimento.addAction(self.actionM_todo_iSuprimentoPadrao_ECF_Daruma)
        self.menuLeitura_da_Mem_ria_Fiscal.addAction(self.actionM_todo_iMFLer_ECF_Daruma)
        self.menuLeitura_da_Mem_ria_Fiscal.addAction(self.actionM_todo_iMFLerSerial_ECF_Daruma)
        self.menuRelat_rios_Fiscais.addAction(self.menuLeitura_X.menuAction())
        self.menuRelat_rios_Fiscais.addAction(self.menuRedu_ao_Z.menuAction())
        self.menuRelat_rios_Fiscais.addAction(self.menuSangria.menuAction())
        self.menuRelat_rios_Fiscais.addAction(self.menuSuprimento.menuAction())
        self.menuRelat_rios_Fiscais.addAction(self.menuLeitura_da_Mem_ria_Fiscal.menuAction())
        self.menuAbertura_de_CCD.addAction(self.actionM_todo_iCCDAbrir_ECF_Daruma)
        self.menuAbertura_de_CCD.addAction(self.actionM_todo_iCCDAbrirPadrao_ECF_Daruma)
        self.menuAbertura_de_CCD.addAction(self.actionM_todo_iCCDAbrirSimplificado_ECF_Daruma)
        self.menuImpress_o_de_Texto.addAction(self.actionM_todo_iCCDImprimirTexto_ECF_Daruma)
        self.menuImpress_o_de_Texto.addAction(self.actionM_todo_iCCDImprimirArquivo_ECF_Daruma)
        self.menuEncerramento_de_CCD.addAction(self.actionM_todo_iCCDFechar_ECF_Daruma)
        self.menuEstorno_de_CCD.addAction(self.actionM_todo_iCCDEstornar_ECF_Daruma)
        self.menuEstorno_de_CCD.addAction(self.actionM_todo_iCCDEstornarPadrao_ECF_Daruma)
        self.menuTEF.addAction(self.actionM_todo_eTEF_EsperarArquivo_ECF_Daruma)
        self.menuTEF.addAction(self.actionM_todo_eTEF_TravarTeclado_ECF_Daruma)
        self.menuTEF.addAction(self.actionM_todo_eTEF_SetarFoco_ECF_Daruma)
        self.menuTEF.addAction(self.actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma)
        self.menuTEF.addAction(self.actionM_todo_iTEF_ImprimirResposta_ECF_Daruma)
        self.menuTEF.addAction(self.actionM_todo_iTEF_Fechar_ECF_Daruma)
        self.menuTEF.addAction(self.actionExemplo_Completo_TEF)
        self.menuCCD_TEF.addAction(self.menuAbertura_de_CCD.menuAction())
        self.menuCCD_TEF.addAction(self.menuImpress_o_de_Texto.menuAction())
        self.menuCCD_TEF.addAction(self.menuEncerramento_de_CCD.menuAction())
        self.menuCCD_TEF.addAction(self.menuEstorno_de_CCD.menuAction())
        self.menuCCD_TEF.addAction(self.action2_Via_de_CCD)
        self.menuCCD_TEF.addAction(self.menuTEF.menuAction())
        self.menuCCD_TEF.addSeparator()
        self.menuCCD_TEF.addAction(self.actionExemplo_CCD_Completo)
        self.menuAbertura_de_Comprovante_N_o_Fiscal.addAction(self.actionM_todo_iCNFAbrir_ECF_Daruma)
        self.menuAbertura_de_Comprovante_N_o_Fiscal.addAction(self.actionM_todo_iCNFAbrirPadrao_ECF_Daruma)
        self.menuRecebimento_de_Itens.addAction(self.actionM_todo_iCNFReceber_ECF_Daruma)
        self.menuRecebimento_de_Itens.addAction(self.actionM_todo_iCNFReceberSemDesc_ECF_Daruma)
        self.menuCancelamento_de_Item.addAction(self.actionM_todo_iCNFCancelarItem_ECF_Daruma)
        self.menuCancelamento_de_Item.addAction(self.actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma)
        self.menuCancelamento_de_Acr_scimo_em_Item_2.addAction(self.actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma)
        self.menuCancelamento_de_Acr_scimo_em_Item_2.addAction(self.actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma)
        self.menuCancelamento_de_Desconto_em_Item_2.addAction(self.actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma)
        self.menuCancelamento_de_Desconto_em_Item_2.addAction(self.actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma)
        self.menuTotaliza_ao_de_CNF.addAction(self.actionM_todo_iCNFTotalizarComprovante_ECF_Daruma)
        self.menuTotaliza_ao_de_CNF.addAction(self.actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma)
        self.menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF.addAction(self.actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma)
        self.menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF.addAction(self.actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma)
        self.menuEncerramento_de_CNF.addAction(self.actionM_todo_iCNFEncerrar_ECF_Daruma)
        self.menuEncerramento_de_CNF.addAction(self.actionM_todo_iCNFEncerrarPadrao_ECF_Daruma)
        self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF.addAction(self.actionM_todo_iCNFEfetuarPagamento_ECF_Daruma)
        self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF.addAction(self.actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma)
        self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF.addAction(self.actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma)
        self.menuCancelamento_de_CNF.addAction(self.actionM_todo_iCNFCancelar_ECF_Daruma)
        self.menuComprovante_N_o_Fiscal.addAction(self.menuAbertura_de_Comprovante_N_o_Fiscal.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuRecebimento_de_Itens.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuCancelamento_de_Item.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuCancelamento_de_Acr_scimo_em_Item_2.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuCancelamento_de_Desconto_em_Item_2.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuTotaliza_ao_de_CNF.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuEncerramento_de_CNF.menuAction())
        self.menuComprovante_N_o_Fiscal.addAction(self.menuCancelamento_de_CNF.menuAction())
        self.menuComprovante_N_o_Fiscal.addSeparator()
        self.menuComprovante_N_o_Fiscal.addAction(self.actionExemplo_CNF_Detalhado)
        self.menuAbertura_de_Relat_rio_Gerencial.addAction(self.actionM_todo_iRGAbrir_ECF_Daruma)
        self.menuAbertura_de_Relat_rio_Gerencial.addAction(self.actionM_todo_iRGAbrirIndice_ECF_Daruma)
        self.menuAbertura_de_Relat_rio_Gerencial.addAction(self.actionM_todo_iRGAbrirPadrao_ECF_Daruma)
        self.menuTexto_para_Impress_o.addAction(self.actionM_todo_iRGImprimirTexto_ECF_Daruma)
        self.menuEncerramento_do_Relat_rio_Gerencial.addAction(self.actionM_todo_iRGFechar_ECF_Daruma)
        self.menuRelat_rio_Gerencial.addAction(self.menuAbertura_de_Relat_rio_Gerencial.menuAction())
        self.menuRelat_rio_Gerencial.addAction(self.menuTexto_para_Impress_o.menuAction())
        self.menuRelat_rio_Gerencial.addAction(self.menuEncerramento_do_Relat_rio_Gerencial.menuAction())
        self.menuECF.addAction(self.actionM_todo_confCadastrar_ECF_Daruma)
        self.menuECF.addAction(self.actionM_todo_confCadastrarPadrao_ECF_Daruma)
        self.menuEspeciais.addAction(self.actionM_todo_eEnviarComando_ECF_Daruma)
        self.menuHor_rio_de_Ver_o.addAction(self.actionHabilitarHVerao)
        self.menuHor_rio_de_Ver_o.addAction(self.actionDesabilitarHVerao)
        self.menuModo_Pr_Venda.addAction(self.actionHabilitarMPreVenda)
        self.menuModo_Pr_Venda.addAction(self.actionDesabilitarMPreVenda)
        self.menuPrograma_o_do_ECF.addAction(self.menuECF.menuAction())
        self.menuPrograma_o_do_ECF.addAction(self.menuEspeciais.menuAction())
        self.menuPrograma_o_do_ECF.addAction(self.menuHor_rio_de_Ver_o.menuAction())
        self.menuPrograma_o_do_ECF.addAction(self.menuModo_Pr_Venda.menuAction())
        self.menuPrograma_o_do_ECF.addAction(self.actionAvan_o_de_Papel)
        self.menuPrograma_o_do_ECF.addAction(self.actionLoja)
        self.menuPrograma_o_do_ECF.addAction(self.actionConfOperador)
        self.menuRetornos_e_Status_do_ECF.addAction(self.actionM_todos_para_Retornos_e_Status)
        self.menuBilhete_de_Passagem.addAction(self.actionM_todo_iCFBPAbrir_ECF_Daruma)
        self.menuBilhete_de_Passagem.addAction(self.actionM_todo_iCFBPVender_ECF_Daruma)
        self.menuBilhete_de_Passagem.addAction(self.actionM_todo_confCFBPProgramarUF_ECF_Daruma)
        self.menuGaveta_Autentica_e_Outros.addAction(self.actionM_todo_eAcionarGuilhotina_ECF_Daruma)
        self.menuGaveta_Autentica_e_Outros.addAction(self.actionM_todo_eAbrirGaveta_ECF_Daruma)
        self.menuGaveta_Autentica_e_Outros.addAction(self.actionM_todo_rStatusGaveta_ECF_Daruma)
        self.menuGaveta_Autentica_e_Outros.addAction(self.actionM_todo_eCarregarBitmapPromocional_ECF_Daruma)
        self.menuCheque.addAction(self.actionM_todo_iChequeImprimir_FS2100_Daruma)
        self.menuC_digo_de_Barras.addAction(self.actionM_todo_iImprimirCodigoBarras_ECF_Daruma)
        self.menuRegistry.addAction(self.actionM_todo_regRetornaValorChave_DarumaFramework)
        self.menuRegistry.addAction(self.actionM_todo_regAlterarValor_Daruma)
        self.menuRegistry.addAction(self.actionM_todo_eDefinirProduto_Daruma)
        self.menuRegistry.addAction(self.actionM_todo_eDefinirModoRegistro_Daruma)
        self.menuRegistry.addAction(self.actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionRGerarEspelhoMFD_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarRelatorio_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarRelatorioOffline_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarMF_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarMFD_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarTDM_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarSPED_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarSINTEGRA_ECF_Daruma)
        self.menuGera_ao_de_Arquivos.addAction(self.actionM_todo_rGerarNFP_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rCalcularMD5_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rRetornarGTCodificado_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rVerificarGTCodificado_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rCodigoModeloFiscal_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_eRSAAssinarArquivo_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_rRSAChavePublica_ECF_Daruma)
        self.menuPAF_ECF.addAction(self.actionM_todo_eMemoriaFiscal_ECF_Daruma)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_LX)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_LMFC)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_LMFS)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Espelho_MFD)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Arq_MFD)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Tab_Produto)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Estoque)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Movimento_por_ECF)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Meios_de_Pgto)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Vendas_por_Per_odo)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Identifica_ao_do_PAF_ECF)
        self.menuMenu_Fiscal.addSeparator()
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_DAV_Emitidos)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Encerrantes)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Transf_Mesas)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Manifesto_Fiscal_de_Viagem)
        self.menuMenu_Fiscal.addSeparator()
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Cupom_de_Embarque)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Cupons_de_Embarque_Gratuidade)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Ped_gios)
        self.menuMenu_Fiscal.addAction(self.action_MenuFiscal_Manuten_ao_de_Bombas)
        self.menubar.addAction(self.menuCupom_Fiscal.menuAction())
        self.menubar.addAction(self.menuCCD_TEF.menuAction())
        self.menubar.addAction(self.menuComprovante_N_o_Fiscal.menuAction())
        self.menubar.addAction(self.menuRelat_rio_Gerencial.menuAction())
        self.menubar.addAction(self.menuBilhete_de_Passagem.menuAction())
        self.menubar.addAction(self.menuRelat_rios_Fiscais.menuAction())
        self.menubar.addAction(self.menuPrograma_o_do_ECF.menuAction())
        self.menubar.addAction(self.menuRetornos_e_Status_do_ECF.menuAction())
        self.menubar.addAction(self.menuGaveta_Autentica_e_Outros.menuAction())
        self.menubar.addAction(self.menuCheque.menuAction())
        self.menubar.addAction(self.menuC_digo_de_Barras.menuAction())
        self.menubar.addAction(self.menuRegistry.menuAction())
        self.menubar.addAction(self.menuGera_ao_de_Arquivos.menuAction())
        self.menubar.addAction(self.menuPAF_ECF.menuAction())
        self.menubar.addAction(self.menuMenu_Fiscal.menuAction())

        self.retranslateUi(MainWindowFISCAL)
        QtCore.QMetaObject.connectSlotsByName(MainWindowFISCAL)

    def retranslateUi(self, MainWindowFISCAL):
        MainWindowFISCAL.setWindowTitle(QtGui.QApplication.translate("MainWindowFISCAL", "DarumaFrameWork - Módulo ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindowFISCAL", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Dúvidas? Ligue: 0800 77 0332 0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindowFISCAL", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Impressora Fiscal</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; font-weight:600;\">Driver: DarumaFramework</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEncerrar.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbertura_de_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Abertura de Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRegistro_de_Item.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Registro de Item", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDesconto_ou_Acr_scimo_em_Item.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Desconto ou Acréscimo em Item ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_Total_de_Item_em_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento Total de Item em Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_Parcial_de_Item_em_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento Parcial de Item em Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Desconto_em_Item.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Desconto em Item", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Acr_scimo_em_Item.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Acréscimo em Item", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTotaliza_o_do_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Totalização do Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Desconto_Acrescimo_em_SubTotal_do_CF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Desconto/Acrescimo em SubTotal do CF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDescri_o_da_Forma_de_Pagamento.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Descrição da Forma de Pagamento", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEncerramento_de_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Encerramento de Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuIdentificac_o_de_Consumidor_no_Rodap_do_Cupom_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Identificacão de Consumidor no Rodapé do Cupom Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCupom_Mania_para_Estado_do_RJ.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cupom Mania para Estado do RJ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEstorno_Meio_de_Pagamento.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Estorno Meio de Pagamento", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExemplos.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Exemplos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRelat_rios_Fiscais.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Relatórios Fiscais", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLeitura_X.setToolTip(QtGui.QApplication.translate("MainWindowFISCAL", "Relatórios Fiscais", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLeitura_X.setStatusTip(QtGui.QApplication.translate("MainWindowFISCAL", "Relatórios Fiscais", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLeitura_X.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Leitura X", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRedu_ao_Z.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Reduçao Z", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSangria.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Sangria", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSuprimento.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Suprimento", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLeitura_da_Mem_ria_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Leitura da Memória Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCCD_TEF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "CCD - TEF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbertura_de_CCD.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Abertura de CCD", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImpress_o_de_Texto.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Impressão de Texto", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEncerramento_de_CCD.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Encerramento de CCD", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEstorno_de_CCD.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Estorno de CCD", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTEF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "TEF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuComprovante_N_o_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Comprovante Não Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbertura_de_Comprovante_N_o_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Abertura de Comprovante Não Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRecebimento_de_Itens.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Recebimento de Itens", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Item.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Item", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Acr_scimo_em_Item_2.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Acréscimo em Item", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Desconto_em_Item_2.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Desconto em Item", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTotaliza_ao_de_CNF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Totalizaçao de CNF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_Acr_scimo_Desconto_em_Subtotal_de_CNF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de Acréscimo/Desconto em Subtotal de CNF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEncerramento_de_CNF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Encerramento de CNF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDescri_ao_dos_Meios_de_Pagamento_de_CNF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Descriçao dos Meios de Pagamento de CNF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCancelamento_de_CNF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cancelamento de CNF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRelat_rio_Gerencial.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Relatório Gerencial", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbertura_de_Relat_rio_Gerencial.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Abertura de Relatório Gerencial", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTexto_para_Impress_o.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Texto para Impressão", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEncerramento_do_Relat_rio_Gerencial.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Encerramento do Relatório Gerencial", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPrograma_o_do_ECF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Programação do ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuECF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEspeciais.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Especiais", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHor_rio_de_Ver_o.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Horário de Verão", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModo_Pr_Venda.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Modo Pré-Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRetornos_e_Status_do_ECF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Retornos e Status do ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBilhete_de_Passagem.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Bilhete de Passagem", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGaveta_Autentica_e_Outros.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Gaveta, Autentica e Outros", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCheque.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Cheque", None, QtGui.QApplication.UnicodeUTF8))
        self.menuC_digo_de_Barras.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Código de Barras", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRegistry.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Registry", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGera_ao_de_Arquivos.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Geração de Arquivos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPAF_ECF.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "PAF-ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu_Fiscal.setTitle(QtGui.QApplication.translate("MainWindowFISCAL", "Menu Fiscal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iLeituraX_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iLeituraX_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iLeituraX_ECF_Daruma.setStatusTip(QtGui.QApplication.translate("MainWindowFISCAL", "Método para impressão da Leitura X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLeituraX_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rLeituraX_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLeituraX_ECF_Daruma.setStatusTip(QtGui.QApplication.translate("MainWindowFISCAL", "Método para gerar a Leitura X em arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFAbrir_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "iCFAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFAbrir_ECF_Daruma.setStatusTip(QtGui.QApplication.translate("MainWindowFISCAL", "Método para abrir cupom com identificação do consumidor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFAbrirPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "iCFAbrirPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFAbrirPadrao_ECF_Daruma.setStatusTip(QtGui.QApplication.translate("MainWindowFISCAL", "Método para abrir o cupom sem identificar o consumidor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFVender_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFVender_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFVenderSemDesc_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFVenderSemDesc_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFVenderResumido_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFVenderResumido_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFLancarAcrescimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFLancarAcrescimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFLancarDescontoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFLancarDescontoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFLancarAcrescimoUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFLancarAcrescimoUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFLancarDescontoUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFLancarDescontoUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarItemParcial_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarItemParcial_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarUltimoItemParcial_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarUltimoItemParcial_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarDescontoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarDescontoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarDescontoUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarDescontoUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarAcrescimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarAcrescimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarAcrescimoUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarAcrescimoUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFTotalizarCupom_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFTotalizarCupom_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFTotalizarPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFTotalizarPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarDescontoSubTotal_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarDescontoSubTotal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelarAcrescimoSubTotal_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelarAcrescimoSubTotal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEfetuarPagamentoPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEfetuarPagamentoPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEfetuarPagamentoFormatado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEfetuarPagamentoFormatado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEfetuarPagamento_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEfetuarPagamento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEncerrarPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEncerrarPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEncerrarConfigMsg_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEncerrarConfigMsg_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEncerrarResumido_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEncerrarResumido_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEncerrar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEncerrar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFEncerrarCupomAdicional_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFEmitirCupomAdicional_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFCancelar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFCancelar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFIdentificarConsumidor_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFIdentificarConsumidor_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurac_o_Cupom_Mania.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Configuracão Cupom Mania", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTotal_de_ISS_e_ICMS_contabilizando_ultimo_CF_Mania.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Total de ISS e ICMS contabilizando ultimo CF Mania", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iEstornarPagamento_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iEstornarPagamento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTeste_de_Venda_de_Itens_Sem_Parar.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Teste de Venda de Itens Sem Parar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCupom_Fiscal_Completo.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Cupom Fiscal Completo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCupom_Fiscal_Resumido.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Cupom Fiscal Resumido", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCupom_Fiscal_Pr_Venda.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Cupom Fiscal Pré Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_CCD_Completo.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Exemplo CCD Completo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDAbrir_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDAbrirPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDAbrirPadrao__ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDAbrirSimplificado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDAbrirSimplificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDImprimirTexto_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDImprimirTexto_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDImprimirArquivo_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDImprimirArquivo_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDFechar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDFechar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDEstornar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDEstornar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCCDEstornarPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCCDEstornarPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.action2_Via_de_CCD.setText(QtGui.QApplication.translate("MainWindowFISCAL", "2º Via de CCD", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eTEF_EsperarArquivo_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eTEF_EsperarArquivo_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_CNF_Detalhado.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Exemplo CNF Detalhado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFAbrir_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFAbrirPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFAbrirPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFReceber_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFReceber_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFReceberSemDesc_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFReceberSemDesc_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarAcrescimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarAcrescimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarAcrescimoUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarAcrescimoUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarDescontoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarDescontoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarDescontoUltimoItem_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarDescontoUltimoItem_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFTotalizarComprovante_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFTotalizarComprovante_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFTotalizarComprovantePadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFTotalizarComprovantePadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarAcrescimoSubtotal_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarAcrescimoSubtotal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelarDescontoSubtotal_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelarDescontoSubtotal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFEfetuarPagamento_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFEfetuarPagamento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFEfetuarPagamentoFormatado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFEfetuarPagamentoFormatado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFEfetuarPagamentoPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFEfetuarPagamentoPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFEncerrar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFEncerrar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFEncerrarPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFEncerrarPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCNFCancelar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCNFCancelar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iRGAbrir_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iRGAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iRGAbrirIndice_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iRGAbrirIndice_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iRGAbrirPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iRGAbrirPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iRGImprimirTexto_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iRGImprimirTexto_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iRGFechar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iRGFechar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rLeituraXCustomizada_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rLeituraXCustomizada_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iReducaoZ_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iReducaoZ_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iSangria_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iSangria_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iSangriaPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iSangriaPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iSuprimento_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iSuprimento_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iSuprimentoPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iSuprimentoPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iMFLer_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iMFLer_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iMFLerSerial_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iMFLerSerial_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_confCadastrar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método confCadastrar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_confCadastrarPadrao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método confCadastrarPadrao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eEnviarComando_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eEnviarComando_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarHVerao.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarHVerao.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarMPreVenda.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarMPreVenda.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAvan_o_de_Papel.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Avanço de Papel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoja.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Loja", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfOperador.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Operador", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todos_para_Retornos_e_Status.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Métodos para Retornos e Status", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFBPAbrir_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFBPAbrir_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iCFBPVender_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iCFBPVender_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_confCFBPProgramarUF_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método confCFBPProgramarUF_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eAcionarGuilhotina_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eAcionarGuilhotina_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eAbrirGaveta_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eAbrirGaveta_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusGaveta_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rStatusGaveta_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eCarregarBitmapPromocional_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eCarregarBitmapPromocional_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iChequeImprimir_FS2100_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iChequeImprimir_FS2100_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iImprimirCodigoBarras_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iImprimirCodigoBarras_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionregRetornaValorChave_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowFISCAL", "regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regAlterarValor_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método regAlterarValor_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRGerarEspelhoMFD_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarEspelhoMFD_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regRetornaValorChave_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regAlterarValor_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método regAlterarValor_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarRelatorio_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarRelatorio_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarRelatorioOffline_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarRelatorioOffline_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarMF_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarMF_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarMFD_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarMFD_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarTDM_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarTDM_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eTEF_TravarTeclado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eTEF_TravarTeclado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eTEF_SetarFoco_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eTEF_SetarFoco_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iTEF_ImprimirRespostaCartao_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iTEF_ImprimirRespostaCartao_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iTEF_ImprimirResposta_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iTEF_ImprimirResposta_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iTEF_Fechar_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método iTEF_Fechar_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_Completo_TEF.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Exemplo Completo TEF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eDefinirProduto_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eDefinirProduto_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eDefinirModoRegistro_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eDefinirModoRegistro_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regCFCupomAdicionalDllConfig_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método regCFCupomAdicionalDllConfig_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rCalcularMD5_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rCalcularMD5_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rRetornarGTCodificado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rRetornarGTCodificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rVerificarGTCodificado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rVerificarGTCodificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rRetornarNumeroSerieCodificado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rRetornarNumeroSerieCodificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rVerificarNumeroSerieCodificado_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rVerificarNumeroSerieCodificado_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rCodigoModeloFiscal_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rCodigoModeloFiscal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eRSAAssinarArquivo_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eRSAAssinarArquivo_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rRSAChavePublica_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rRSAChavePublica_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eMemoriaFiscal_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método eMemoriaFiscal_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_LX.setText(QtGui.QApplication.translate("MainWindowFISCAL", "LX", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_LMFC.setText(QtGui.QApplication.translate("MainWindowFISCAL", "LMFC", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_LMFS.setText(QtGui.QApplication.translate("MainWindowFISCAL", "LMFS", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Espelho_MFD.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Espelho MFD", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Arq_MFD.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Arq MFD", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Tab_Produto.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Tab. Prod", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Estoque.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Estoque", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Movimento_por_ECF.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Movimento por ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Meios_de_Pgto.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Meios de Pgto", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Vendas_por_Per_odo.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Vendas por Período", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Identifica_ao_do_PAF_ECF.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Identificaçao do PAF-ECF", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Tab_T_cnico_ndices_de_Produ_o.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Tab. Técnico Índices de Produção", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_DAV_Emitidos.setText(QtGui.QApplication.translate("MainWindowFISCAL", "DAV Emitidos", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Encerrantes.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Encerrantes", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Transf_Mesas.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Transf. Mesas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Manifesto_Fiscal_de_Viagem.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Manifesto Fiscal de Viagem", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Cupom_de_Embarque.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Cupom de Embarque", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Embarque.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Leitura do Movimento Diário de Cupom de Embarque", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Cupons_de_Embarque_Gratuidade.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Cupons de Embarque Gratuidade", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Leitura_do_Movimento_Di_rio_de_Cupom_de_Gratuidade.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Leitura do Movimento Diário de Cupom de Gratuidade", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Ped_gios.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Pedágios", None, QtGui.QApplication.UnicodeUTF8))
        self.action_MenuFiscal_Manuten_ao_de_Bombas.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Manutençao de Bombas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarSPED_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarSPED_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarSINTEGRA_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarSINTEGRA_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rGerarNFP_ECF_Daruma.setText(QtGui.QApplication.translate("MainWindowFISCAL", "Método rGerarNFP_ECF_Daruma", None, QtGui.QApplication.UnicodeUTF8))

