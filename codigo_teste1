# tabuleiro matriz = tabuleiro sem as frescuras
# tabuleiro completo = tabuleiro com elas

# função usada para imprimir o tabuleiro completo
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

# adiciona os detelhes ao tabuleiro
def inicializar_tabuleiro(tabuleiro_inicial):

    tabuleiro = []
    
    # colunas e linhas que darão as coodenadas
    letras = "ABCDEFGHIJ"
    numeros = "0123456789"

    # estrutura da linhas da letras que são add no início e no fim do tabuleiro
    linha_superior = "  " + "|".join([""+letra+"" for letra in letras]) + ""
    linha_inferior = "  " + "|".join([""+letra+"" for letra in letras]) + ""

    # estrutura usada para separar visualemnte as casas (vamos nos referir a ele como separador)
    separador = " +-+-+-+-+-+-+-+-+-+-+ "

    # adiciona no topo uma linha de letras e um separador logo abaixo
    tabuleiro.append(linha_superior)
    tabuleiro.append(separador)


    for i in range(10):
        linha = numeros[i] + "|"
        for j in range(10):
            linha += "" + tabuleiro_inicial[i][j] + "|"
        linha += numeros[i]
        tabuleiro.append(linha)
        tabuleiro.append(separador)

    tabuleiro.append(linha_inferior)

    return tabuleiro

def movimento_valido(tabuleiro_inicial, jogador, coluna_inicial, linha_inicial, coluna_final, linha_final):
    global erro
    # Verificar se as coordenadas estão dentro do tabuleiro
    if coluna_inicial < 0 or coluna_inicial >= 10 or linha_inicial < 0 or linha_inicial >= 10 or coluna_final < 0 or coluna_final >= 10 or linha_final < 0 or linha_final >= 10:
        return False

    # Verificar se a posição inicial contém a peça do jogador
    if jogador == "C" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "o" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "O":
        return False
    elif jogador == "B" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "@" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "&":
        return False

    # Verificar se a posição final está vazia
    if tabuleiro_inicial[linha_final][coluna_final] != " ":
        
        erro = 2
        return False
    

    # verificar se o movimento é diagonal
    # abs() retorna o valor absoluto de um núemro
    if abs(coluna_final - coluna_inicial) != abs(linha_final - linha_inicial):
        
        erro = 3
        return False

    # Verificar se é um movimento válido para uma peça normal
    if tabuleiro_inicial[linha_inicial][coluna_inicial] == "o" or tabuleiro_inicial[linha_inicial][coluna_inicial] == "@":
        if jogador == "C" and ((abs(linha_final - linha_inicial) != 1 and abs(linha_final - linha_inicial) != 2) or (abs(coluna_final - coluna_inicial) != 1 and abs(coluna_final - coluna_inicial) != 2)):
            
            erro = 4
            return False
        elif jogador == "B" and ((abs(linha_final - linha_inicial) != 1 and abs(linha_final - linha_inicial) != 2) or (abs(coluna_final - coluna_inicial) != 1 and abs(coluna_final - coluna_inicial) != 2)):
            
            erro = 5
            return False
        if jogador == "C" and (abs(linha_final - linha_inicial) == 2 or abs(coluna_final - coluna_inicial) == 2):
            coluna_meio = (coluna_inicial + coluna_final) // 2
            linha_meio = (linha_inicial + linha_final) // 2
            if (tabuleiro_inicial[linha_meio][coluna_meio] != "@" or tabuleiro_inicial[linha_meio][coluna_meio] != "&"):
                
                erro = 6
                return False
            elif jogador == "B" and (tabuleiro_inicial[linha_meio][coluna_meio] == "o" or tabuleiro_inicial[linha_meio][coluna_meio] == "O"):
                
                erro = 7
                return False


    # verifica movimento dama
    if tabuleiro_inicial[linha_inicial][coluna_inicial] == "O" or tabuleiro_inicial[linha_inicial][coluna_inicial] == "&":
        linha_direcao = 1 if linha_final > linha_inicial else -1
        coluna_direcao = 1 if coluna_final > coluna_inicial else -1
        i = linha_inicial + linha_direcao
        j = coluna_inicial + coluna_direcao
        obstaculos_seguidos = 0
        while i != linha_final and j != coluna_final:
            if tabuleiro_inicial[linha_inicial][coluna_inicial] == "O":
                if tabuleiro_inicial[i][j] != " " and tabuleiro_inicial[i][j] != "@" and tabuleiro_inicial[i][j] != "&":
                    return False
                if tabuleiro_inicial[i][j] == "@" or tabuleiro_inicial[i][j] == "&":
                    obstaculos_seguidos += 1
            if tabuleiro_inicial[linha_inicial][coluna_inicial] == "&":
                if tabuleiro_inicial[i][j] != " " and tabuleiro_inicial[i][j] != "o" and tabuleiro_inicial[i][j] != "O":
                    return False   
                if tabuleiro_inicial[i][j] == "o" or tabuleiro_inicial[i][j] == "O":
                    obstaculos_seguidos += 1     
            i += linha_direcao
            j += coluna_direcao
        if obstaculos_seguidos > 1:
            return False    

    return True

def realizar_movimento(tabuleiro_inicial, jogador, coluna_inicial, linha_inicial, coluna_final, linha_final):
    
    
    # Verificar se há uma peça inimiga entre a posição inicial e a posição final
    if abs(coluna_final - coluna_inicial) == 2 and abs(linha_final - linha_inicial) == 2:
        coluna_comida = (coluna_inicial + coluna_final) // 2
        linha_comida = (linha_inicial + linha_final) // 2

        if jogador == "C" and (tabuleiro_inicial[linha_comida][coluna_comida] == "@" or tabuleiro_inicial[linha_comida][coluna_comida] == "&"):
            # Remover a peça inimiga do tabuleiro
            tabuleiro_inicial[linha_comida][coluna_comida] = " "
        elif jogador == "B" and (tabuleiro_inicial[linha_comida][coluna_comida] == "o" or tabuleiro_inicial[linha_comida][coluna_comida] == "O"):
            # Remover a peça inimiga do tabuleiro
            tabuleiro_inicial[linha_comida][coluna_comida] = " "
    
    # captura de peças pela dama
    if tabuleiro_inicial[linha_inicial][coluna_inicial] == "O" or tabuleiro_inicial[linha_inicial][coluna_inicial] == "&":
        linha_direcao = 1 if linha_final > linha_inicial else -1
        coluna_direcao = 1 if coluna_final > coluna_inicial else -1
        i = linha_inicial + linha_direcao
        j = coluna_inicial + coluna_direcao
        while i != linha_final and j != coluna_final:
            if tabuleiro_inicial[linha_inicial][coluna_inicial] == "O":
                if tabuleiro_inicial[i][j] == "@" or tabuleiro_inicial[i][j] == "&":
                    tabuleiro_inicial[i][j] = " "
            if tabuleiro_inicial[linha_inicial][coluna_inicial] == "&":  
                if tabuleiro_inicial[i][j] == "o" or tabuleiro_inicial[i][j] == "O":
                    tabuleiro_inicial[i][j] = " "    
            i += linha_direcao
            j += coluna_direcao


    # fazer o movimento
    tabuleiro_inicial[linha_final][coluna_final] = tabuleiro_inicial[linha_inicial][coluna_inicial]
    tabuleiro_inicial[linha_inicial][coluna_inicial] = " "

    #transforma peça em damas
    if jogador == "C" and linha_final == 9:
        tabuleiro_inicial[linha_final][coluna_final] = "O"
    elif jogador == "B" and linha_final == 0:
        tabuleiro_inicial[linha_final][coluna_final] = "&"

    
    
      
def jogo_damas():
    erro = "mac"
    tabuleiro_inicial = [
    ["#", " ", "#", "o", "#", "o", "#", "o", "#", "o"],
    ["o", "#", "@", "#", "o", "#", "o", "#", "o", "#"],
    ["#", "o", "#", "@", "#", "o", "#", "o", "#", "o"],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "O", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", " "],
    ["#", " ", "#", " ", "#", " ", "#", "@", "#", " "],
    ["@", "#", "@", "#", "@", "#", "@", "#", " ", "#"],
    ["#", "@", "#", "@", "#", "@", "#", "@", "#", "@"],
    ["@", "#", "@", "#", "@", "#", "@", "#", " ", "#"]
    ]
    
    jogador_atual = "C"

    while True:
        tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
        imprimir_tabuleiro(tabuleiro)

        if jogador_atual == "C":
            print("Jogador atual: C (o)")
        else:
            print("Jogador atual: B (@)")

        movimento = input("Digite o movimento (exemplo: C3-D4): ")

        #deixa tudo em maiúsculo para evitar erro do usuário
        movimento = movimento.upper()

        if movimento == "SAIR":
            print("Jogo encerrado.")
            break

        if len(movimento) != 5:
            print("Movimento inválido, Digite novamente. ***s1***")
            continue
        # ord retorna o valor ASCII da letra, pela subatração conseguimos a posição relativa em relação a A
        # ou seja, transforma as letras em números 
        coluna_inicial = ord(movimento[0]) - ord('A') 
        linha_inicial = int(movimento[1])
        coluna_final = ord(movimento[3]) - ord('A') 
        linha_final = int(movimento[4])

        if not movimento_valido(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final):
            print("Movimento inválido! Digite novamente. ***S2***")
            print(erro)
            continue

        realizar_movimento(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final)

        if jogador_atual == "C":
            jogador_atual = "B"
        else:
            jogador_atual = "C"

jogo_damas()






