# PROGRAMA PARA CRIAR A MATRIZ 3*3 COM INTEIROS E MULTIPLIQUE ELES POR DOIS
matriz = [[0.0]*3, [0.0]*3, [0.0]*3]
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um número na posição [{linha}][{coluna}] "))
print("-"*30)
print("Matriz original")
for linha in range(0,3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()
print("-"*30)
print("Matriz multiplicada por dois")

matriz_duplicada = matriz[:]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz_duplicada[linha][coluna] = matriz_duplicada[linha][coluna] * 2
        print(f"[{matriz_duplicada[linha][coluna]:^5}]", end="")
    print()