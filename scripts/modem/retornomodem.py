from PySide.QtGui import QMessageBox

__author__ = 'Edinei'

def tratarRetornoModem(iRetorno, Janela):

    if (iRetorno == 0):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno 0 - Erro de comunicação, não foi possível enviar o método."
    elif (iRetorno == 1):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno 1 - Operação realizada com sucesso!!"
    elif (iRetorno == -1):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -1 - Erro na comunicação da serial."
    elif (iRetorno == -2):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -2 - Modem retornou erro."
    elif (iRetorno == -3):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -3 - Modem retornou caractere(s) inválido(s)."
    elif (iRetorno == -4):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -4 - Modem não conectado na rede GSM."
    elif (iRetorno == -5):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -5 - Modem retornou NO CARRIER."
    elif (iRetorno == -6):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -6 - Modem retornou NO DIALTONE."
    elif (iRetorno == -7):
        QStrRetornoMetodo = "Tratamento de Retorno - DarumaFramework Qt C++","Retorno -7 - Modem retornou BUSY."

    if (iRetorno > 1):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt C++"," O nivel de sinal é: " + str(iRetorno));
    else:
        QMessageBox.information(Janela, "Tratamento Retorno - Genérico","Retorno do Método: " + QStrRetornoMetodo)

def tratarRetornoModemReg(iRetorno, Janela):

    if (iRetorno == 0):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt C++","Retorno 0 - Erro de comunicação, não foi possível enviar o método.")
    elif (iRetorno == 1):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt C++","Retorno 1 - Operação realizada com sucesso!!")
    elif (iRetorno == -1):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt C++","Retorno -1 - Erro de atualização de Chave.")