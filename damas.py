#importa biblioteca sys
import sys
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
        return False
    elif jogador == "B" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "@" and tabuleiro_inicial[linha_inicial][coluna_inicial] != "&":
        return False

    # Verificar se a posição final está vazia
    if tabuleiro_inicial[linha_final][coluna_final] != " ":
        return False
    
    # verificar se o movimento é diagonal
    # abs() retorna o valor absoluto de um núemro
    if abs(coluna_final - coluna_inicial) != abs(linha_final - linha_inicial):
        return False

    # Verificar se é um movimento válido para uma peça normal
    if tabuleiro_inicial[linha_inicial][coluna_inicial] == "o" or tabuleiro_inicial[linha_inicial][coluna_inicial] == "@":
        if jogador == "C" and ((abs(linha_final - linha_inicial) != 1 and abs(linha_final - linha_inicial) != 2) or (abs(coluna_final - coluna_inicial) != 1 and abs(coluna_final - coluna_inicial) != 2)):
            return False

        elif jogador == "B" and ((abs(linha_final - linha_inicial) != 1 and abs(linha_final - linha_inicial) != 2) or (abs(coluna_final - coluna_inicial) != 1 and abs(coluna_final - coluna_inicial) != 2)):
            return False

        if (abs(linha_final - linha_inicial) == 2 or abs(coluna_final - coluna_inicial) == 2):
            coluna_meio = (coluna_inicial + coluna_final) // 2
            linha_meio = (linha_inicial + linha_final) // 2
            if jogador == "C" and (tabuleiro_inicial[linha_meio][coluna_meio] != "@" and tabuleiro_inicial[linha_meio][coluna_meio] != "&"):
                return False

            elif jogador == "B" and (tabuleiro_inicial[linha_meio][coluna_meio] != "o" and tabuleiro_inicial[linha_meio][coluna_meio] != "O"):
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

    if verificar_captura_obrigatoria(tabuleiro_inicial, jogador) == True:
        if abs(coluna_inicial - coluna_final) == 1:
            return False
             
    return True

def realizar_movimento(tabuleiro_inicial, jogador, coluna_inicial, linha_inicial, coluna_final, linha_final, contador):
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

    #transforma peça em damas
    if jogador == "C" and linha_final == 9:
        tabuleiro_inicial[linha_final][coluna_final] = "O"
    elif jogador == "B" and linha_final == 0:
        tabuleiro_inicial[linha_final][coluna_final] = "&"

    if captura_feita:
        capturas_possiveis, matriz_letras = verificar_capturas_possiveis(tabuleiro_inicial, jogador, coluna_final, linha_final)
        if capturas_possiveis:
            return tabuleiro_inicial, [(linha_final, coluna_final), capturas_possiveis], matriz_letras, contador  # Retornar o tabuleiro atualizado e indicar que mais capturas são possíveis
        else:
            return tabuleiro_inicial, False, ["Captura_ja_realizada"], contador  # Retornar o tabuleiro atualizado e indicar que não há mais capturas possíveis
    
    return tabuleiro_inicial, False, ["qqr"], contador  # Retornar o tabuleiro atualizado e indicar que não houve captura
        
def contar_caractere(matriz, peca, dama):
    contador_de_elem = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == peca:
                contador_de_elem += 1
            if elemento == dama:
                contador_de_elem += 1
    return contador_de_elem  
  
def verificar_captura_obrigatoria(tabuleiro_inicial, jogador):
    # verifica o jogador
    if jogador == "C":
        pecas_amigas = ['o', 'O']
        pecas_oponente = ["@", "&"]
    else:
        pecas_amigas = ["@", "&"]
        pecas_oponente = ["o", "O"]
    capturas_possiveis = False
    for x in range(10):
        for y in range(10):
            linha = x
            coluna = y
            # verificar as diagonais
            movimentos_diagonais = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for direcao in movimentos_diagonais:
                coluna_alvo = coluna + direcao[0]
                linha_alvo = linha + direcao[1]
                coluna_captura = coluna + 2 * direcao[0]
                linha_captura = linha + 2 * direcao[1]
                
                # Verificar se as posições estão dentro do tabuleiro
                if coluna_alvo >= 0 and coluna_alvo < 10 and linha_alvo >= 0 and linha_alvo < 10 and coluna_captura >= 0 and coluna_captura < 10 and linha_captura >= 0 and linha_captura < 10:
                    peca_alvo = tabuleiro_inicial[linha_alvo][coluna_alvo]
                    peca_captura = tabuleiro_inicial[linha_captura][coluna_captura]
                    peca_origem = tabuleiro_inicial[x][y]
                    
                    # Verificar se a posição alvo contém uma peça do oponente e a posição de captura está vazia
                    if peca_alvo in pecas_oponente and peca_captura == " " and peca_origem in pecas_amigas:
                        capturas_possiveis = True
            
    return capturas_possiveis  

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
     
def transformar_jogadas(tabuleiro_inicial,lista_de_arquivo, contador):
    erro = False
    if not len(lista_de_arquivo) == 0:
        movimento = lista_de_arquivo[contador].strip()
        contador = contador + 1
    else:
        movimento = input("Digite o movimento (exemplo: C3--D4): ")
    #deixa tudo em maiúsculo para evitar erro do usuário
    movimento = movimento.upper()

    if not len(lista_de_arquivo) == 0:
        if len(movimento) != 6:
            N = contador + 1
            print(f'Jogada inválida na linha {N} do arquivo de entrada1.')
            erro = True
    else:
        if len(movimento) != 6:
            print("Movimento inválido, Digite novamente.")
            erro = True 
    
    # ord retorna o valor ASCII da letra, pela subatração [cap[0]conseguimos a posição relativa em relação a A
    # ou seja, transforma as letras em números 
    coluna_inicial = ord(movimento[0]) - ord('A') 
    linha_inicial = int(movimento[1])
    coluna_final = ord(movimento[4]) - ord('A') 
    linha_final = int(movimento[5])

    if len(lista_de_arquivo) == 0:    
        if not movimento_valido(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final):
            print("Movimento inválido! Digite novamente.")
            print(erro)
            erro = True
    else:
        if not movimento_valido(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final):
            N = contador 
            print(f'Jogada inválida na linha {N} do arquivo de entrada.')
            erro = True
    return (linha_inicial, coluna_inicial, linha_final, coluna_final, erro, contador)

def jogo_damas(linhas):
    N = 0
    lista_de_arquivo = linhas
    global jogador_atual
    if len(sys.argv) > 1:
        jogador_atual = lista_de_arquivo[0].strip()
    else:
        jogador_atual = input("Digite qual usuário deve começar: C(o) ou B(@): ")
    jogador_atual = jogador_atual.upper()
    global vencedor
    global tabuleiro_inicial
    tabuleiro_inicial = [
    ["#", "o", "#", "o", "#", "o", "#", "o", "#", "o"],
    ["o", "#", "o", "#", "o", "#", "o", "#", "o", "#"],
    ["#", "o", "#", "o", "#", "o", "#", "o", "#", "o"],
    [" ", "#", " ", "#", " ", "#", "@", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    ["@", "#", "@", "#", "@", "#", "@", "#", "@", "#"],
    ["#", "@", "#", "@", "#", "@", "#", "@", "#", "@"],
    ["@", "#", "@", "#", "@", "#", "@", "#", "@", "#"]
    ]
    contador = 1
    while True:

        if not len(sys.argv) > 1:
            tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
            imprimir_tabuleiro(tabuleiro)
            if jogador_atual == "C":
                print("Jogador atual: C (o)")
            else:
                print("Jogador atual: B (@)")
        
        [linha_inicial, coluna_inicial, linha_final, coluna_final, erro_jogada, contador] = transformar_jogadas(tabuleiro_inicial, lista_de_arquivo, contador)
        
        if erro_jogada:
            continue
        while True:
            [tabuleiro_inicial, out, matriz_letras, contador] = realizar_movimento(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final, contador)
            captura = False
            
            if out:
                if len(matriz_letras) == 1:
                    [(linha_inicial, coluna_inicial), captura] = out
                    coluna_final = captura[0][0]
                    linha_final  = captura[0][1]
                else:
                    [(linha_inicial, coluna_inicial), captura] = out
                    tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
                    if not len(sys.argv) > 1:
                        imprimir_tabuleiro(tabuleiro)
                        movimento_2 = input("Digite a posição da peça a ser capturada (A, B, C, D): \n ex: D     B\n        P\n     C     A\n")
                    else: 
                        movimento_2 = lista_de_arquivo[contador].strip()
                        contador = contador + 1
                    while True:    
                        if not movimento_2 in matriz_letras:
                            N = contador + 1
                            if not len(sys.argv) > 1:
                                print("Comando inválido: ")
                                movimento_2 = input("Digite a posição da peça a ser capturada (A, B, C, D): \n ex: D     B\n        P\n     C     A\n")
                            else:
                                print(f'Jogada inválida na linha {N} do arquivo de entrada1.')
                                movimento_2 = lista_de_arquivo[contador].strip()                            
                                contador = contador + 1    
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
        
        if matriz_letras[0] == "Captura_ja_realizada":
            tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
            if not len(sys.argv) > 1:
                imprimir_tabuleiro(tabuleiro)
                print("Você capturou um peça e tem direito a mais uma jogada!")
            [linha_inicial, coluna_inicial, linha_final, coluna_final, erro_jogada, contador] = transformar_jogadas(tabuleiro_inicial, lista_de_arquivo, contador)
            if erro_jogada:
                continue
            realizar_movimento(tabuleiro_inicial, jogador_atual, coluna_inicial, linha_inicial, coluna_final, linha_final, contador)
            

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
pecas_c = 0
pecas_b = 0
while a == True:
    #função que retorna se o jogo deve reiniciar
    def revanche():
        global a
        if len(sys.argv) > 1:
            a = False
        else:
            escolha = (input("Deseja jogar novamente? (Digite SIM ou NAO) :"))
            escolha = escolha.upper()
            if escolha == "SIM":
                a = True
                return  a
            elif escolha == "NAO":
                a = False
                return a 
            
    if len(sys.argv) > 1:
        arquivo_de_texto = sys.argv[1]
        with open(arquivo_de_texto, 'r') as arquivo:
            linhas = arquivo.readlines()
        jogo_damas(linhas)
    else:
        linhas = []
        jogo_damas(linhas)
    #printa o vencedor do jogo
    if len(sys.argv) > 1:
        tabuleiro = inicializar_tabuleiro(tabuleiro_inicial)
        imprimir_tabuleiro(tabuleiro)
    if vencedor == "B":
        print("B venceu")
    if vencedor == "C":
        print("C venceu")

    for linha in tabuleiro_inicial:
        pecas_c = pecas_c + linha.count("o")
        pecas_c = pecas_c + linha.count("O")
        pecas_b = pecas_b + linha.count("@")
        pecas_b = pecas_b + linha.count("&")
    if len(sys.argv) > 1:
        print(f"Peças comidas:\nJogador B: {15 - pecas_b}\nJogador C: {15 - pecas_c}")
    revanche()
    
