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
        erro = 41
        return False

    # Verificar se a posição inicial contém a peça do jogador
    if jogador == "C" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "o" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "O":
        erro = 45
        return False
    elif jogador == "B" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "@" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "&":
        erro = 46
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
        if (abs(linha_final - linha_inicial) == 2 or abs(coluna_final - coluna_inicial) == 2):
            coluna_meio = (coluna_inicial + coluna_final) // 2
            linha_meio = (linha_inicial + linha_final) // 2
            if jogador == "C" and (tabuleiro_inicial[linha_meio][coluna_meio] != "@" and tabuleiro_inicial[linha_meio][coluna_meio] != "&"):
                
                erro = 6
                return False
            elif jogador == "B" and (tabuleiro_inicial[linha_meio][coluna_meio] != "o" and tabuleiro_inicial[linha_meio][coluna_meio] != "O"):
                
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
                    erro = 8
                    return False
                if tabuleiro_inicial[i][j] == "@" or tabuleiro_inicial[i][j] == "&":
                    obstaculos_seguidos += 1
                    
            if tabuleiro_inicial[linha_inicial][coluna_inicial] == "&":
                if tabuleiro_inicial[i][j] != " " and tabuleiro_inicial[i][j] != "o" and tabuleiro_inicial[i][j] != "O":
                    erro = 9
                    return False   
                if tabuleiro_inicial[i][j] == "o" or tabuleiro_inicial[i][j] == "O":
                    obstaculos_seguidos += 1
                       
            i += linha_direcao
            j += coluna_direcao
        if obstaculos_seguidos > 1:
            erro = 10
            return False    
            
    return True

def realizar_movimento(tabuleiro_inicial, jogador, coluna_inicial, linha_inicial, coluna_final, linha_final):
    captura_feita = False
    
    # Verificar se há uma peça inimiga entre a posição inicial e a posição final
    if abs(coluna_final - coluna_inicial) == 2 and abs(linha_final - linha_inicial) == 2:
        coluna_comida = (coluna_inicial + coluna_final) // 2
        linha_comida = (linha_inicial + linha_final) // 2

        if jogador == "C" and (tabuleiro_inicial[linha_comida][coluna_comida] == "@" or tabuleiro_inicial[linha_comida][coluna_comida] == "&"):
            # Remover a peça inimiga do tabuleiro
            tabuleiro_inicial[linha_comida][coluna_comida] = " "
            captura_feita = True

        elif jogador == "B" and (tabuleiro_inicial[linha_comida][coluna_comida] == "o" or tabuleiro_inicial[linha_comida][coluna_comida] == "O"):
            # Remover a peça inimiga do tabuleiro
            tabuleiro_inicial[linha_comida][coluna_comida] = " "
            captura_feita = True
    
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
                    captura_feita = True
            if tabuleiro_inicial[linha_inicial][coluna_inicial] == "&":  
                if tabuleiro_inicial[i][j] == "o" or tabuleiro_inicial[i][j] == "O":
                    tabuleiro_inicial[i][j] = " "  
                    captura_feita = True  
            i += linha_direcao
            j += coluna_direcao


    # fazer o movimento
    tabuleiro_inicial[linha_final][coluna_final] = tabuleiro_inicial[linha_inicial][coluna_inicial]
    tabuleiro_inicial[linha_inicial][coluna_inicial] = " "
    
    #tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
    #imprimir_tabuleiro(tabuleiro)

    #transforma peça em damas
    if jogador == "C" and linha_final == 9:
        tabuleiro_inicial[linha_final][coluna_final] = "O"
    elif jogador == "B" and linha_final == 0:
        tabuleiro_inicial[linha_final][coluna_final] = "&"
    if captura_feita:
        capturas_possiveis, matriz_letras = verificar_capturas_possiveis(tabuleiro_inicial, jogador, coluna_final, linha_final)
        if capturas_possiveis:
            return tabuleiro_inicial, [(linha_final, coluna_final), capturas_possiveis], matriz_letras  # Retornar o tabuleiro atualizado e indicar que mais capturas são possíveis
        else:
            return tabuleiro_inicial, False, []  # Retornar o tabuleiro atualizado e indicar que não há mais capturas possíveis
    
    return tabuleiro_inicial, False, []  # Retornar o tabuleiro atualizado e indicar que não houve captura

        
def contar_caractere(matriz, peca, dama):
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == peca:
                contador += 1
            if elemento == dama:
                contador += 1
    return contador    

def verificar_capturas_possiveis(tabuleiro_inicial, jogador, coluna, linha):
    capturas_possiveis = False
    movimentos_captura = []
    
    # Verificar se o jogador é o C ou o B
    if jogador == "C":
        pecas_oponente = ["@", "&"]
    else:
        pecas_oponente = ["o", "O"]
    
    # Verificar as diagonais para possíveis capturas
    movimentos_diagonais = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    matriz_letras = []
    numero_matriz = 65
    for direcao in movimentos_diagonais:
        coluna_atual = coluna
        linha_atual = linha
        coluna_alvo = coluna + direcao[0]
        linha_alvo = linha + direcao[1]
        coluna_captura = coluna + 2 * direcao[0]
        linha_captura = linha + 2 * direcao[1]
        
        # Verificar se as posições estão dentro do tabuleiro
        if coluna_alvo >= 0 and coluna_alvo < 10 and linha_alvo >= 0 and linha_alvo < 10 and coluna_captura >= 0 and coluna_captura < 10 and linha_captura >= 0 and linha_captura < 10:
            peca_alvo = tabuleiro_inicial[linha_alvo][coluna_alvo]
            peca_captura = tabuleiro_inicial[linha_captura][coluna_captura]
            
            # Verificar se a posição alvo contém uma peça do oponente e a posição de captura está vazia
            if peca_alvo in pecas_oponente and peca_captura == " ":
                movimentos_captura.append((coluna_captura, linha_captura, coluna_alvo, linha_alvo))
                capturas_possiveis = True
                
                matriz_letras.append(str(chr(numero_matriz)))
        numero_matriz += 1
    
    return (movimentos_captura, matriz_letras) if capturas_possiveis else ([], matriz_letras)     
def jogo_damas():
    erro = "**"
    jogador_atual = input("Digite qual usuário deve começar: C(o) ou B(@): ")
    jogador_atual = jogador_atual.upper()
    global vencedor
    tabuleiro_inicial = [
    ["#", "o", "#", "o", "#", "o", "#", "o", "#", "o"],
    ["o", "#", "o", "#", "o", "#", "o", "#", "o", "#"],
    ["#", "o", "#", "o", "#", "o", "#", "o", "#", "o"],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    ["@", "#", "@", "#", "@", "#", "@", "#", "@", "#"],
    ["#", "@", "#", "@", "#", "@", "#", "@", "#", "@"],
    ["@", "#", "@", "#", "@", "#", "@", "#", "@", "#"]
    ]

    while True:
        tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
        imprimir_tabuleiro(tabuleiro)

        def printTabueliro(tabuleiro):
            tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
            imprimir_tabuleiro(tabuleiro)

        if jogador_atual == "C":
            print("Jogador atual: C (o)")
        else:
            print("Jogador atual: B (@)")

        movimento = input("Digite o movimento (exemplo: C3--D4): ")

        #deixa tudo em maiúsculo para evitar erro do usuário
        movimento = movimento.upper()

        if movimento == "SAIR":
            print("Jogo encerrado.")
            break

        if len(movimento) != 6:
            print("Movimento inválido, Digite novamente.")
            continue
        

        # ord retorna o valor ASCII da letra, pela subatração [cap[0]conseguimos a posição relativa em relação a A
        # ou seja, transforma as letras em números 
        coluna_inicial = ord(movimento[0]) - ord('A') 
        linha_inicial = int(movimento[1])
        coluna_final = ord(movimento[4]) - ord('A') 
        linha_final = int(movimento[5])
        

         
        if not movimento_valido(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final):
            print("Movimento inválido! Digite novamente.")
            print(erro)
            continue
        
        

        while True:
            [tabuleiro_inicial, out, matriz_letras] = realizar_movimento(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final)
            captura = False
            
            if out:
                if len(matriz_letras) == 1:
                    [(linha_inicial, coluna_inicial), captura] = out
                    coluna_final = captura[0][0]
                    linha_final  = captura[0][1]
                else:
                    [(linha_inicial, coluna_inicial), captura] = out
                    tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
                    imprimir_tabuleiro(tabuleiro)
                    movimento_2 = input("Digite a posição da peça a ser capturada (A, B, C, D): \n ex: D     B\n        P\n     C     A\n")
                    while True:    
                        if not movimento_2 in matriz_letras:
                            print("Comando inválido: ")
                            movimento_2 = input("Digite a posição da peça a ser capturada (A, B, C, D): \n ex: D     B\n        P\n     C     A\n")
                        else:
                            break
                    tamanho_da_matriz = len(matriz_letras)
                    for i in range(tamanho_da_matriz):
                        if movimento_2 == matriz_letras[i]:
                            a = i

                    coluna_final = captura[a][0]
                    linha_final  = captura[a][1]
            if not captura:
                break


        # if capturas:
        #     tabuleiro_inicial[capturas[0][0]][capturas[0][1]] = 

        if jogador_atual == "C":
            jogador_atual = "B"
        else:
            jogador_atual = "C"
        
        ocorrencia_B = contar_caractere(tabuleiro_inicial, "@" , "&")
        ocorrencia_C = contar_caractere(tabuleiro_inicial, "o" , "O")
        if ocorrencia_B == 0:
            vencedor = "C"
            return False
        if ocorrencia_C == 0:
            vencedor = "B"
            return False
            
a = True 
while a == True:
    #função que retorna se o jogo deve reiniciar
    def revanche():
        global a
        escolha = (input("Deseja jogar novamente? (Digite SIM ou NAO) :"))
        escolha = escolha.upper()
        if escolha == "SIM":
            a = True
            return  a
        elif escolha == "NAO":
            a = False
            return a 
    #inicia do jogo
    jogo_damas()
    #printa o vencedor do jogo
    if vencedor == "B":
        print("B venceu")
    if vencedor == "C":
        print("C venceu")
    revanche()
    
