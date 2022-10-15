# LISTA DE 20 INTEIROS, QUANTOS NÚMEROS PARES E IMPRIMA ESSA QUANTIDADE E O VETOR INTEIRO
numeros = list()
pares = 0
for n in range(0, 20):
    numeros.append(int(input("Digite um número: ")))
    if numeros[-1] % 2 == 0:
        pares += 1
print(f"A lista de números é: {numeros}")
print(f"A lista possui {pares} números pares")


