# Verificar movimentos possíveis para comer peças
    movimentos = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
    for movimento in movimentos:
        linha_destino = linha + movimento[0]
        coluna_destino = coluna + movimento[1]
        linha_comida = linha + movimento[0] // 2
        coluna_comida = coluna + movimento[1] // 2
        
        # Verificar se o movimento é válido
        if linha_destino >= 0 and linha_destino < len(tabuleiro) and coluna_destino >= 0 and coluna_destino < len(tabuleiro[0]):
            if tabuleiro[linha_destino][coluna_destino] == 0 and tabuleiro[linha_comida][coluna_comida] != 0 and tabuleiro[linha_comida][coluna_comida] != jogador:
                # Copiar o tabuleiro atual para um novo tabuleiro temporário
                novo_tabuleiro = [linha.copy() for linha in tabuleiro]
                novo_tabuleiro[linha][coluna] = 0  # Remover a peça atual
                novo_tabuleiro[linha_destino][coluna_destino] = jogador  # Mover a peça para a nova posição
                novo_tabuleiro[linha_comida][coluna_comida] = 0  # Remover a peça comida
                
                # Chamar recursivamente a função para continuar comendo peças
                nova_sequencia = sequencia + [(linha, coluna), (linha_destino, coluna_destino)]
                sub_sequencias = comer_pecas(novo_tabuleiro, jogador, linha_destino, coluna_destino, nova_sequencia)
                
                # Adicionar as sequências encontradas à lista de sequências possíveis
                sequencias_possiveis.extend(sub_sequencias)
    
    # Se não houver mais peças para comer, retornar a sequência encontrada
    if not sequencias_possiveis:
        return [sequencia]
    
    return sequencias_possiveis
