__author__ = 'Edinei'
from PySide.QtGui import QMessageBox

__author__ = 'Edinei'

def tratarRetornoGenerico(iRetorno, Janela):

    if (iRetorno == 0):
        QStrRetornoMetodo = "[0] - Erro durante a execução"
    elif (iRetorno == 1):
        QStrRetornoMetodo = "[1] - Operação realizada com sucesso"
    elif (iRetorno == 3):
        QStrRetornoMetodo = "[3] - lebin.dll retornou período sem movimento"
    elif (iRetorno == -1):
        QStrRetornoMetodo = "[-1] - Erro do Método"
    elif (iRetorno == 2):
        QStrRetornoMetodo = "[-2] - Parâmetro incorreto"
    elif (iRetorno == -3):
        QStrRetornoMetodo = "[-3] - Alíquota (Situação tributária) não programada"
    elif (iRetorno == -4):
        QStrRetornoMetodo= "[-4] - Chave do Registry não encontrada"
    elif (iRetorno == -5):
        QStrRetornoMetodo= "[-5] - Erro ao Abrir a porta de Comunicação"
    elif (iRetorno == -6):
        QStrRetornoMetodo= "[-6] - Impressora Desligada"
    elif (iRetorno == -7):
        QStrRetornoMetodo= "[-7] - Erro no Número do Banco"
    elif (iRetorno == -8):
        QStrRetornoMetodo= "[-8] - Erro ao Gravar as informações no arquivo de Status ou de Retorno de Info"
    elif (iRetorno == -9):
        QStrRetornoMetodo= "[-9] - Erro ao Fechar a porta de Comunicação"
    elif (iRetorno == -10):
        QStrRetornoMetodo= "[-10] - Se o ECF não tem forma de pagamento e não permite cadastrar esta forma"
    elif (iRetorno == -12):
        QStrRetornoMetodo= "[-12] - A função executou o comando porém o ECF sinalizou Erro, chame a rStatusUltimoCmdInt_ECF_Daruma para identificar o Erro."
    elif (iRetorno == -24):
        QStrRetornoMetodo= "[-24] - Forma de Pagamento não Programada"
    elif (iRetorno == -25):
        QStrRetornoMetodo= "[-25] - Totalizador nao ECF Não Vinculado nao Programado"
    elif (iRetorno == -27):
        QStrRetornoMetodo= "[-27] - Foi Detectado Erro ou Warning na Impressora"
    elif (iRetorno == -28):
        QStrRetornoMetodo= "[-28] - Time-Out"
    elif (iRetorno == -40):
        QStrRetornoMetodo= "[-40] - Tag XML Inválida"
    elif (iRetorno == -50):
        QStrRetornoMetodo= "[-50] - Problemas ao Criar Chave no Registry"
    elif (iRetorno == -51):
        QStrRetornoMetodo= "[-51] - Erro ao Gravar LOG"
    elif (iRetorno == -52):
        QStrRetornoMetodo= "[-52] - Erro ao abrir arquivo"
    elif (iRetorno == -53):
        QStrRetornoMetodo= "[-53] - Fim de arquivo"
    elif (iRetorno == -60):
        QStrRetornoMetodo= "[-60] - Erro na tag de formatacao DHTML"
    elif (iRetorno == -90):
        QStrRetornoMetodo= "[-90] - Erro Configurar a Porta de Comunicação"
    elif (iRetorno == -99):
        QStrRetornoMetodo= "[-99] - Parâmetro inválido ou ponteiro nulo de parâmetro"
    elif (iRetorno == -101):
        QStrRetornoMetodo= "[-101] - Erro ao LER ou ESCREVER arquivo"
    elif (iRetorno == -102):
        QStrRetornoMetodo= "[-102] - Erro ao LER ou ESCREVER arquivo"
    elif (iRetorno == -103):
        QStrRetornoMetodo= "[-103] - Não foram encontradas as DDLs auxiliares (lebin.dll e LeituraMFDBin.dll"
    elif (iRetorno == -104):
        QStrRetornoMetodo= "[-104] - Data informada é inferior ao primeiro documento emitido"
    elif (iRetorno == -105):
        QStrRetornoMetodo= "[-105] - Data informada é maior que a última redução Z impressa"
    elif (iRetorno == -107):
        QStrRetornoMetodo= "[-107] - Deve-se fechar a porta atual (para abrir outra ou ao tentá-la abrir novamente)"
    else:
        QStrRetornoMetodo = "Indice Inválido"

    QMessageBox.information(Janela, "Tratamento Retorno - Genérico","Retorno do Método: " + QStrRetornoMetodo)