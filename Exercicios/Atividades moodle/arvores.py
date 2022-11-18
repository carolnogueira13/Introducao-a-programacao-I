n = int(input("Você quer quantas linhas na sua árvore? "))
arvoreSimples = []
arvoreCompleta = []
for i in range(0, n):
    arvoreSimples.append("*" * (i+1))
    arvoreCompleta.append("*" * ((2 * i) + 1))

print(f"\na) Arvore cortada com {n} linhas")
for linha in arvoreSimples:
    print(linha)
print(f"\nb) Arvore completa com {n} linhas")
for linha in arvoreCompleta:
    print(f"{linha:^{(2*n) + 1}}")
