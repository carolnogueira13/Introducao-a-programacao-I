#Escreva um programa que imprima um tabuleiro preenchido do jogo da velha no formato abaixo.
# Use uma matriz quadrada 3x3 com dados preenchidos como “X” e ”O” para armazenar os dados.

jogo = [["O"]*3, ["X"]*3, ["O"]*3]
for linha in range(3):
    for coluna in range(3):
        if coluna < 2:
            print(f"{jogo[linha][coluna]:^3}", end="|")
        else:
            print(f"{jogo[linha][coluna]:^3}", end="")

    print()
    print("---*---*---")

