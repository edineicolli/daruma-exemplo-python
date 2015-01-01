from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import eRetornarAvisoErroUltimoCMD_ECF_Daruma, eInterpretarRetorno_ECF_Daruma

__author__ = 'Edinei'


def tratarRetornoFiscal(iRetorno, Janela):
    QStrMensagem = ''
    iRetornoLocal = iRetorno
    cInterpretaErro = b''
    cInterpretaAviso = b''
    cInterpretaRetorno = b''

    #ESTE MÉTODO VERIFICA O STATUS DO ULTIMO COMANDO, E INTERPRETA OS INDICES DE AVISO E ERRO.
    eRetornarAvisoErroUltimoCMD_ECF_Daruma(cInterpretaAviso,cInterpretaErro)
    eInterpretarRetorno_ECF_Daruma(iRetornoLocal, cInterpretaRetorno)

    QStrMensagem+="Retorno do Metodo: "
    QStrMensagem+=cInterpretaRetorno
    QStrMensagem+="\n"
    QStrMensagem+="Erro: "
    QStrMensagem+= cInterpretaErro
    QStrMensagem+="\n"
    QStrMensagem+="Aviso: "
    QStrMensagem+=cInterpretaAviso
    QStrMensagem+="\n"

    QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Python/Qt",QStrMensagem);
    return 0;