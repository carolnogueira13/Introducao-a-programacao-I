from math import factorial
n = int(input("Quantas linhas deseja ter no triângulo de Pasacal: "))
pascal = []
termo = []
for i in range(n):
    for j in range(i + 1):
        termo.append(factorial(i) // (factorial(j) * factorial(i - j)))
    pascal.append(termo[:])
    termo.clear()

for linha in pascal:
    for coluna in linha:
        print(f"{coluna}", end=" ")
    print()
