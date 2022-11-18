# Escreva um programa que imprima uma matriz quadrada 3 x 3 com dados numéricos aleatórios.
# Use a função random.randint da biblioteca random.

from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = randint(0, 100)
        print(f"[{matriz[linha][coluna]:^4}]", end="")
    print()
