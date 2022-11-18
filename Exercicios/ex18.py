# Escreva um programa que imprima uma matriz quadrada 3 x 3 com dados numéricos preenchidos.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("-"*20)
print("A MATRIZ É: ")
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^3}]", end="")
    print()
print("-"*20)
