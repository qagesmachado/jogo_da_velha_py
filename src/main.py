## Biblioteca usadas
import random

## Criação e print do tabuleiro

# Cria o tabuleiro
def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

tabuleiro = criar_tabuleiro()

# Imprime o tabuleiro, colocando cada lista interna presente na matriz tabuleiro em uma linha diferente
def imprimir_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))

## Verificação de empate/vitória

# Verifica se alguem ganhou
def jogo_acabou():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return True

# Verifica se o jogador/bot X ganhou
def jogo_acabou1():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == 'X':
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == 'X':
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
        return True

# Verifica se o jogador/bot O ganhou   
def jogo_acabou2():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == 'O':
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == 'O':
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
        return True
    
# Verifica se não tem mais lugares para jogar
def empate():
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    else:
        return True

## Jogadores

# Jogador X
def jogada_jogador1():
    while True:
        try:
            if teclado == 1:
                # Referência
                print('-----')
                print('7|8|9')
                print('4|5|6')
                print('1|2|3\n')
            # Pergunta a posição que o jogador deseja colocar (Baseado no teclado númerico)
            entradadedados = int(input('•Use o teclado númerico como referência•\nDigite o local Jogador (X): '))
            # Transforma o número em um posição na matriz tabuleiro
            if entradadedados == 1:
                linha = 2
                coluna = 0
            elif entradadedados == 2:
                linha = 2 
                coluna = 1
            elif entradadedados == 3:
                linha = 2 
                coluna = 2
            elif entradadedados == 4:
                linha = 1
                coluna = 0       
            elif entradadedados == 5:
                linha = 1
                coluna = 1
            elif entradadedados == 6:
                linha = 1
                coluna = 2   
            elif entradadedados == 7:
                linha = 0
                coluna = 0
            elif entradadedados == 8:
                linha = 0
                coluna = 1      
            elif entradadedados == 9:
                linha = 0
                coluna = 2
            else:
                # Caso o jogador informe um número negativo ou maior que 9
                print('Insira números entre 1 e 9')
            # Verifica se a posição selecionada está vazia
            if tabuleiro[linha][coluna] == ' ':
                # Posiciona no lugar que o jogador indicou
                tabuleiro[linha][coluna] = 'X'
                return True
            else:
                # Informa que o jogador colocou em lugar que já foi usado
                print('Essa posição já está ocupada!')
                imprimir_tabuleiro()
        except:
            # Caso o jogador coloque letra ou não insira números inteiros
            print('Entrada Inválida')
            imprimir_tabuleiro()

# Jogador O
def jogada_jogador2():
    while True:
        try:
            if teclado == 1:
                # Referência
                print('-----')
                print('7|8|9')
                print('4|5|6')
                print('1|2|3\n')
            # Pergunta a posição que o jogador deseja colocar (Baseado no teclado númerico)
            entradadedados = int(input('•Use o teclado númerico como referência•\nDigite o local Jogador 2 (O): '))
            # Transforma o número em um posição na matriz
            if entradadedados == 1:
                linha = 2
                coluna = 0
            elif entradadedados == 2:
                linha = 2 
                coluna = 1
            elif entradadedados == 3:
                linha = 2 
                coluna = 2
            elif entradadedados == 4:
                linha = 1
                coluna = 0       
            elif entradadedados == 5:
                linha = 1
                coluna = 1
            elif entradadedados == 6:
                linha = 1
                coluna = 2   
            elif entradadedados == 7:
                linha = 0
                coluna = 0
            elif entradadedados == 8:
                linha = 0
                coluna = 1      
            elif entradadedados == 9:
                linha = 0
                coluna = 2
            else:
                # Caso o jogador informe um número negativo ou maior que 9
                print('Insira números entre 1 e 9')
            # Verifica se a posição selecionada está vazia
            if tabuleiro[linha][coluna] == ' ':
                # Posiciona no lugar que o jogador indicou
                tabuleiro[linha][coluna] = 'O'
                return True
            else:
                # Informa que o jogador colocou em lugar que já foi usado
                print('Essa posição já está ocupada!')
                imprimir_tabuleiro()
        except:
            # Caso o jogador coloque letra ou não insira números inteiros
            print('Entrada Inválida')
            imprimir_tabuleiro()

## Jogadas dos Bots

# Jogada aleatoria
def jogada_aleatoria(var):
    # Caso nenhuma jogada necessite ser feita, escolhe uma posição aleatória
    while True:
            if empate():
                break
            else:    
                linha = random.randint(0, 2)
                coluna = random.randint(0, 2)
                if tabuleiro[linha][coluna] == ' ':
                    tabuleiro[linha][coluna] = var
                    return True

# Jogada tentando bloquear e ganhar
def jogadas_medias(var1,var2):
    # Verifica se o bot pode ganhar o jogo nas linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == var1 and tabuleiro[i][2] == ' ':
            tabuleiro[i][2] = var1
            return True
        if tabuleiro[i][0] == tabuleiro[i][2] == var1 and tabuleiro[i][1] == ' ':
            tabuleiro[i][1] = var1
            return True
        if tabuleiro[i][1] == tabuleiro[i][2] == var1 and tabuleiro[i][0] == ' ':
            tabuleiro[i][0] = var1
            return True
    # Verifica se o bot pode ganhar o jogo nas colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == var1 and tabuleiro[2][i] == ' ':
            tabuleiro[2][i] = var1
            return True
        if tabuleiro[0][i] == tabuleiro[2][i] == var1 and tabuleiro[1][i] == ' ':
            tabuleiro[1][i] = var1
            return True
        if tabuleiro[1][i] == tabuleiro[2][i] == var1 and tabuleiro[0][i] == ' ':
            tabuleiro[0][i] = var1
            return True
    # Verifica se o bot pode ganhar o jogo na diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == var1 and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = var1
        return True
    if tabuleiro[0][0] == tabuleiro[2][2] == var1 and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True
    if tabuleiro[1][1] == tabuleiro[2][2] == var1 and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = var1
        return True
    # Verifica se o bot pode ganhar o jogo na diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == var1 and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = var1
        return True
    if tabuleiro[0][2] == tabuleiro[2][0] == var1 and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True
    if tabuleiro[1][1] == tabuleiro[2][0] == var1 and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = var1
        return True
    # Verifica se o bot precisa bloquear a jogada do oponente nas linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == var2 and tabuleiro[i][2] == ' ':
            tabuleiro[i][2] = var1
            return True
        if tabuleiro[i][1] == tabuleiro[i][2] == var2 and tabuleiro[i][0] == ' ':
            tabuleiro[i][0] = var1
            return True
        if tabuleiro[i][0] == tabuleiro[i][2] == var2 and tabuleiro[i][1] == ' ':
            tabuleiro[i][1] = var1
            return True
    # Verifica se o bot precisa bloquear a jogada do oponente nas colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == var2 and tabuleiro[2][i] == ' ':
            tabuleiro[2][i] = var1
            return True
        if tabuleiro[0][i] == tabuleiro[2][i] == var2 and tabuleiro[1][i] == ' ':
            tabuleiro[1][i] = var1
            return True
        if tabuleiro[1][i] == tabuleiro[2][i] == var2 and tabuleiro[0][i] == ' ':
            tabuleiro[0][i] = var1
            return True
    # Verifica se o bot precisa bloquear a jogada do oponente na diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == var2 and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = var1
        return True
    if tabuleiro[0][0] == tabuleiro[2][2] == var2 and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True
    if tabuleiro[1][1] == tabuleiro[2][2] == var2 and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = var1
        return True
    # Verifica se o bot precisa bloquear a jogada do oponente na diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == var2 and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = var1
        return True
    if tabuleiro[0][2] == tabuleiro[2][0] == var2 and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True
    if tabuleiro[1][1] == tabuleiro[2][0] == var2 and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = var1
        return True

# Jogadas predeterminadas bot O
def jogadas_impossiveis(var1,var2):
    # Vê se o bot consegue colocar no meio na primeira jogada
    if tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True

    # Gera uma posição em uma das quinas
    padrao = (0,2)
    lin = random.choice(padrao)
    col = random.choice(padrao)
    # Coloca a primeira jogada na quina caso o oponente tenha colocado no meio
    if tabuleiro[1][1] == var2 and tabuleiro[0][0] == tabuleiro[0][2] == tabuleiro[2][0] == tabuleiro[2][2] == ' ':
        tabuleiro[lin][col] = var1
        return True

    # Se o bot tiver jogado no meio
    if tabuleiro[1][1] == var1:
        # Evita o oponente de ganhar no modelo exemplo:
        #   _ | X | _
        #   _ | O | X
        #   _ | _ | _
        if tabuleiro[0][1] == tabuleiro[1][2] == var2 and tabuleiro[0][2] == ' ':
            tabuleiro[0][2] = var1
            return True
        if tabuleiro[0][1] == tabuleiro[1][0] == var2 and tabuleiro[0][0] == ' ':
            tabuleiro[0][0] = var1
            return True
        if tabuleiro[2][1] == tabuleiro[1][2] == var2 and tabuleiro[2][0] == ' ':
            tabuleiro[2][2] = var1
            return True
        if tabuleiro[2][1] == tabuleiro[1][0] == var2 and tabuleiro[2][2] == ' ':
            tabuleiro[2][0] = var1
            return True
        
        # Evita o oponente de ganhar no modelo exemplo:
        #   _ | _ | X
        #   _ | O | _
        #   _ | X | _
        if tabuleiro[0][0] == tabuleiro[2][1] == var2 and tabuleiro[1][0] == tabuleiro[2][0] == ' ':
            tabuleiro[random.randint(1,2)][0] = var1
            return True
        if tabuleiro[0][0] == tabuleiro[1][2] == var2 and tabuleiro[0][1] == tabuleiro[0][2] == ' ':
            tabuleiro[0][random.randint(1,2)] = var1
            return True
        if tabuleiro[0][2] == tabuleiro[1][0] == var2 and tabuleiro[0][0] == tabuleiro[0][1] == ' ':
            tabuleiro[0][random.randint(0,1)] = var1
            return True
        if tabuleiro[0][2] == tabuleiro[2][1] == var2 and tabuleiro[1][2] == tabuleiro[2][2] == ' ':
            tabuleiro[random.randint(0,1)][2] = var1
            return True
        if tabuleiro[2][0] == tabuleiro[0][1] == var2 and tabuleiro[0][0] == tabuleiro[1][0] == ' ':
            tabuleiro[random.randint(0,1)][0] = var1
            return True
        if tabuleiro[2][0] == tabuleiro[1][2] == var2 and tabuleiro[2][1] == tabuleiro[2][2] == ' ':
            tabuleiro[2][random.randint(1,2)] = var1
            return True
        if tabuleiro[2][2] == tabuleiro[1][0] == var2 and tabuleiro[2][0] == tabuleiro[2][1] == ' ':
            tabuleiro[2][random.randint(0,1)] = var1
            return True
        if tabuleiro[2][2] == tabuleiro[0][1] == var2 and tabuleiro[0][2] == tabuleiro[1][2] == ' ':
            tabuleiro[random.randint(0,1)][2] = var1
            return True
        
        # Joga em posições adjacentes ao meio caso o oponente tenha jogado na diagonal
        if tabuleiro[0][0] == var2 and tabuleiro[1][0] == tabuleiro[0][1] == ' ':
            alea = (0,1)
            while True:    
                l = random.choice(alea)
                c = random.choice(alea)
                if l != c:
                    if tabuleiro[l][c] == ' ':
                        tabuleiro[l][c] = var1
                        return True
        if tabuleiro[0][2] == var2 and tabuleiro[0][1] == tabuleiro[1][2] == ' ':
            alea = (0,1)
            alea2 = (1,2)
            while True:    
                l = random.choice(alea)
                c = random.choice(alea2)
                if l == 0 and c == 1 or l == 1 and c == 2:
                    if tabuleiro[l][c] == ' ':
                        tabuleiro[l][c] = var1
                        return True
        if tabuleiro[2][0] == var2 and tabuleiro[1][0] == tabuleiro[2][1] == ' ':
            alea = (1,2)
            alea2 = (0,1)
            while True:    
                l = random.choice(alea)
                c = random.choice(alea2)
                if l == 1 and c == 0 or l == 2 and c == 1:
                    if tabuleiro[l][c] == ' ':
                        tabuleiro[l][c] = var1
                        return True
        if tabuleiro[2][2] == var2 and tabuleiro[2][1] == tabuleiro[1][2] == ' ':
            alea = (1,2)
            while True:    
                l = random.choice(alea)
                c = random.choice(alea)
                if l != c:
                    if tabuleiro[l][c] == ' ':
                        tabuleiro[l][c] = var1
                        return True

    # Função para tentar jogar em uma das quinas
    def diagonal():
        while True:
            lin = random.choice(padrao)
            col = random.choice(padrao)
            if tabuleiro[lin][col] == ' ':
                tabuleiro[lin][col] = var1
                return True
            
    # Coloca a segunda jogada em outra quina caso o oponente tenha coloca no lado oposto ao bot
    if tabuleiro[0][0] == var1 and tabuleiro[2][2] == var2 and tabuleiro[0][2] == tabuleiro[2][0] == ' ':
        if diagonal():
            return True
    elif tabuleiro[0][2] == var1 and tabuleiro[2][0] == var2 and tabuleiro[2][2] == tabuleiro[0][0] == ' ':
        if diagonal():
            return True
    elif tabuleiro[2][0] == var1 and tabuleiro[0][2] == var2 and tabuleiro[2][2] == tabuleiro[0][0] == ' ':
        if diagonal():
            return True
    elif tabuleiro[2][2] == var1 and tabuleiro[0][0] == var2 and tabuleiro[0][2] == tabuleiro[2][0] == ' ':
        if diagonal():
            return True
        
    else:
        if jogada_aleatoria(var1):
            return True

def jogada_com_estrategia(var1,var2):
    if dificuldade2 > 1:
        if jogadas_medias(var1,var2):
            return True
    if dificuldade2 == 2:
        if jogada_aleatoria(var1):
            return True
    if dificuldade2 == 3:
        if jogadas_impossiveis(var1,var2):
            return True    

# Jogadas predeterminadas bot X
def jogadas_impossiveis2(var1,var2):
    # Faz com que o bot tenha a chance começar ou não no meio
    aleatorio = random.randint(1,2)
    if aleatorio == 1 and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True
    
    # Função que tenta jogar em uma das quinas
    padrao = (0,2)
    def diagonal():
        while True:
            lin = random.choice(padrao)
            col = random.choice(padrao)
            if tabuleiro[lin][col] == ' ':
                tabuleiro[lin][col] = var1
                return True
            
    # Joga a segunda jogada no meio        
    dado = 1
    for i in range(3):
        if tabuleiro[0][i] == var1 or tabuleiro[1][i] or tabuleiro[2][i]:
            dado = 0
    if dado == 0 and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = var1
        return True
    
    # Coloca a primeira jogada na quina caso o oponente tenha colocado no meio
    if tabuleiro[1][1] == var2 and tabuleiro[0][0] == ' ' or tabuleiro[0][2] == ' ' or tabuleiro[2][0] == ' ' or tabuleiro[2][2] == ' ':
        if diagonal():
            return True
    
    else:
        if jogada_aleatoria('X'):
            return True

def jogada_com_estrategia2(var1,var2):
    if dificuldade1 > 1:
        if jogadas_medias(var1,var2):
            return True
    if dificuldade1 == 2:
        if jogada_aleatoria(var1):
            return True
    if dificuldade1 == 3:
        if jogadas_impossiveis2(var1,var2):
            return True

## Bots
                
# Bot X     
def jogada_bot1():
    # Dificuldade Fácil o bot só joga aleatorio
    if dificuldade1 == 1:
        if jogada_aleatoria('X'):
            return True    
    # Dificuldade Média o
    if dificuldade1 > 1:
        if jogada_com_estrategia2('X','O'):
            return True
        
# Bot O
def jogada_bot2():
    # Dificuldade Fácil o bot só joga aleatorio
    if dificuldade2 == 1:
        if jogada_aleatoria('O'):
            return True
    else:
        if jogada_com_estrategia('O','X'):
            return True

## Modos de jogo

# Jogador vs Jogador
def pvp():
    while True:
        imprimir_tabuleiro()
        if empate():
            imprimir_tabuleiro()
            print('Empate!\n')
            break     
        if jogada_jogador1():
            if jogo_acabou1():
                imprimir_tabuleiro()
                print('Jogador 1 venceu\n')
                break
            else:
                if not empate():
                    imprimir_tabuleiro()
                    if jogada_jogador2():
                        if jogo_acabou2():
                            imprimir_tabuleiro()
                            print('Jogador 2 venceu\n')
                            break
                else:
                    imprimir_tabuleiro() 
                    print('Empate!')
                    break

# Jogador vs Máquina
def pvb():
    while True:
        imprimir_tabuleiro()
        if empate():
            imprimir_tabuleiro()
            print('Empate!\n')
            break     
        if jogada_jogador1():
            if jogo_acabou1():
                imprimir_tabuleiro()
                print('Você venceu\n')
                break
            else:
                if not empate():
                    if jogada_bot2():
                        if jogo_acabou2():
                            imprimir_tabuleiro()
                            print('O bot venceu\n')
                            break
                else:
                    imprimir_tabuleiro() 
                    print('Empate!\n')
                    break

# Máquina vs Jogador
def bvp():
    while True:
        if empate():
            imprimir_tabuleiro()
            print('Empate!\n')
            break     
        if jogada_bot1():
            imprimir_tabuleiro()
            if jogo_acabou1():
                print('O bot venceu\n')
                break
            else:
                if not empate():
                    if jogada_jogador2():
                        if jogo_acabou2():
                            imprimir_tabuleiro()
                            print('Você venceu\n')
                            break
                else:
                    imprimir_tabuleiro() 
                    print('Empate!\n')
                    break

# Máquina vs Máquina
def bvb():
    while True:
        imprimir_tabuleiro() 
        if empate():
            print('- - -')
            imprimir_tabuleiro()
            print('Empate!\n')
            break   
        if jogada_bot1():
            if jogo_acabou1():
                    print('- - -')
                    imprimir_tabuleiro()
                    print('Bot X venceu\n')
                    break
            else:
                if not empate():
                    if jogada_bot2():
                        if jogo_acabou2():
                            print('- - -')
                            imprimir_tabuleiro()
                            print('Bot O venceu\n')
                            break
                else:
                    print('- - -')
                    imprimir_tabuleiro()
                    print('Empate!\n')
                    break
        print('- - -')

## Execução do menu e jogo da velha

while True:
    #Reseta o tabuleiro
    tabuleiro = criar_tabuleiro()

    # Pergunta qual modo de jogo a pessoa deseja jogar
    menu = input('Modo de jogo\na = PvP\nb = PvB\nc = BvB\nInsira: ')

    # Executa o jogo de acordo com a opção selecionada
    if menu == 'a':
        while True:
            tecladonum = input('Você tem teclado númerico S ou N: ')
            if tecladonum == 'S' or tecladonum == 's':
                teclado = 0
                break
            elif tecladonum == 'N' or tecladonum == 'n':
                teclado = 1
                break
            else:
                print('Entrada Inválida')
        pvp()

    elif menu == 'b':
        while True:
            tecladonum = input('Você tem teclado númerico S ou N: ')
            if tecladonum == 'S' or tecladonum == 's':
                teclado = 0
                break
            elif tecladonum == 'N' or tecladonum == 'n':
                teclado = 1
                break
            else:
                print('Entrada Inválida')
        while True:
            try:
                dificuldade = int(input('Dificuldade do bot (1-3): '))
            except:
                print('Entrada Inválida')
            else:
                while True:
                    primeiro = input('Você deseja começar primeiro S ou N: ')
                    if primeiro == 'S' or primeiro == 's':
                        dificuldade2 = dificuldade
                        pvb()
                        break
                    elif primeiro == 'N' or primeiro == 'n':
                        dificuldade1 = dificuldade
                        bvp()
                        break
                    else:
                        print('Entrada Inválida')
            break

    elif menu == 'c':
        while True:
            empates = 0
            vitoriaX = 0
            vitoriaO = 0
            try:
                dificuldade1 = int(input('Dificuldade do bot X (1-3): '))
                dificuldade2 = int(input('Dificuldade do bot O (1-3): '))
                jogadas = int(input('Número de jogos a serem feitos: '))
            except:
                print('Entrada Inválida')
            else:
                jogo = 1
                while jogo <= jogadas:
                    tabuleiro = criar_tabuleiro()
                    bvb()
                    if empate():
                        empates += 1
                    elif jogo_acabou1():
                        vitoriaX += 1
                    elif jogo_acabou2():
                        vitoriaO += 1
                    jogo += 1
                else:
                    print(f'Empates: {empates}\nX ganhou: {vitoriaX}\nO ganhou: {vitoriaO}\n')
                break
    
    # Caso a pessoa tenha informado algo que não esta no menu
    else:
        print('Entrada Inválida')
