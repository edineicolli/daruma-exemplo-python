from PySide.QtGui import QMessageBox

__author__ = 'Edinei'

def tratarRetornoModem(iRetorno, Janela):

    RetornoMetodo = ''
    if (iRetorno == 0):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno 0 - Erro de comunicação, não foi possível enviar o método.'
    elif (iRetorno == 1):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno 1 - Operação realizada com sucesso!!'
    elif (iRetorno == -1):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -1 - Erro na comunicação da serial.'
    elif (iRetorno == -2):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -2 - Modem retornou erro.'
    elif (iRetorno == -3):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -3 - Modem retornou caractere(s) inválido(s).'
    elif (iRetorno == -4):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -4 - Modem não conectado na rede GSM.'
    elif (iRetorno == -5):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -5 - Modem retornou NO CARRIER.'
    elif (iRetorno == -6):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -6 - Modem retornou NO DIALTONE.'
    elif (iRetorno == -7):
        RetornoMetodo = 'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -7 - Modem retornou BUSY.'

    if (iRetorno > 1):
        QMessageBox.information(Janela,'Tratamento de Retorno - DarumaFramework Python/Qt',' O nivel de sinal é: ' + str(iRetorno));
    else:
        QMessageBox.information(Janela, 'Tratamento Retorno - Genérico','Retorno do Método: ' + str(RetornoMetodo))

def tratarRetornoModemReg(iRetorno, Janela):

    if (iRetorno == 0):
        QMessageBox.information(Janela,'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno 0 - Erro de comunicação, não foi possível enviar o método.')
    elif (iRetorno == 1):
        QMessageBox.information(Janela,'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno 1 - Operação realizada com sucesso!!')
    elif (iRetorno == -1):
        QMessageBox.information(Janela,'Tratamento de Retorno - DarumaFramework Python/Qt','Retorno -1 - Erro de atualização de Chave.')