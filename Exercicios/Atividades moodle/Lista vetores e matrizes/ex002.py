matriz = [[0]*3, [0]*3, [0]*3]
soma = [0, 0, 0]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Indique o valor da matriz na posição [{linha}][{coluna}]: "))
        soma[linha] += matriz[linha][coluna]
    print()

print("A matriz gerada foi: ")
for linha in range(0,3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^3}]", end="")
    print()
print()
print("E a matriz SOMA gerada é: ")
for c in soma:
    print(f"[{c:^4}]")
