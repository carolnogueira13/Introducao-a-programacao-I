# PROGRAMA PARA PRODUZIR A MATRIZ IDENTIDADE
matriz_id = [[0]*3, [0]*3, [0]*3]
for linha in range(0, 3):
    for coluna in range(0, 3):
        if linha == coluna:
            matriz_id[linha][coluna] = 1

print("MATRIZ IDENTIDADE")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz_id[linha][coluna]:^5}]", end="")
    print()

