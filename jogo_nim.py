def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Jogada inválida! Tente novamente.")
            jogada = 0
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    # Decide quem começa
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador = 1
    else:
        print("Computador começa!")
        jogador = 0
    
    # Loop do jogo
    while n > 0:
        if jogador == 1:
            jogada = usuario_escolhe_jogada(n, m)
            print("Você tirou", jogada, "peça(s).")
            jogador = 0
        else:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou", jogada, "peça(s).")
            jogador = 1
        n -= jogada
        print("Agora restam", n, "peças no tabuleiro.")
    
    if jogador == 1:
        print("O computador ganhou!")
        return 0
    else:
        print("Você ganhou!")
        return 1

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for rodada in range(1, 4):
        print("\n**** Rodada", rodada, "****")
        vencedor = partida()
        if vencedor == 1:
            placar_usuario += 1
        else:
            placar_computador += 1
    print("\nPlacar final: Você", placar_usuario, "X", placar_computador, "Computador")

# Execução do jogo
print("Bem-vindo ao jogo do NIM! Escolha uma opção:")
print("1 - Partida única")
print("2 - Campeonato")
opcao = int(input())

if opcao == 1:
    partida()
elif opcao == 2:
    campeonato()
else:
    print("Opção inválida. Encerrando o jogo.")