# SOMA DE MATRIZES
# Definindo as variaveis
matriz1 = [[], [], []]
matriz2 = [[], [], []]
matriz_soma = [[], [], []]
matriz_ajuda = [["[0][0]", "[0][1]", "[0][2]"], ["[1][0]", "[1][1]", "[1][2]"], ["[2][0]", "[2][1]", "[2][2]"]]

# Ajudando o usuário
print("Considere as posições dessa matriz 3X3 como base")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"{matriz_ajuda[linha][coluna]:^5}    ", end="")
    print()
print()
# Contruindo as matrizes
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz1[linha].append(int(input(f"Digite um número da matriz 1 na posição [{linha}][{coluna}]:  ")))
print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz2[linha].append(int(input(f"Digite um número da matriz 2 na posição [{linha}][{coluna}]:  ")))

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz_soma[linha].append(matriz1[linha][coluna] + matriz2[linha][coluna])

# Imprimindo as matrizes geradas
print("-" * 30)
print("Matriz 1")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz1[linha][coluna]:^5}]", end="")
    print()

print("-" * 30)
print("Matriz 2")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz2[linha][coluna]:^5}]", end="")
    print()

print("-" * 30)
print("Matriz SOMA")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz_soma[linha][coluna]:^5}]", end="")
    print()
