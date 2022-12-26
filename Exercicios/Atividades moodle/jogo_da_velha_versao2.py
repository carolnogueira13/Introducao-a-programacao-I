# PROGRAMA PARA FAZER JOGO DA VELHA PARTE 01 + PARTE 02
# DEPOIS CONTINUAR

def imprime_tabuleiro():
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f"[{matriz_jogo[linha][coluna]:^3}]", end="")
        print()
    print()

def lin():
    linha = 0
    while linha not in {1, 2, 3}:
        linha = int(input("Escolha a linha: "))
    return linha

def col():
    coluna = 0
    while coluna not in {1, 2, 3}:
        coluna = int(input("Escolha a coluna: "))
    return coluna

def jogada(linha,coluna, jogador):
    if matriz_jogo[linha - 1][coluna - 1] == " ":
        if jogador == 1:
            matriz_jogo[linha - 1][coluna - 1] = "X"
            #cont += 1
            #break
        elif jogador == 2:
            matriz_jogo[linha - 1][coluna - 1] = "O"
            #cont += 1
            #break



matriz_jogo = [[" "] * 3, [" "] * 3, [" "] * 3]
cont = 0
vencedor = " "

# Imprimindo a matriz ajuda para o usuário
print("JOGO DA VELHA: ")
print(f"-{'1':^3}--{'2':^3}--{'3':^3}-")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz_jogo[linha][coluna]:^3}]", end="")
    print(f"-{linha + 1:^3}-")

# Fazendo as jogadas e definindo quem ganhou
while True:
    print("\nJogador X")
    while True:
        linha = lin()
        coluna = col()
        jogada(linha, coluna, 1)
    imprime_tabuleiro()

    for linha in range(0, 3):
        if matriz_jogo[linha][0] == "X" and matriz_jogo[linha][1] == "X" and matriz_jogo[linha][2] == "X":
            vencedor = "X"
            print("O vencedor é o X!")

    for coluna in range(0, 3):
        if matriz_jogo[0][coluna] == "X" and matriz_jogo[1][coluna] == "X" and matriz_jogo[2][coluna] == "X":
            vencedor = "X"
            print("O vencedor é o X!")

    if matriz_jogo[0][0] == "X" and matriz_jogo[1][1] == "X" and matriz_jogo[2][2] == "X":
        vencedor = "X"
        print("O vencedor é o X!")

    if matriz_jogo[0][2] == "X" and matriz_jogo[1][1] == "X" and matriz_jogo[2][0] == "X":
        vencedor = "X"
        print("O vencedor é o X!")

    if vencedor != " ":
        break

    if cont == 9:
        print("Deu velha")
        break

    print("Jogador O")
    while True:
        linha = lin()
        coluna = col()
        jogada(linha, coluna, 2)
    imprime_tabuleiro()

    for linha in range(0, 3):
        if matriz_jogo[linha][0] == "O" and matriz_jogo[linha][1] == "O" and matriz_jogo[linha][2] == "O":
            vencedor = "O"
            print("O vencedor é o O!")

    for coluna in range(0, 3):
        if matriz_jogo[0][coluna] == "O" and matriz_jogo[1][coluna] == "O" and matriz_jogo[2][coluna] == "O":
            vencedor = "O"
            print("O vencedor é o O!")

    if matriz_jogo[0][0] == "O" and matriz_jogo[1][1] == "O" and matriz_jogo[2][2] == "O":
        vencedor = "O"
        print("O vencedor é o O!")

    if matriz_jogo[0][2] == "O" and matriz_jogo[1][1] == "O" and matriz_jogo[2][0] == "O":
        vencedor = "O"
        print("O vencedor é o O!")

    if vencedor != " ":
        break

    if cont == 9:
        print("Deu velha!")
        break
