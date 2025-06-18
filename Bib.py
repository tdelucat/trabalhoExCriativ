#biblioteca para ser usada no trabalho

def TelaAbertura():

    lista_perguntas = ["Ação para minimização dos efeitos","Score e nível de risco para pessoa solicitada","Impressão de todas as pessoas","Percentual de pessoas com nível de risco baixo","Percentual de pessoas com nível de risco moderado","Percentual de pessoas com nível de risco alto"]

    for i in range(len(lista_perguntas)):
        print(f"\n{lista_perguntas[i]}")
        print("\nS para aceitar, N para ir para a proxima, E para sair.")
        confere = input("Digite se quer essa pergunta: ").upper()
        while confere not in "SEN":
            confere = input("\nDigite uma resposta válida: ").upper()
        if confere == "S":
           return i

        elif confere == "E":
            return -1 

def CalculaScoreIndividual(respostas):

    Pesos = [["Nunca", "Às vezes", "Frequentemente", "Todos os dias"], 
             ["Sim", "Com dificuldade", "Não consegui"], 
             ["Sim", "Neutro", "Nada motivado(a)"], 
             ["Não", "Um pouco", "Sim, constantemente"], 
             ["Não", "Às vezes", "Quase sempre"], 
             ["Não", "Já tive essa semana", "Tenho todos os dias"], 
             ["Não", "Levemente", "Muito"], 
             ["Não", "Com esforço", "Me isolei totalmente"], 
             ["Sim", "Não tive tempo", "Nem vontade tive"]]
    Pesos_perguntas = [3, 2, 3, 2, 3, 3, 2, 2, 2]

    risco = 0
    
    for i in range(len(respostas)):
        resposta_atual = respostas[i]
        if resposta_atual not in Pesos[i]:
            print(f"Erro de contagem!!!!! {resposta_atual} com {i}")
        else:
            risco += Pesos[i].index(resposta_atual) * Pesos_perguntas[i]
    return risco
                
def ClassificaNivelRisco(riscos):

    if riscos <= 10:
        return "Risco Baixo"
    elif riscos > 20:
        return "Risco Alto"
    else:
        return "Risco Moderado"
    
def SugereMinimizacaoSintomas():

    lista_perguntas = ["Cansaço físico","Energia para tarefas","Motivação pelo trabalho","Procrastinação","Sentido no trabalho","Pensamentos negativos","Isolamento emocional","Isolamento social","Fazer algo prazeroso"]
    lista_respostas = ["Evite estudar até tarde e reduza o uso de telas à noite. Incorpore pausas estratégicas durante o dia (técnica Pomodoro, por exemplo).",
    "Organize sua rotina começando por pequenas vitórias, como arrumar a cama ou tomar café — isso ativa o cérebro e gera estímulo.",
    "Busque aplicar conteúdos em projetos reais, participar de hackathons, ou explorar temas que te inspiram dentro do curso.",
    "Use listas com entregas claras e realistas por dia. Elimine distrações e crie um ambiente de foco (limpo, silencioso, com metas visíveis).",
    "Converse com colegas e professores, entenda o impacto do que você está estudando e crie conexões com seus valores pessoais.",
    "Reconheça o limite entre cansaço e sofrimento. Conversar com alguém que compreenda sua trajetória pode aliviar a sobrecarga emocional.",
    "Mesmo em poucos minutos, práticas como respiração guiada ou alongamentos reduzem o acúmulo emocional.",
    "Uma ligação de 5 minutos ou uma pausa para café com alguém confiável ajuda a recuperar o senso de pertencimento.",
    "Desenhar, ouvir música, assistir algo leve, cozinhar... O prazer gratuito recarrega energia emocional e combate a anedonia."]
    
    for i in range(len(lista_perguntas)):
        print(f"\n{lista_perguntas[i]}")
        print("\nS para aceitar, N para ir para a proxima, E para sair.")
        confere = input("Digite se quer essa pergunta: \n").upper()
        while confere not in "SEN":
            confere = input("\nDigite uma resposta válida: \n").upper()
        if confere == "S":
            for j in range(len(lista_respostas)):
                if j == i:
                    print(f"\n{lista_respostas[j]}\n")
            break
        elif confere == "E":
            return -1

def CalculaPercentual(lista,indice):
    
    total = len(lista) - 1
    quant_alto = 0
    quant_moderado = 0
    quant_baixo = 0

    for i in range(1, len(lista)):
        risco = lista[i][11]
        if risco == "Risco Baixo":
            quant_baixo += 1
        elif risco == "Risco Moderado":
            quant_moderado += 1
        else:
            quant_alto += 1

    Perc_Baixo = (quant_baixo / total) * 100
    Perc_Moderado = (quant_moderado / total) * 100
    Perc_Alto = (quant_alto / total) * 100

    print()
    print("\n------- Percentual de Pessoas -------")
    if indice == 3:
        print(f"Tem {quant_baixo} pessoas, contando um percentual de {Perc_Baixo:.2f}%")
    elif indice == 4:
        print(f"Tem {quant_moderado} pessoas, contando um percentual de {Perc_Moderado:.2f}%")
    elif indice == 5:
        print(f"Tem {quant_alto} pessoas, contando um percentual de {Perc_Alto:.2f}%")

def AtualizaMatrizScoreRisco(lista):
    lista[0].append("Score")
    lista[0].append("Risco")
    

    for i in range(1, len(lista)):
        respostas = lista[i][1:]
        score = CalculaScoreIndividual(respostas)
        risco = ClassificaNivelRisco(score)
        lista[i].append(score)
        lista[i].append(risco)

def ImprimeMatrizScoreRisco(lista):
    
    for i in range(len(lista)):
        print()
        print(lista[i])

def ImprimePessoaScoreRisco(lista):
    
    numero = int(input("Escolha o numero da pessoa (1-120): "))

    for i in range(len(lista)):
        if numero == i:
            print(f"Pessoa {numero} | Score: {lista[i][10]} | Risco: {lista[i][11]}")