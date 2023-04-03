import random

# Define o tamanho da matriz
tamanho = 3

# Cria a matriz com zeros
matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

# Função para imprimir a matriz
def imprimir_matriz():
    for linha in matriz:
        print(linha)

# Função para verificar se o jogo acabou
def jogo_acabou():
    # Verifica se todas as casas estão preenchidas
    if all(all(linha) for linha in matriz):
        return True

    # Verifica se alguma linha está completa
    for linha in matriz:
        if all(linha):
            return True

    # Verifica se alguma coluna está completa
    for coluna in range(tamanho):
        if all(matriz[linha][coluna] for linha in range(tamanho)):
            return True

    # Verifica se alguma diagonal está completa
    if all(matriz[i][i] for i in range(tamanho)):
        return True

    if all(matriz[i][tamanho-i-1] for i in range(tamanho)):
        return True

    return False

import random

def inicializar_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        linha = [0] * tamanho
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def obter_jogada():
    jogada_valida = False
    while not jogada_valida:
        try:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            if matriz[linha][coluna] != 0:
                print("Esta posição já está ocupada. Tente novamente.")
            else:
                jogada_valida = True
        except:
            print("Entrada inválida. Tente novamente.")
    return linha, coluna

def verificar_vitoria(matriz):
    for i in range(len(matriz)):
        # verifica se a linha i é toda igual
        if matriz[i][0] != 0 and matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2]:
            return True, matriz[i][0]
        # verifica se a coluna i é toda igual
        if matriz[0][i] != 0 and matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i]:
            return True, matriz[0][i]
    # verifica as diagonais
    if matriz[0][0] != 0 and matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]:
        return True, matriz[0][0]
    if matriz[0][2] != 0 and matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
        return True, matriz[0][2]
    # verifica se deu empate
    if all([all(linha) for linha in matriz]):
        return True, None
    return False, None

def verificar_vencedor(tabuleiro):
    # Verifica as linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

    # Verifica as colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
            return tabuleiro[0][coluna]

    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    # Se ninguém venceu, retorna None
    return None

def desenhar_tabuleiro(tabuleiro):
    print(f' {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ')
    print('---+---+---')
    print(f' {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ')
    print('---+---+---')
    print(f' {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ')

def fazer_jogada(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

def obter_jogada(jogador):
    print(f"Vez do jogador {jogador}")
    linha = int(input("Escolha uma linha (0, 1 ou 2): "))
    coluna = int(input("Escolha uma coluna (0, 1 ou 2): "))
    return linha, coluna

def verificar_vencedor(tabuleiro):
    # Verifica as linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

    # Verifica as colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
            return tabuleiro[0][coluna]

    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    # Se ninguém venceu, retorna None
    return None

def jogar():
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    jogadores = ['X', 'O']
    jogador_atual = jogadores[0]

    while True:
        # Desenha o tabuleiro
        desenhar_tabuleiro(tabuleiro)

        # Pede a jogada do jogador atual
        if jogador_atual == 'X':
            linha, coluna = obter_jogada(jogador_atual)
        else:
            linha, coluna = obter_jogada_bot(jogador_atual, tabuleiro)

        # Faz a jogada e verifica se é válida
        if fazer_jogada(tabuleiro, jogador_atual, linha, coluna):
            # Verifica se o jogador venceu
            if verificar_vencedor(tabuleiro) == jogador_atual:
                desenhar_tabuleiro(tabuleiro)
                print

def jogar_tic_tac_toe():
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # Define os jogadores
    jogador1 = 'X'
    jogador2 = 'O'

    # Inicia o jogo
    jogando = True
    vez_do_jogador1 = True
    while jogando:
        if vez_do_jogador1:
            # Jogador 1 faz a jogada
            jogada = obter_jogada(tabuleiro, jogador1)
        else:
            # Bot faz a jogada
            jogada = obter_jogada_bot(tabuleiro, jogador2, jogador1)
            print("O bot jogou na posição:", jogada)
# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

# Função para atualizar o tabuleiro
def atualizar_tabuleiro(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

# Função para verificar se o tabuleiro está completo
def tabuleiro_completo(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == " ":
                return False
    return True

# Função para verificar se houve um vencedor
def verificar_vencedor(tabuleiro):
    # Verificando linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != " ":
            return linha[0]

    # Verificando colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != " ":
            return tabuleiro[0][coluna]

    # Verificando diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        return tabuleiro[0][0]

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        return tabuleiro[0][2]

    # Se não houver vencedor
    return None

# Função para obter a jogada do bot
def obter_jogada_bot(tabuleiro):
    # Verificando se é possível ganhar na próxima jogada
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "O"
                if verificar_vencedor(tabuleiro) == "O":
                    return (linha, coluna)
                tabuleiro[linha][coluna] = " "

    # Verificando se o jogador pode ganhar na próxima jogada
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "X"
                if verificar_vencedor(tabuleiro) == "X":
                    return (linha, coluna)
                tabuleiro[linha][coluna] = " "

    # Jogando em uma posição aleatória
    posicoes_vazias = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                posicoes_vazias.append((linha, coluna))
    return random.choice(posicoes_vazias)


# Função principal
def jogar_jogo():
    tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    jogador_atual = "X"

    # Loop do jogo
    while True:
        imprimir_tabuleiro(tabuleiro)

        # Verifica se alguém venceu ou empatou
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            print("O jogador", vencedor, "venceu!")
            jogando = False
        elif tabuleiro_completo(tabuleiro):
            print("Empate!")
            jogando = False

        # Troca a vez do jogador
        vez_do_jogador1 = not vez_do_jogador1

def obter_jogada_bot():
    jogada_valida = False
    while not jogada_valida:
        linha = random.randint(0, tamanho-1)
        coluna = random.randint(0, tamanho-1)
        if matriz[linha][coluna] == 0:
            jogada_valida = True
    return linha, coluna

def obter_jogada_bot(tabuleiro, jogador_bot, jogador_pessoa):
    # Verifica se o bot pode vencer em alguma jogada
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = jogador_bot
                if verificar_vencedor(tabuleiro) == jogador_bot:
                    return (i, j)
                tabuleiro[i][j] = ' '

    # Verifica se o jogador pode vencer em alguma jogada e bloqueia
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = jogador_pessoa
                if verificar_vencedor(tabuleiro) == jogador_pessoa:
                    return (i, j)
                tabuleiro[i][j] = ' '

    # Joga em uma posição aleatória
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if tabuleiro[i][j] == ' ':
            return (i, j)

# programa principal

print("Bem-vindo ao Jogo da Velha!\n")

tamanho = 3
matriz = inicializar_matriz(tamanho)
jogador_atual = 1

modo_jogo = input("Digite 'p' para jogar contra um amigo ou 'b' para jogar contra o bot: ")
if modo_jogo == 'p':
    jogadores = ['X', 'O']
else:
    jogadores = ['X', 'Bot']
    if jogador_atual == "X":
     jogada = obter_jogada("X")

    else:
      jogada = obter_jogada("O")

while True:
    # exibe a matriz atual
    exibir_matriz(matriz)
    # solicita a jogada do jogador atual
    print("Jogador", jogadores[jogador_atual-1])

    if jogadores[jogador_atual-1] == 'Bot':
        linha, coluna = obter_jogada_bot('O')
    else:
        linha, coluna = obter_jogada('X')
    matriz[linha][coluna] = jogador_atual
    # verifica se houve vencedor