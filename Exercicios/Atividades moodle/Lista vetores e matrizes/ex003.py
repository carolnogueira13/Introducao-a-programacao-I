matriz = [[0.0]*3, [0.0]*3, [0.0]*3]
diagonal = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Indique o valor da matriz na posição [{linha}][{coluna}]: "))
        if linha == coluna:
            diagonal += matriz[linha][coluna]
    print()

print("A matriz gerada foi: ")
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^3}]", end="")
    print()

print(f"O valor da diagonal principal dessa matriz formada é {diagonal}")