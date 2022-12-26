# PROGRAMA JOGA DA VELHA ESQUISITO
matriz = [[0.0]*3, [0.0]*3, [0.0]*3]
diagonal = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor na posição [{linha}][{coluna}]: "))
        if linha == coluna:
            diagonal += matriz[linha][coluna]
print("-"*40)
print("Matriz direta:")
for linha in range(3):
    print(f"{matriz[linha][0]}|{matriz[linha][1]}|{matriz[linha][2]}")
print(f"A soma da diagonal principal é: {diagonal}")
print("-"*40)
print("Matriz invertida:")
for linha in range(2, -1, -1):
    print(f"{matriz[linha][2]}|{matriz[linha][1]}|{matriz[linha][0]}")
print(f"A soma da diagonal principal é: {diagonal}")
