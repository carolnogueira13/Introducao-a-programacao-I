# Incremente o programa anterior lendo os 9 dados dos jogadores. Jogador 1 é “X” e o jogador 2 é o “O”.
# A cada leitura imprima o tabuleiro. O programa termina após a leitura da 9ª jogada.

jogo = [[" "]*3, [" "]*3, [" "]*3]
for i in range(3):
    print(f"{jogo[0][i]:3}|{jogo[1][i]:3}|{jogo[2][i]:3}")
    if i < 2:
        print("---*---*---")

