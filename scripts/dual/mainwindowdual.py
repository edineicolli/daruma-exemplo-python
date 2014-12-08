# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowdual.ui'
#
# Created: Mon Nov 24 22:25:05 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from pydaruma.pydaruma import regAguardarProcesso_DUAL_DarumaFramework
from scripts.dual.retornodual import tratarRetornoDUAL
from scripts.dual.ui_dual_iautenticardocumento import Ui_ui_dual_iautenticardocumento
from scripts.dual.ui_dual_ienviarbmp import Ui_ui_dual_ienviarbmp
from scripts.dual.ui_dual_iimprimirarquivo import Ui_ui_dual_iimprimirarquivo
from scripts.dual.ui_dual_iimprimirtexto import Ui_ui_dual_iimprimirtexto
from scripts.dual.ui_dual_loopingdestatus import Ui_ui_dual_loopingdestatus
from scripts.dual.ui_dual_loopingstatusdocumento import Ui_ui_dual_loopingstatusdocumento
from scripts.dual.ui_dual_rconsultastatusimpressora import Ui_ui_dual_rconsultastatusimpressora
from scripts.dual.ui_dual_reglinhasguilhotina import Ui_ui_dual_reglinhasguilhotina
from scripts.dual.ui_dual_regportacomunicacao import Ui_ui_dual_regportacomunicacao
from scripts.dual.ui_dual_regtabulacao import Ui_ui_dual_regtabulacao
from scripts.dual.ui_dual_regvelocidade import Ui_ui_dual_regvelocidade
from scripts.fiscal.ui_fiscal_regretornavalorchave import Ui_ui_FISCAL_regRetornaValorChave
from scripts.ui_geral_contatossuporte import Ui_ui_Geral_ContatosSuporte


class Ui_MainWindowDual(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindowDual, self).__init__()

        self.setupUi(self)
        #//CHAMA A FUNÇAO PARA CARREGAR A BIBLIOTECA DARUMAFRAMEWORK
        #carregarDarumaFramework(this);

        self.actionM_todo_eDefinirProduto_Daruma.triggered.connect(self.on_actionM_todo_eDefinirProduto_Daruma_triggered)
        self.actionM_todo_regRetornaValorChave_DarumaFramework.triggered.connect(self.on_actionM_todo_regRetornaValorChave_DarumaFramework_triggered)
        self.actionHabilitarAguardarProcesso.triggered.connect(self.on_actionHabilitarAguardarProcesso_triggered)
        self.actionDesabilitarAguardarProcesso.triggered.connect(self.on_actionDesabilitarAguardarProcesso_triggered)
        self.actionHabilitarEnterFinal.triggered.connect(self.on_actionHabilitarEnterFinal_triggered)
        self.actionDesabilitarEnterFinal.triggered.connect(self.on_actionDesabilitarEnterFinal_triggered)
        self.actionPadraoGaveta.triggered.connect(self.on_actionPadraoGaveta_triggered)
        self.actionAlteraPadraoGaveta.triggered.connect(self.on_actionAlteraPadraoGaveta_triggered)
        self.actionHabilitarTermica.triggered.connect(self.on_actionHabilitarTermica_triggered)
        self.actionDesabilitarTermica.triggered.connect(self.on_actionDesabilitarTermica_triggered)
        self.actionHabilitarCodePageAutomatico.triggered.connect(self.on_actionHabilitarCodePageAutomatico_triggered)
        self.actionDesabilitarCodePageAutomatico.triggered.connect(self.on_actionDesabilitarCodePageAutomatico_triggered)
        self.actionHabilitarZeroCortado.triggered.connect(self.on_actionHabilitarZeroCortado_triggered)
        self.actionDesabilitarZeroCortado.triggered.connect(self.on_actionDesabilitarZeroCortado_triggered)
        self.actionExemplo_1_Buffer.triggered.connect(self.on_actionExemplo_1_Buffer_triggered)
        self.actionExemplo_2_Tabula_o.triggered.connect(self.on_actionExemplo_2_Tabula_o_triggered)
        self.actionExemplo_3_Linha_a_Linha.triggered.connect(self.on_actionExemplo_3_Linha_a_Linha_triggered)
        self.actionExemplo_1_Buffer_2.triggered.connect(self.on_actionExemplo_1_Buffer_2_triggered)
        self.actionExemplo_2_Tabula_ao.triggered.connect(self.on_actionExemplo_2_Tabula_ao_triggered)
        self.actionExemplo_3_Linha_a_Linha_2.triggered.connect(self.on_actionExemplo_3_Linha_a_Linha_2_triggered)
        self.actionTeste_Completo_em_Buffer.triggered.connect(self.on_actionTeste_Completo_em_Buffer_triggered)
        self.actionTeste_Completo_Linha_a_Linha.triggered.connect(self.on_actionTeste_Completo_Linha_a_Linha_triggered)
        self.actionExemplo_4_Formulario.triggered.connect(self.on_actionExemplo_4_Formulario_triggered)
        self.actionM_todo_regVelocidade_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_regVelocidade_DUAL_DarumaFramework_triggered)
        self.actionM_todo_regTabulacao_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_regTabulacao_DUAL_DarumaFramework_triggered)
        self.actionM_todo_regPortaComunicacao_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_regPortaComunicacao_DUAL_DarumaFramework_triggered)
        self.actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework_triggered)
        self.actionM_todo_rStatusImpressora_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_rStatusImpressora_DUAL_DarumaFramework_triggered)
        self.actionM_todo_rStatusDocumento_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_rStatusDocumento_DUAL_DarumaFramework_triggered)
        self.actionM_todo_rStatusGaveta_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_rStatusGaveta_DUAL_DarumaFramework_triggered)
        self.actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework_triggered)
        self.actionTeste_para_Looping_de_verica_o_de_Status.triggered.connect(self.on_actionTeste_para_Looping_de_verica_o_de_Status_triggered)
        self.actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento.triggered.connect(self.on_actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento_triggered)
        self.actionM_todo_iEnviarBMP_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_iEnviarBMP_DUAL_DarumaFramework_triggered)
        self.actionM_todo_iAcionarGaveta_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_iAcionarGaveta_DUAL_DarumaFramework_triggered)
        self.actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework_triggered)
        self.actionM_todo_iImprimirArquivo_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_iImprimirArquivo_DUAL_DarumaFramework_triggered)
        self.actionM_todo_iImprimirTexto_DUAL_DarumaFramework.triggered.connect(self.on_actionM_todo_iImprimirTexto_DUAL_DarumaFramework_triggered)
        self.pushButtonEncerrar.clicked.connect(self.on_pushButtonEncerrar_clicked)
        self.pushButtonContatos_2.clicked.connect(self.on_pushButtonContatos_clicked)

    def on_actionM_todo_eDefinirProduto_Daruma_triggered(self):
        #tratarRetornoDUAL(eDefinirProduto_Daruma("DUAL"), self)
        pass


    def on_actionM_todo_regRetornaValorChave_DarumaFramework_triggered(self):
        self.form_FISCAL_regRetornaValorChave = Ui_ui_FISCAL_regRetornaValorChave()
        self.form_FISCAL_regRetornaValorChave.show()


    def on_actionHabilitarAguardarProcesso_triggered(self):
        tratarRetornoDUAL(regAguardarProcesso_DUAL_DarumaFramework("1"), self)


    def on_actionDesabilitarAguardarProcesso_triggered(self):
        tratarRetornoDUAL(regAguardarProcesso_DUAL_DarumaFramework("0"), self)


    def on_actionHabilitarEnterFinal_triggered(self):
        #tratarRetornoDUAL(regEnterFinal_DUAL_DarumaFramework("1"), self)
        pass


    def on_actionDesabilitarEnterFinal_triggered(self):
        #tratarRetornoDUAL(regEnterFinal_DUAL_DarumaFramework("0"), self)
        pass


    def on_actionPadraoGaveta_triggered(self):
        #tratarRetornoDUAL(regModoGaveta_DUAL_DarumaFramework("0"), self)
        pass


    def on_actionAlteraPadraoGaveta_triggered(self):
        #tratarRetornoDUAL(regModoGaveta_DUAL_DarumaFramework("1"), self)
        pass


    def on_actionHabilitarTermica_triggered(self):
        #tratarRetornoDUAL(regTermica_DUAL_DarumaFramework("1"), self)
        pass


    def on_actionDesabilitarTermica_triggered(self):
        #tratarRetornoDUAL(regTermica_DUAL_DarumaFramework("0"), self)
        pass


    def on_actionHabilitarCodePageAutomatico_triggered(self):
        #tratarRetornoDUAL(regCodePageAutomatico_DUAL_DarumaFramework("1"), self)
        pass


    def on_actionDesabilitarCodePageAutomatico_triggered(self):
        #tratarRetornoDUAL(regCodePageAutomatico_DUAL_DarumaFramework("0"), self)
        pass

    def on_actionHabilitarZeroCortado_triggered(self):
        #tratarRetornoDUAL(regZeroCortado_DUAL_DarumaFramework("1"), self)
        pass


    def on_actionDesabilitarZeroCortado_triggered(self):
        #tratarRetornoDUAL(regZeroCortado_DUAL_DarumaFramework("0"), self)
        pass


    def on_actionExemplo_1_Buffer_triggered(self):
        '''
        iRetorno = 0
        char sTexto[200];memset(sTexto, 0, sizeof(sTexto))
        iImprimirTexto_DUAL_DarumaFramework("<tc>~</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e><b>CENTRO DE DANÇA FLASH</b></e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l></l><tc>~</tc>",0)
        iImprimirTexto_DUAL_DarumaFramework("Rua: XV de Novembro N 785 Centro SP BR",0)
        iImprimirTexto_DUAL_DarumaFramework("Fone: 6234-5678 Fax:6324-5678",0)
        iImprimirTexto_DUAL_DarumaFramework("Data: <dt></dt><tb><tb>Hora: <hr></hr>",0)
        strcat(sTexto,"Pedido:00069 Cliente:00013<l></l>")
        strcat(sTexto,"Atividades Escolhidas:<l></l>")
        strcat(sTexto,"SAMBA+BOLERO+FORRÓ<l></l>")
        strcat(sTexto,"Valor: 55,00<l></l>")
        strcat(sTexto,"Vencimento: 10-03-05<l></l>")
        strcat(sTexto,"o não pagamento implica no cancelamento da vaga<l></l>")
        strcat(sTexto,"Início dia 01 de Fevereiro as 17:30hr<l></l>")
        strcat(sTexto,"Venha Dançar!!!<l></l>")
        strcat(sTexto,"Samba,Bolero,Soltinho,Forró,Zouk<l></l>")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        memset(sTexto, 0, sizeof(sTexto))
        strcat(sTexto,"<bmp></bmp><ean8><w3>1234567</w3></ean8>")
        strcat(sTexto,"<upc-a><txt>12345678912</txt></upc-a>")
        strcat(sTexto,"<code39><txt>12345678A-B-Z*F-E-H*</txt></code39>")
        strcat(sTexto,"<code93><txt>12345678A-B-Z-F&</txt></code93>")
        strcat(sTexto,"<codabar><txt>12345678A$$</txt></codabar>")
        strcat(sTexto,"<code11><txt>1234567891234567</txt></code11>")
        strcat(sTexto,"<code128><txt>123456789123-A-B-*_%-&</txt></code128>")
        strcat(sTexto,"<msi><txt>1234567890</txt></msi>")
        strcat(sTexto,"<i2of5><txt>1234</txt></i2of5>")
        strcat(sTexto,"<s2of5><txt>12345678</txt></s2of5>")
        strcat(sTexto,"<bmp></bmp>")
        strcat(sTexto,"<ean13><cbv><w3><h70>123456789123</h70></w3></cbv></ean13><sl>05</sl>")
        strcat(sTexto,"<code39><w3><h120><txt>12345678A-B-Z*F-E-H*</txt></h120></w3></code39><sl>05</sl>")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        iImprimirTexto_DUAL_DarumaFramework("<ad>Obrigado.</ad>",0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<sl>3</sl><sn></sn>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass


    def on_actionExemplo_2_Tabula_o_triggered(self):
        '''
        iRetorno = 0
        iImprimirTexto_UAL_DarumaFramework("<tb><b>FRAB<tb>Ano<tb>Modelo<tb>Valor<tb>Cor</b>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>GM<tb>2000<tb>Corsa<tb>12.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Ford<tb>2005<tb>Fiesta<tb>14.000<tb>Verde",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Fiat<tb>1998<tb>Uno Mille<tb>9.000<tb>Branco",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>GM<tb>1997<tb>Vectra<tb>18.000<tb>Prata",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>GM<tb>1999<tb>Tigra<tb>17.000<tb>Verde",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Ford<tb>2001<tb>Versalhes<tb>5.000<tb>Vinho",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>GM<tb>1998<tb>Corsa<tb>10.000<tb>Preto",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Fiat<tb>1996<tb>Fiurino<tb>6.000<tb>Branca",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>WV<tb>1979<tb>Fusca<tb>3.000<tb>Bordo",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>GM<tb>1996<tb>Vectra<tb>16.000<tb>Grafite",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Fiat<tb>1985<tb>Fiat147<tb>3.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Hond<tb>2003<tb>Civic<tb>28.000<tb>Preto",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Fiat<tb>1999<tb>Palio<tb>12.000<tb>Cinza",0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<tb>GM<tb>2003<tb>Celta<tb>17.000<tb>Branco<sl>7</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass


    def on_actionExemplo_3_Linha_a_Linha_triggered(self):
        '''
        iRetorno = 0
        iImprimirTexto_UAL_DarumaFramework("<tc>#</tc>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e><ce>ACADEMIA NEW SPORTS</ce></e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb><i>Rua Nossa Senhora da Luz</i>, 350",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb><i>Jardim Social   -   Curitiba   -  PR</i>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>CNPJ 04.888.968/0001-79<tb><e>234-5678<l></l></e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tc>#</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<i><dt></dt><i>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ad>Recibo nr.258963</ad><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Nome : </c><b>ELAINE MARIA</b><sp>5</sp>(545)<l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Plano : </c><b>MUSCULAÇÃO NOTURNO</b><sp>5</sp>(5)<l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>VALOR PAGO : 45,00</e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Ref. ao período de 03/04/2005 até 03/05/2005</c><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Obs: MENSALIDADE</c><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tc>_</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>WWW.ACADEMIANEW.COM.BR</e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tc>_</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>SAUDE BELEZA E BEM ESTAR</e></ce>",0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<sl>7</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass

    def on_actionExemplo_1_Buffer_2_triggered(self):
        '''
        iRetorno = 0
        char sTexto[200];memset(sTexto, 0, sizeof(sTexto))
        iImprimirTexto_DUAL_DarumaFramework("<tc>~</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<bmp></bmp>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e><b>CENTRO DE DANÇA</b></e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("ce><e><b>FLASH</b></e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l></l><tc>~</tc>",0)
        strcat(sTexto,"Rua: XV de Novembro N 785 Centro SP")
        strcat(sTexto,"Fone: 6234-5678 Fax:6324-5678")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        iImprimirTexto_DUAL_DarumaFramework("Data: <dt></dt><tb><tb>Hora:<hr></hr>",0)
        memset(sTexto, 0, sizeof(sTexto))
        strcat(sTexto,"Pedido:00069 Cliente:00013<l></l>")
        strcat(sTexto,"Atividades Escolhidas:<l></l>")
        strcat(sTexto,"SAMBA+BOLERO+FORRÓ<l></l>")
        strcat(sTexto,"Valor: 55,00<l></l>")
        strcat(sTexto,"Vencimento: 10-03-05<l></l>")
        strcat(sTexto,"o não pagamento implica no<l></l>")
        strcat(sTexto,"cancelamento da vaga<l></l>")
        strcat(sTexto,"Início dia 01 de Fevereiro - 17:30hr<l></l>")
        strcat(sTexto,"Venha Dançar!!!<l></l>")
        strcat(sTexto,"Samba,Bolero,Soltinho,Forró,Zouk<l></l>")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        memset(sTexto, 0, sizeof(sTexto))
        strcat(sTexto,"<ean8><w3>1234567</w3></ean8>")
        strcat(sTexto,"<upc-a><txt>12345678912</txt></upc-a>")
        strcat(sTexto,"<code39><txt>12345678A-B-Z*F-E-H*</txt></code39>")
        strcat(sTexto,"<code93><txt>12345678A-B-Z-F&</txt></code93>")
        strcat(sTexto,"<codabar><txt>12345678A$$</txt></codabar>")
        strcat(sTexto,"<code11><txt>1234567891234567</txt></code11>")
        strcat(sTexto,"<code128><txt>123456789123-A-B-*_%-&</txt></code128>")
        strcat(sTexto,"<msi><txt>1234567890</txt></msi>")
        strcat(sTexto,"<i2of5><txt>1234</txt></i2of5>")
        strcat(sTexto,"<s2of5><txt>12345678</txt></s2of5>")
        strcat(sTexto,"<ean13><cbv><w3><h70>123456789123</h70></w3></cbv></ean13>")
        strcat(sTexto,"<code39><w3><h120><txt>12345678A-B-Z*F-E-H*</txt></h120></w3></code39><sl>05</sl>")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<sl>3</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass


    def on_actionExemplo_2_Tabula_ao_triggered(self):
        '''
        iRetorno = 0
        iImprimirTexto_UAL_DarumaFramework("<b>FABR<tb>Ano<tb>Modelo<tb>Valor<tb>Cor",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>2000<tb>Corsa<tb>12.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Ford<tb>2005<tb>Fiesta<tb>14.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1998<tb>Uno<tb>9.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1997<tb>Vectra<tb>18.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1999<tb>Tigra<tb>17.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Ford<tb>2001<tb>Ka<tb>5.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1998<tb>Corsa<tb>10.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1996<tb>Fiurino<tb>6.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("WV<tb>1979<tb>Fusca<tb>3.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1996<tb>Vectra<tb>16.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1985<tb>Fiat147<tb>3.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Hond<tb>2003<tb>Civic<tb>28.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1999<tb>Palio<tb>12.000<tb>Azul",0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("GM<tb>2003<tb>Celta<tb>17.000<tb>Azul<sl>7</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass


    def on_actionExemplo_3_Linha_a_Linha_2_triggered(self):
        '''
        iRetorno=0
        iImprimirText_DUAL_DarumaFramework("<tc>#</tc>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e>  ACADEMIA NEW</e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e>    SPORTS</e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb><i>Rua Nossa Sra. da Luz</i>, 350",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb><i>Jardim Social - Curitiba - PR</i>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>CNPJ 04.888.968/0001-79<l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tc>#</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<i><dt></dt><i>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb>Recibo nr.258963<l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Nome : </c><b>ELAINE MARIA</b><sp>5</sp>(545)<l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Plano : </c><b>MUSCULAÇÃO NOTURNO</b><sp>5</sp>(5)<l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>VALOR PAGO : 45,00</e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Ref. ao período de 03/04/012 a 03/05/012</c><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>Obs: MENSALIDADE</c><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tc>_</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>WWW.ACADEMIA.COM</e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tc>_</tc><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>SAUDE BELEZA E</e></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><e>BEM ESTAR</e></ce>",0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<sl>7</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass


    def on_actionTeste_Completo_em_Buffer_triggered(self):
        '''
        char sTexto[2000];memset(sTexto, 0, sizeof(sTexto)
        iImprimirTexto_DUAL_DarumaFramework("<e><b>BUFFER COMPLETO</e></b><l></l>",0)
        strcat(sTexto,"<e>DATA:<dt></dt></e><l></l><e>Hora:<hr></hr></e><l></l>")
        strcat(sTexto,"<ce>Avançando 5 Linhas</ce><sl>5</sl>Inserindo<sp>5</sp>5 espaços em Branco<sl>2</sl>")
        strcat(sTexto,"<ce>Formatação Normal</ce><l></l>DARUMA AUTOMAÇÃO!!<sl>2</sl><ce>Negr+Ital+Subl+Expand</ce><l></l>")
        strcat(sTexto,"<b><i><s><e>DARUMA AUTOMAÇÃO!!</b></i></s></e><sl>2</sl><ce>Negr+Ital+Subl+Condensado</ce><l></l>")
        strcat(sTexto,"<b><i><s><c>DARUMA AUTOMAÇÃO!!</b></i></s></c><sl>2</sl><ce>Negr+Ital+Subl+Normal</ce><l></l>")
        strcat(sTexto,"<b><i><s><n>DARUMA AUTOMAÇÃO!!</b></i></s></n><sl>2</sl><ce>Expandido</ce><l></l>")
        strcat(sTexto,"<e>DARUMA AUTOMAÇÃO!!</e><sl>2</sl><ce>Condensado</ce><l></l>")
        strcat(sTexto,"<c>DARUMA AUTOMAÇÃO!!</c><sl>2</sl><ce>Negrito+Expandido</ce><l></l>")
        strcat(sTexto,"<b><e>DARUMA AUTOMAÇÃO!!</b></e><sl>2</sl><ce>Itálico+Expandido</ce><l></l>")
        strcat(sTexto,"<i><e>DARUMA AUTOMAÇÃO!!</i></e><sl>2</sl><ce>Sublinhado+Expandido</ce><l></l>")
        strcat(sTexto,"<s><e>DARUMA AUTOMAÇÃO!!</s></e><sl>2</sl><ce>Negrito+Condensado</ce><l></l>")
        strcat(sTexto,"<b><c>DARUMA AUTOMAÇÃO!!</b></c><sl>2</sl><ce>Itálico+Condensado</ce><l></l>")
        strcat(sTexto,"<i><c>DARUMA AUTOMAÇÃO!!</i></c><sl>2</sl><ce>Sublinhado+Condensado</ce><l></l>")
        strcat(sTexto,"<s><c>DARUMA AUTOMAÇÃO!!</s></c><sl>2</sl><ce>Negrito+Normal</ce><l></l>")
        strcat(sTexto,"<b><n>DARUMA AUTOMAÇÃO!!</n></b><l></l>")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        iImprimirTexto_DUAL_DarumaFramework("<e><b>FIM BUFFER COMPLETO</b></e><sl>03</sl>",0)
        iImprimirTexto_DUAL_DarumaFramework("<sl>03</sl>",0)
        trataRetornoDUAL(iImprimirTexto_DUAL_DarumaFramework("<gui></gui>",0), self)
        '''
        pass


    def on_actionTeste_Completo_Linha_a_Linha_triggered(self):
        '''
        iRetorno = 0
        iImprimirTexto_UAL_DarumaFramework("<sn><l><ce><s>Teste com Formatação DHTM</s></ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<n>Estes são os carácteres que<l> você poderá utilizar<n><l>Você poderá a qualquer momento<l> combinar as formatações!!",0)
        iImprimirTexto_DUAL_DarumaFramework("<<b>><</b>> Para sinalizar Negrito",0)
        iImprimirTexto_DUAL_DarumaFramework("<<i>><</i>> Para sinalizar Itálico",0)
        iImprimirTexto_DUAL_DarumaFramework("<<s>><</s>> Para sinalizar Sublinhado",0)
        iImprimirTexto_DUAL_DarumaFramework("<<e>><</e>> Para sinalizar Expandido",0)
        iImprimirTexto_DUAL_DarumaFramework("<<c>><</c>> Para sinalizar Condensado",0)
        iImprimirTexto_DUAL_DarumaFramework("<<n>><</n>> Para sinalizar Normal",0)
        iImprimirTexto_DUAL_DarumaFramework("<<l>><</l>> Para Saltar Uma Linha",0)
        iImprimirTexto_DUAL_DarumaFramework("<<fe>><</fe>> Ativa o Modo fonte Elite",0)
        iImprimirTexto_DUAL_DarumaFramework("<<ad>><</ad>> Para alinhar a direita",0)
        iImprimirTexto_DUAL_DarumaFramework("<<ft>>n1,..,n6<</ft>> Habilitar tabulação",0)
        iImprimirTexto_DUAL_DarumaFramework("<<tb>><</tb>>Saltar até proxima tabulação",0)
        iImprimirTexto_DUAL_DarumaFramework("<<sl>>NN<</sl>> Saltar Várias Linhas",0)
        iImprimirTexto_DUAL_DarumaFramework("<<tc>>C<</tc>>Riscar Linha<l> com Carácter Específico",0)
        iImprimirTexto_DUAL_DarumaFramework("<<ce>><</ce>> Para Centralizar",0)
        iImprimirTexto_DUAL_DarumaFramework("<<dt>><</dt>> Para Imprimir Data Atual",0)
        iImprimirTexto_DUAL_DarumaFramework("<<hr>><</hr>> Para Imprimir Hora Atual",0)
        iImprimirTexto_DUAL_DarumaFramework("<<sp>>NN<</sp>> Inserir NN Espaços<l> em Branco",0)
        iImprimirTexto_DUAL_DarumaFramework("<<sn>><</sn>> Sinal Sonoro, Apitar",0)
        iImprimirTexto_DUAL_DarumaFramework("<<g>><</g>> Abre a Gaveta",0)
        iImprimirTexto_DUAL_DarumaFramework("<<a>><</a>> Aguardar Término da Impressão",0)
        iImprimirTexto_DUAL_DarumaFramework("<l><tc>_</tc><tc>_</tc>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e><ce>TABULAÇÃO</ce><e><l></l><tc>_</tc>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b>FABR<tb>Ano<tb>Modelo<tb>Valor<tb>Cor</b>",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>2000<tb>Corsa<tb>12.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Ford<tb>2005<tb>Fiesta<tb>14.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1998<tb>Uno<tb>9.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1997<tb>Vectra<tb>18.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1999<tb>Tigra<tb>17.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Ford<tb>2001<tb>Ka<tb>5.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1998<tb>Corsa<tb>10.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1996<tb>Fiurino<tb>6.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("WV<tb>1979<tb>Fusca<tb>3.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>1996<tb>Vectra<tb>16.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1985<tb>Fiat147<tb>3.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Hond<tb>2003<tb>Civic<tb>28.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("Fiat<tb>1999<tb>Palio<tb>12.000<tb>Azul",0)
        iImprimirTexto_DUAL_DarumaFramework("GM<tb>2003<tb>Celta<tb>17.000<tb>Azul<sl>7</sl>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l><tc>_</tc>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l></l><e>DATA:<dt></dt></e><l></l><e>Hora:<hr></hr></e><l></l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>Anvançando 3 Linhas</ce><sl>3</sl>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>Anvançando 1 Linha</ce><sl>1</sl>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l>Inserindo<sp>5</sp>5 espaços em Branco",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>Formatação Normal</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<n>DARUMA AUTOMAÇÃO!!</n><l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>NEGR+ITAL+SUBL+EXPAND</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b><i><s><e>DARUMA AUTOMAÇÃO!!</b></i></s></e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>NEGR+ITAL+SUBL+CONDENSADO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b><i><s><c>DARUMA AUTOMAÇÃO!!</b></i></s></c>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>NEGR+ITAL+SUBL+NORMAL</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b><i><s><n>DARUMA AUTOMAÇÃO!!</b></i></s></n>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>EXPANDIDO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e>DARUMA AUTOMAÇÃO!!<e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>CONDENSADO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<c>DARUMA AUTOMAÇÃO!!</c>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>NEGRITO+EXPANDIDO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b><e>DARUMA AUTOMAÇÃO!!</b></e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>ITÁLICO+EXPANDIDO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<i><e>DARUMA AUTOMAÇÃO!!</i></e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce><dt></dt>SUBLINHADO+EXPANDIDO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<s><e>DARUMA AUTOMAÇÃO!!</s></e>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>NEGRITO+CONDENSADO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b><c>DARUMA AUTOMAÇÃO!!</b></c>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>ITÁLICO+CONDENSADO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<i><c>DARUMA AUTOMAÇÃO!!</i></c>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>SUBLINHADO+CONDENSADO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<s><c>DARUMA AUTOMAÇÃO!!</s></c>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>NEGRITO+NORMAL</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<b><n>DARUMA AUTOMAÇÃO!!</b></n>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>ITÁLICO+NORMAL</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l><i><n>DARUMA AUTOMAÇÃO!!</i></n>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>SUBLINHADO+NORMAL</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<s><n>DARUMA AUTOMAÇÃO!!</s></n><l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>ALINHADO A DIREITA</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ad>DARUMA</ad><l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>CENTRALIZADO + EXPANDIDO</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<e><ce>DARUMA!!</ce></e><l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ft>05,10,15,20,30,40</ft>",0)
        iImprimirTexto_DUAL_DarumaFramework("<ce>TABULADO NA COLUNA 10</ce>",0)
        iImprimirTexto_DUAL_DarumaFramework("<tb></tb><tb></tb>DARUMA<l>",0)
        iImprimirTexto_DUAL_DarumaFramework("<l><e><b>FIM TAGS COMPLETO</e></b>",0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<sl>03</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass


    def on_actionExemplo_4_Formulario_triggered(self):
        '''
        iRetorno = 0
        char sTexto[200];memset(sTexto, 0, sizeof(sTexto))
        iImprimirTexto_DUAL_DarumaFramework("<sp>4</sp>Nome da Empresa:Daruma Developers Community",0)
        strcat(sTexto,"<ce><tc>-</tc></ce><l></l>")
        strcat(sTexto,"<sp>4</sp>Endereço:<i>Avenida Paulista, 1776 - 16ºAndar</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Fones:<i>11-31464900</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Pedido Nº:<i>0541</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Data:<i><dt></dt></i><l></l>")
        strcat(sTexto,"<ce><tc>-</tc></ce><l></l>")
        strcat(sTexto,"<sp>4</sp>Tema Mensagem:<i>Desenvolvimento</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Titulo Mensagem:<i>Exemplo Qt</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Valor Mensagem:<i>5,00</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Forma Cobranca:<i>Boleto</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Cliente:<i>Sucesso Beatriz Silva</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Fone Res:<i>11-31464900</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Celular:<i>99239281</i><l></l>")
        strcat(sTexto,"<sp>4</sp>Fone Com:<i>11-31464900</i><sl>1</sl><l></l>")
        strcat(sTexto,"<ce><b>Mensagem Promo:Agradecemos a Preferência!!<l></l>(www.desenvolvedoresdaruma.com.br)</b></ce><sl>2</sl><l></l>")
        strcat(sTexto,"<sp>35</sp>Hora:<hr></hr><l></l>")
        iImprimirTexto_DUAL_DarumaFramework(sTexto,0)
        iRetorno = iImprimirTexto_DUAL_DarumaFramework("<e><tc>-</tc></ce><sl>7</sl>",0)
        trataRetornoDUAL(iRetorno,this)
        '''
        pass

    def on_actionM_todo_regVelocidade_DUAL_DarumaFramework_triggered(self):
        self.form_dual_regvelocidade=Ui_ui_dual_regvelocidade()
        self.form_dual_regvelocidade.show()

    def on_actionM_todo_regTabulacao_DUAL_DarumaFramework_triggered(self):
        self.form_dual_regtabulacao=Ui_ui_dual_regtabulacao()
        self.form_dual_regtabulacao.show()


    def on_actionM_todo_regPortaComunicacao_DUAL_DarumaFramework_triggered(self):
        self.form_dual_regportacomunicacao = Ui_ui_dual_regportacomunicacao()
        self.form_dual_regportacomunicacao.show()

    def on_actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework_triggered(self):
        self.form_dual_reglinhasguilhotina = Ui_ui_dual_reglinhasguilhotina()
        self.form_dual_reglinhasguilhotina.show()

    def on_actionM_todo_rStatusImpressora_DUAL_DarumaFramework_triggered(self):
        #tratarRetornoDUAL(rStatusImpressora_DUAL_DarumaFramework(), self)
        pass


    def on_actionM_todo_rStatusDocumento_DUAL_DarumaFramework_triggered(self):
        #tratarRetornoDUAL(rStatusDocumento_DUAL_DarumaFramework(), self)
        pass


    def on_actionM_todo_rStatusGaveta_DUAL_DarumaFramework_triggered(self):
        #gavetaStatus = 0
        #tratarRetornoDUAL(rSatusGaveta_DUAL_DarumaFramework(&gavetaStatus), self)

        #/* ***Converte o char Retorno para QString, para poder ser transferido para o QMessageBox*** */
        #QString StrgavetaStatus; StrgavetaStatus.append(QString("%1").arg(gavetaStatus))

        #/* ***Devolve o retorno da DLL para o campo de texto*** */
        #QMessageBox::information(this,"DarumaFramework - Qt C++","Status: "+StrgavetaStatus)
        pass

    def on_actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework_triggered(self):
        self.form_dual_rconsultastatusimpressora = Ui_ui_dual_rconsultastatusimpressora()
        self.form_dual_rconsultastatusimpressora.show()

    def on_actionTeste_para_Looping_de_verica_o_de_Status_triggered(self):
        self.form_dual_loopingdestatus = Ui_ui_dual_loopingdestatus()
        self.form_dual_loopingdestatus.show()

    def on_actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento_triggered(self):
        self.form_dual_loopingstatusdocumento = Ui_ui_dual_loopingstatusdocumento()
        self.form_dual_loopingstatusdocumento.show()

    def on_actionM_todo_iEnviarBMP_DUAL_DarumaFramework_triggered(self):
        self.form_dual_ienviarbmp = Ui_ui_dual_ienviarbmp()
        self.form_dual_ienviarbmp.show()

    def on_actionM_todo_iAcionarGaveta_DUAL_DarumaFramework_triggered(self):
        #tratarRetornoDUAL(iAcionarGaveta_DUAL_DarumaFramework(), self)
        pass

    def on_actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework_triggered(self):
        self.form_dual_iautenticardocumento = Ui_ui_dual_iautenticardocumento()
        self.form_dual_iautenticardocumento.show()

    def on_actionM_todo_iImprimirArquivo_DUAL_DarumaFramework_triggered(self):
        self.form_dual_iimprimirarquivo = Ui_ui_dual_iimprimirarquivo()
        self.form_dual_iimprimirarquivo.show()

    def on_actionM_todo_iImprimirTexto_DUAL_DarumaFramework_triggered(self):
        self.form_dual_iimprimirtexto = Ui_ui_dual_iimprimirtexto()
        self.form_dual_iimprimirtexto.show()

    #// *** FIM *** //
    #/* ****** MENU DUAL ******* */

    def on_pushButtonEncerrar_clicked(self):
        self.close()

    def on_pushButtonContatos_clicked(self):
        self.form_Geral_ContatosSuporte = Ui_ui_Geral_ContatosSuporte
        self.form_Geral_ContatosSuporte.show()

    def setupUi(self, MainWindowDual):
        MainWindowDual.setObjectName("MainWindowDual")
        MainWindowDual.resize(1037, 629)
        self.centralwidget = QtGui.QWidget(MainWindowDual)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 383, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 132))
        font = QtGui.QFont()
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(693, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(693, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButtonContatos_2 = QtGui.QPushButton(self.frame_2)
        self.pushButtonContatos_2.setMinimumSize(QtCore.QSize(191, 101))
        self.pushButtonContatos_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonContatos_2.setStyleSheet("background-image: url(:/Recursos/Imagens/avatar.png);")
        self.pushButtonContatos_2.setText("")
        self.pushButtonContatos_2.setObjectName("pushButtonContatos_2")
        self.horizontalLayout_2.addWidget(self.pushButtonContatos_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtGui.QSpacerItem(1178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButtonEncerrar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEncerrar.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButtonEncerrar.setObjectName("pushButtonEncerrar")
        self.horizontalLayout_3.addWidget(self.pushButtonEncerrar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindowDual.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowDual)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 18))
        self.menubar.setObjectName("menubar")
        self.menuM_todos_para_DarumaFramework = QtGui.QMenu(self.menubar)
        self.menuM_todos_para_DarumaFramework.setObjectName("menuM_todos_para_DarumaFramework")
        self.menuM_todos_para_Registro_Registry = QtGui.QMenu(self.menubar)
        self.menuM_todos_para_Registro_Registry.setObjectName("menuM_todos_para_Registro_Registry")
        self.menuM_todo_regAguardarProcesso_DUAL_DarumaFramework = QtGui.QMenu(self.menuM_todos_para_Registro_Registry)
        self.menuM_todo_regAguardarProcesso_DUAL_DarumaFramework.setObjectName("menuM_todo_regAguardarProcesso_DUAL_DarumaFramework")
        self.menuM_todo_regEnterFinal_DUAL_DarumaFramework = QtGui.QMenu(self.menuM_todos_para_Registro_Registry)
        self.menuM_todo_regEnterFinal_DUAL_DarumaFramework.setObjectName("menuM_todo_regEnterFinal_DUAL_DarumaFramework")
        self.menuM_todo_regModoGaveta_DUAL_DarumaFramework = QtGui.QMenu(self.menuM_todos_para_Registro_Registry)
        self.menuM_todo_regModoGaveta_DUAL_DarumaFramework.setObjectName("menuM_todo_regModoGaveta_DUAL_DarumaFramework")
        self.menuM_todo_regTermica_DUAL_DarumaFramework = QtGui.QMenu(self.menuM_todos_para_Registro_Registry)
        self.menuM_todo_regTermica_DUAL_DarumaFramework.setObjectName("menuM_todo_regTermica_DUAL_DarumaFramework")
        self.menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework = QtGui.QMenu(self.menuM_todos_para_Registro_Registry)
        self.menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework.setObjectName("menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework")
        self.menuM_todo_regZeroCortado_DUAL_DarumaFramework = QtGui.QMenu(self.menuM_todos_para_Registro_Registry)
        self.menuM_todo_regZeroCortado_DUAL_DarumaFramework.setObjectName("menuM_todo_regZeroCortado_DUAL_DarumaFramework")
        self.menuM_todos_para_Status_e_Testes = QtGui.QMenu(self.menubar)
        self.menuM_todos_para_Status_e_Testes.setObjectName("menuM_todos_para_Status_e_Testes")
        self.menuMenu_para_Testes = QtGui.QMenu(self.menuM_todos_para_Status_e_Testes)
        self.menuMenu_para_Testes.setObjectName("menuMenu_para_Testes")
        self.menuM_todos_para_Autentica_ao_e_Impress_o = QtGui.QMenu(self.menubar)
        self.menuM_todos_para_Autentica_ao_e_Impress_o.setObjectName("menuM_todos_para_Autentica_ao_e_Impress_o")
        self.menuExemplos = QtGui.QMenu(self.menubar)
        self.menuExemplos.setObjectName("menuExemplos")
        self.menuBobina_35_Colunas = QtGui.QMenu(self.menubar)
        self.menuBobina_35_Colunas.setObjectName("menuBobina_35_Colunas")
        MainWindowDual.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowDual)
        self.statusbar.setObjectName("statusbar")
        MainWindowDual.setStatusBar(self.statusbar)
        self.actionM_todo_eDefinirProduto_Daruma = QtGui.QAction(MainWindowDual)
        self.actionM_todo_eDefinirProduto_Daruma.setObjectName("actionM_todo_eDefinirProduto_Daruma")
        self.actionM_todo_regRetornaValorChave_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_regRetornaValorChave_DarumaFramework.setObjectName("actionM_todo_regRetornaValorChave_DarumaFramework")
        self.actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework.setObjectName("actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework")
        self.actionM_todo_regPortaComunicacao_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_regPortaComunicacao_DUAL_DarumaFramework.setObjectName("actionM_todo_regPortaComunicacao_DUAL_DarumaFramework")
        self.actionM_todo_regTabulacao_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_regTabulacao_DUAL_DarumaFramework.setObjectName("actionM_todo_regTabulacao_DUAL_DarumaFramework")
        self.actionM_todo_regVelocidade_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_regVelocidade_DUAL_DarumaFramework.setObjectName("actionM_todo_regVelocidade_DUAL_DarumaFramework")
        self.action1_Habilitar = QtGui.QAction(MainWindowDual)
        self.action1_Habilitar.setObjectName("action1_Habilitar")
        self.actionHabilitarAguardarProcesso = QtGui.QAction(MainWindowDual)
        self.actionHabilitarAguardarProcesso.setObjectName("actionHabilitarAguardarProcesso")
        self.actionDesabilitarAguardarProcesso = QtGui.QAction(MainWindowDual)
        self.actionDesabilitarAguardarProcesso.setObjectName("actionDesabilitarAguardarProcesso")
        self.actionHabilitarEnterFinal = QtGui.QAction(MainWindowDual)
        self.actionHabilitarEnterFinal.setObjectName("actionHabilitarEnterFinal")
        self.actionDesabilitarEnterFinal = QtGui.QAction(MainWindowDual)
        self.actionDesabilitarEnterFinal.setObjectName("actionDesabilitarEnterFinal")
        self.actionPadraoGaveta = QtGui.QAction(MainWindowDual)
        self.actionPadraoGaveta.setObjectName("actionPadraoGaveta")
        self.actionAlteraPadraoGaveta = QtGui.QAction(MainWindowDual)
        self.actionAlteraPadraoGaveta.setObjectName("actionAlteraPadraoGaveta")
        self.actionHabilitarTermica = QtGui.QAction(MainWindowDual)
        self.actionHabilitarTermica.setObjectName("actionHabilitarTermica")
        self.actionDesabilitarTermica = QtGui.QAction(MainWindowDual)
        self.actionDesabilitarTermica.setObjectName("actionDesabilitarTermica")
        self.actionHabilitarCodePageAutomatico = QtGui.QAction(MainWindowDual)
        self.actionHabilitarCodePageAutomatico.setObjectName("actionHabilitarCodePageAutomatico")
        self.actionDesabilitarCodePageAutomatico = QtGui.QAction(MainWindowDual)
        self.actionDesabilitarCodePageAutomatico.setObjectName("actionDesabilitarCodePageAutomatico")
        self.actionHabilitarZeroCortado = QtGui.QAction(MainWindowDual)
        self.actionHabilitarZeroCortado.setObjectName("actionHabilitarZeroCortado")
        self.actionDesabilitarZeroCortado = QtGui.QAction(MainWindowDual)
        self.actionDesabilitarZeroCortado.setObjectName("actionDesabilitarZeroCortado")
        self.actionM_todo_rStatusImpressora_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_rStatusImpressora_DUAL_DarumaFramework.setObjectName("actionM_todo_rStatusImpressora_DUAL_DarumaFramework")
        self.actionM_todo_rStatusDocumento_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_rStatusDocumento_DUAL_DarumaFramework.setObjectName("actionM_todo_rStatusDocumento_DUAL_DarumaFramework")
        self.actionM_todo_rStatusGaveta_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_rStatusGaveta_DUAL_DarumaFramework.setObjectName("actionM_todo_rStatusGaveta_DUAL_DarumaFramework")
        self.actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework.setObjectName("actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework")
        self.actionTeste_para_Looping_de_verica_o_de_Status = QtGui.QAction(MainWindowDual)
        self.actionTeste_para_Looping_de_verica_o_de_Status.setObjectName("actionTeste_para_Looping_de_verica_o_de_Status")
        self.actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento = QtGui.QAction(MainWindowDual)
        self.actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento.setObjectName("actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento")
        self.actionM_todo_iImprimirTexto_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_iImprimirTexto_DUAL_DarumaFramework.setObjectName("actionM_todo_iImprimirTexto_DUAL_DarumaFramework")
        self.actionM_todo_iImprimirArquivo_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_iImprimirArquivo_DUAL_DarumaFramework.setObjectName("actionM_todo_iImprimirArquivo_DUAL_DarumaFramework")
        self.actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework.setObjectName("actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework")
        self.actionM_todo_iAcionarGaveta_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_iAcionarGaveta_DUAL_DarumaFramework.setObjectName("actionM_todo_iAcionarGaveta_DUAL_DarumaFramework")
        self.actionM_todo_iEnviarBMP_DUAL_DarumaFramework = QtGui.QAction(MainWindowDual)
        self.actionM_todo_iEnviarBMP_DUAL_DarumaFramework.setObjectName("actionM_todo_iEnviarBMP_DUAL_DarumaFramework")
        self.actionExemplo_1_Buffer = QtGui.QAction(MainWindowDual)
        self.actionExemplo_1_Buffer.setObjectName("actionExemplo_1_Buffer")
        self.actionExemplo_2_Tabula_o = QtGui.QAction(MainWindowDual)
        self.actionExemplo_2_Tabula_o.setObjectName("actionExemplo_2_Tabula_o")
        self.actionExemplo_3_Linha_a_Linha = QtGui.QAction(MainWindowDual)
        self.actionExemplo_3_Linha_a_Linha.setObjectName("actionExemplo_3_Linha_a_Linha")
        self.actionExemplo_4_Formulario = QtGui.QAction(MainWindowDual)
        self.actionExemplo_4_Formulario.setObjectName("actionExemplo_4_Formulario")
        self.actionExemplo_1_Buffer_2 = QtGui.QAction(MainWindowDual)
        self.actionExemplo_1_Buffer_2.setObjectName("actionExemplo_1_Buffer_2")
        self.actionExemplo_2_Tabula_ao = QtGui.QAction(MainWindowDual)
        self.actionExemplo_2_Tabula_ao.setObjectName("actionExemplo_2_Tabula_ao")
        self.actionExemplo_3_Linha_a_Linha_2 = QtGui.QAction(MainWindowDual)
        self.actionExemplo_3_Linha_a_Linha_2.setObjectName("actionExemplo_3_Linha_a_Linha_2")
        self.actionTeste_Completo_em_Buffer = QtGui.QAction(MainWindowDual)
        self.actionTeste_Completo_em_Buffer.setObjectName("actionTeste_Completo_em_Buffer")
        self.actionTeste_Completo_Linha_a_Linha = QtGui.QAction(MainWindowDual)
        self.actionTeste_Completo_Linha_a_Linha.setObjectName("actionTeste_Completo_Linha_a_Linha")
        self.menuM_todos_para_DarumaFramework.addAction(self.actionM_todo_eDefinirProduto_Daruma)
        self.menuM_todos_para_DarumaFramework.addAction(self.actionM_todo_regRetornaValorChave_DarumaFramework)
        self.menuM_todo_regAguardarProcesso_DUAL_DarumaFramework.addAction(self.actionHabilitarAguardarProcesso)
        self.menuM_todo_regAguardarProcesso_DUAL_DarumaFramework.addAction(self.actionDesabilitarAguardarProcesso)
        self.menuM_todo_regEnterFinal_DUAL_DarumaFramework.addAction(self.actionHabilitarEnterFinal)
        self.menuM_todo_regEnterFinal_DUAL_DarumaFramework.addAction(self.actionDesabilitarEnterFinal)
        self.menuM_todo_regModoGaveta_DUAL_DarumaFramework.addAction(self.actionPadraoGaveta)
        self.menuM_todo_regModoGaveta_DUAL_DarumaFramework.addAction(self.actionAlteraPadraoGaveta)
        self.menuM_todo_regTermica_DUAL_DarumaFramework.addAction(self.actionHabilitarTermica)
        self.menuM_todo_regTermica_DUAL_DarumaFramework.addAction(self.actionDesabilitarTermica)
        self.menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework.addAction(self.actionHabilitarCodePageAutomatico)
        self.menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework.addAction(self.actionDesabilitarCodePageAutomatico)
        self.menuM_todo_regZeroCortado_DUAL_DarumaFramework.addAction(self.actionHabilitarZeroCortado)
        self.menuM_todo_regZeroCortado_DUAL_DarumaFramework.addAction(self.actionDesabilitarZeroCortado)
        self.menuM_todos_para_Registro_Registry.addAction(self.menuM_todo_regAguardarProcesso_DUAL_DarumaFramework.menuAction())
        self.menuM_todos_para_Registro_Registry.addAction(self.menuM_todo_regEnterFinal_DUAL_DarumaFramework.menuAction())
        self.menuM_todos_para_Registro_Registry.addAction(self.actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework)
        self.menuM_todos_para_Registro_Registry.addAction(self.menuM_todo_regModoGaveta_DUAL_DarumaFramework.menuAction())
        self.menuM_todos_para_Registro_Registry.addAction(self.actionM_todo_regPortaComunicacao_DUAL_DarumaFramework)
        self.menuM_todos_para_Registro_Registry.addAction(self.actionM_todo_regTabulacao_DUAL_DarumaFramework)
        self.menuM_todos_para_Registro_Registry.addAction(self.menuM_todo_regTermica_DUAL_DarumaFramework.menuAction())
        self.menuM_todos_para_Registro_Registry.addAction(self.actionM_todo_regVelocidade_DUAL_DarumaFramework)
        self.menuM_todos_para_Registro_Registry.addAction(self.menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework.menuAction())
        self.menuM_todos_para_Registro_Registry.addAction(self.menuM_todo_regZeroCortado_DUAL_DarumaFramework.menuAction())
        self.menuMenu_para_Testes.addAction(self.actionTeste_para_Looping_de_verica_o_de_Status)
        self.menuMenu_para_Testes.addAction(self.actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento)
        self.menuM_todos_para_Status_e_Testes.addAction(self.actionM_todo_rStatusImpressora_DUAL_DarumaFramework)
        self.menuM_todos_para_Status_e_Testes.addAction(self.actionM_todo_rStatusDocumento_DUAL_DarumaFramework)
        self.menuM_todos_para_Status_e_Testes.addAction(self.actionM_todo_rStatusGaveta_DUAL_DarumaFramework)
        self.menuM_todos_para_Status_e_Testes.addAction(self.actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework)
        self.menuM_todos_para_Status_e_Testes.addAction(self.menuMenu_para_Testes.menuAction())
        self.menuM_todos_para_Autentica_ao_e_Impress_o.addAction(self.actionM_todo_iImprimirTexto_DUAL_DarumaFramework)
        self.menuM_todos_para_Autentica_ao_e_Impress_o.addAction(self.actionM_todo_iImprimirArquivo_DUAL_DarumaFramework)
        self.menuM_todos_para_Autentica_ao_e_Impress_o.addAction(self.actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework)
        self.menuM_todos_para_Autentica_ao_e_Impress_o.addAction(self.actionM_todo_iAcionarGaveta_DUAL_DarumaFramework)
        self.menuM_todos_para_Autentica_ao_e_Impress_o.addAction(self.actionM_todo_iEnviarBMP_DUAL_DarumaFramework)
        self.menuExemplos.addAction(self.actionExemplo_1_Buffer)
        self.menuExemplos.addAction(self.actionExemplo_2_Tabula_o)
        self.menuExemplos.addAction(self.actionExemplo_3_Linha_a_Linha)
        self.menuExemplos.addAction(self.actionExemplo_4_Formulario)
        self.menuBobina_35_Colunas.addAction(self.actionExemplo_1_Buffer_2)
        self.menuBobina_35_Colunas.addAction(self.actionExemplo_2_Tabula_ao)
        self.menuBobina_35_Colunas.addAction(self.actionExemplo_3_Linha_a_Linha_2)
        self.menuBobina_35_Colunas.addAction(self.actionTeste_Completo_em_Buffer)
        self.menuBobina_35_Colunas.addAction(self.actionTeste_Completo_Linha_a_Linha)
        self.menubar.addAction(self.menuM_todos_para_DarumaFramework.menuAction())
        self.menubar.addAction(self.menuM_todos_para_Registro_Registry.menuAction())
        self.menubar.addAction(self.menuM_todos_para_Status_e_Testes.menuAction())
        self.menubar.addAction(self.menuM_todos_para_Autentica_ao_e_Impress_o.menuAction())
        self.menubar.addAction(self.menuExemplos.menuAction())
        self.menubar.addAction(self.menuBobina_35_Colunas.menuAction())

        self.retranslateUi(MainWindowDual)
        QtCore.QMetaObject.connectSlotsByName(MainWindowDual)

    def retranslateUi(self, MainWindowDual):
        MainWindowDual.setWindowTitle(QtGui.QApplication.translate("MainWindowDual", "DarumaFrameWork - Módulo DUAL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindowDual", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Dúvidas? Ligue: 0800 77 0332 0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindowDual", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Impressora Não Fiscal</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; font-weight:600;\">DLL: DarumaFramework.dll</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindowDual", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Recursos/Imagens/logo_daruma_developers.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEncerrar.setText(QtGui.QApplication.translate("MainWindowDual", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_para_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Métodos para DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_para_Registro_Registry.setTitle(QtGui.QApplication.translate("MainWindowDual", "Métodos para Registro(Registry)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regAguardarProcesso_DUAL_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Método regAguardarProcesso_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regEnterFinal_DUAL_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Método regEnterFinal_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regModoGaveta_DUAL_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Método regModoGaveta_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regTermica_DUAL_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Método regTermica_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regCodePageAutomatico_DUAL_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Método regCodePageAutomatico_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todo_regZeroCortado_DUAL_DarumaFramework.setTitle(QtGui.QApplication.translate("MainWindowDual", "Método regZeroCortado_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_para_Status_e_Testes.setTitle(QtGui.QApplication.translate("MainWindowDual", "Métodos para Status e Testes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu_para_Testes.setTitle(QtGui.QApplication.translate("MainWindowDual", "Menu para Testes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuM_todos_para_Autentica_ao_e_Impress_o.setTitle(QtGui.QApplication.translate("MainWindowDual", "Métodos para Autenticaçao e Impressão", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExemplos.setTitle(QtGui.QApplication.translate("MainWindowDual", "Exemplos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBobina_35_Colunas.setTitle(QtGui.QApplication.translate("MainWindowDual", "Bobina 35 Colunas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_eDefinirProduto_Daruma.setText(QtGui.QApplication.translate("MainWindowDual", "Método eDefinirProduto_Daruma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regRetornaValorChave_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método regRetornaValorChave_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regLinhasGuilhotina_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método regLinhasGuilhotina_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regPortaComunicacao_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método regPortaComunicacao_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regTabulacao_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método regTabulacao_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_regVelocidade_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método regVelocidade_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.action1_Habilitar.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarAguardarProcesso.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarAguardarProcesso.setText(QtGui.QApplication.translate("MainWindowDual", "0 - Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarEnterFinal.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarEnterFinal.setText(QtGui.QApplication.translate("MainWindowDual", "0 - Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPadraoGaveta.setText(QtGui.QApplication.translate("MainWindowDual", "0 - Padrão", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlteraPadraoGaveta.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Altera Padrão", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarTermica.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarTermica.setText(QtGui.QApplication.translate("MainWindowDual", "0 - Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarCodePageAutomatico.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarCodePageAutomatico.setText(QtGui.QApplication.translate("MainWindowDual", "0 - Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHabilitarZeroCortado.setText(QtGui.QApplication.translate("MainWindowDual", "1 - Habilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesabilitarZeroCortado.setText(QtGui.QApplication.translate("MainWindowDual", "0 - Desabilitar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusImpressora_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método rStatusImpressora_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusDocumento_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método rStatusDocumento_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rStatusGaveta_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método rStatusGaveta_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_rConsultaStatusImpressora_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método rConsultaStatusImpressora_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTeste_para_Looping_de_verica_o_de_Status.setText(QtGui.QApplication.translate("MainWindowDual", "Teste para Looping de verificação de Status", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTeste_para_Looping_de_verifica_ao_de_Status_de_Documento.setText(QtGui.QApplication.translate("MainWindowDual", "Teste para Looping de verificaçao de Status de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iImprimirTexto_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método iImprimirTexto_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iImprimirArquivo_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método iImprimirArquivo_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iAutenticarDocumento_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método iAutenticarDocumento_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iAcionarGaveta_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método iAcionarGaveta_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM_todo_iEnviarBMP_DUAL_DarumaFramework.setText(QtGui.QApplication.translate("MainWindowDual", "Método iEnviarBMP_DUAL_DarumaFramework", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_1_Buffer.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 1 (Buffer)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_2_Tabula_o.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 2 (Tabulação)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_3_Linha_a_Linha.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 3 (Linha-a-Linha)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_4_Formulario.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 4 (Formulário)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_1_Buffer_2.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 1 (Buffer)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_2_Tabula_ao.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 2 (Tabulação)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExemplo_3_Linha_a_Linha_2.setText(QtGui.QApplication.translate("MainWindowDual", "Exemplo 3 (Linha-a-Linha)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTeste_Completo_em_Buffer.setText(QtGui.QApplication.translate("MainWindowDual", "Teste Completo em Buffer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTeste_Completo_Linha_a_Linha.setText(QtGui.QApplication.translate("MainWindowDual", "Teste Completo Linha-a-Linha", None, QtGui.QApplication.UnicodeUTF8))

