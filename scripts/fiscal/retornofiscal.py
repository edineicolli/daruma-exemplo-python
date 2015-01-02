from ctypes import create_string_buffer
from PySide.QtGui import QMessageBox
from pydaruma.pydaruma import eRetornarAvisoErroUltimoCMD_ECF_Daruma, eInterpretarRetorno_ECF_Daruma

__author__ = 'Edinei'


def tratarRetornoFiscal(iRetorno, Janela):
    QStrMensagem = ''
    iRetornoLocal = iRetorno
    cInterpretaErro = create_string_buffer(300)
    cInterpretaAviso = create_string_buffer(300)
    cInterpretaRetorno = create_string_buffer(200)

    #ESTE MÉTODO VERIFICA O STATUS DO ULTIMO COMANDO, E INTERPRETA OS INDICES DE AVISO E ERRO.
    eRetornarAvisoErroUltimoCMD_ECF_Daruma(bytes(cInterpretaAviso),bytes(cInterpretaErro))
    # bug report - python stop run
    #eInterpretarRetorno_ECF_Daruma(iRetornoLocal, bytes(cInterpretaRetorno))

    QStrMensagem+="Retorno do Metodo: "
    QStrMensagem+=cInterpretaRetorno.value.decode('latin-1')
    QStrMensagem+="\n"
    QStrMensagem+="Erro: "
    QStrMensagem+= cInterpretaErro.value.decode('latin-1')
    QStrMensagem+="\n"
    QStrMensagem+="Aviso: "
    QStrMensagem+=cInterpretaAviso.value.decode('latin-1')
    QStrMensagem+="\n"

    QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Python/Qt",QStrMensagem)
    return 0