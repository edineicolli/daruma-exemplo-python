from PySide.QtGui import QMessageBox

__author__ = 'Edinei'

def tratarRetornoDUAL(iRetorno, Janela):

    if (iRetorno == 0):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno 0 - Erro de comunicação, não foi possível enviar o método.")
    elif (iRetorno == 1):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno 1 - OK, Sucesso ao enviar o método.")
    elif (iRetorno == -99):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -99 - Método não executado, parâmetro inválido.")
    elif (iRetorno == -1):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -1 - Erro de atualização de Chave.")
    elif (iRetorno == -2):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -2 - Linhas e Colunas inválidas.")
    elif (iRetorno == -4):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -4 - A chave ou Valor no Arquivo do Registro(Registry) não foi encontada.")
    elif (iRetorno == -27):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -27 - Erro Genérico.")
    elif (iRetorno == -50):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -50 - Impressora OFF-LINE.")
    elif (iRetorno == -51):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -51 -  Impressora sem papel.")
    elif (iRetorno == -52):
        QMessageBox.information(Janela,"Tratamento de Retorno - DarumaFramework Qt","Retorno -52 -  Impressora inicializando.")