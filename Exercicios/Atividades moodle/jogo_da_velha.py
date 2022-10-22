# PROGRAMA PARA FAZER JOGO DA VELHA PARTE 01
from random import randint

matriz_ajuda_jogo = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
matriz_jogo = [[], [], []]
jogador_x = 0
jogador_o = 0

# Imprimindo a matriz ajuda para o usuário
print("Considere essas opções do jogo: ")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz_ajuda_jogo[linha][coluna]:^3}]", end="")
    print()

# Definindo o primeiro a jogar:
primeiro = randint(0, 1)
if primeiro == 0:
    print("O jogador X começa")
    jogador_x = str(input("Escolha a posição para jogar: "))
else:
    print("O jogador O começa")
    jogador_o = str(input("Escolha a posição para jogar: "))
