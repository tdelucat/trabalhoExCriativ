#main do trabalho
from Bib import *
from dados_coletados import lista_respostas

matriz_para_modificacao = []
for item in lista_respostas:
    matriz_para_modificacao.append(list(item)) 

AtualizaMatrizScoreRisco(matriz_para_modificacao)

while True:
    indice = TelaAbertura() # Puxa a abertura de tela, fiz de forma exotica para diferenciar do normal de selecao, 1,2,3,4,5,6,0

    if indice == -1:
        print("Saindo...") #Sai quando, na tela inicial, o usuario escolhe o E
        break

    if indice == 0:
        SugereMinimizacaoSintomas() #Puxa a funcao nomeada, faz outra selecao parecida com a tela de abertura.
        
    if indice == 1:
        ImprimePessoaScoreRisco(matriz_para_modificacao) #puxa uma funcao que leva a pessoa a selecionar uma pessoa para saber seu Score e seu Risco
        
    if indice == 2:
        ImprimeMatrizScoreRisco(matriz_para_modificacao) #Imprime a matriz completa, de forma um pouco mais limpa

    if indice == 3:
        CalculaPercentual(matriz_para_modificacao,indice) #mostra o calculo de percentual de pessoas com baixo risco
        
    if indice == 4:
        CalculaPercentual(matriz_para_modificacao,indice) #mostra o calculo de percentual de pessoas com moderado risco
        
    if indice == 5:
        CalculaPercentual(matriz_para_modificacao,indice) #mostra o calculo de percentual de pessoas com alto risco
        