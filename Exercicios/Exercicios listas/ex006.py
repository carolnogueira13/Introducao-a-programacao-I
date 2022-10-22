# PROGRAMA PARA LER 10 NÚMEROS INTEIROS, E MOSTRA DUAS LISTAS COM POSITIVOS E NEGATIVOS
numeros = [[0.0]*10, [0.0]*10]
print(numeros)
p = i = 0
for c in range(1, 11):
    n = int(input(f"Digite o {c}º número: "))
    if n > 0:
        numeros[0][p] = n
        p += 1
    elif n < 0:
        numeros[1][i] = n
        i += 1
print(f"Os números positivos digitados são: {numeros[0]}")
print(f"Os números negativos digitados são: {numeros[1]}")

# Segunda versão
'''numeros = [[], []]
for c in range(1, 11):
    n = int(input(f"Digite o {c}º número: "))
    if n >= 0:
        numeros[0].append(n)
    elif n < 0:
        numeros[1].append(n)
print(f"Os números positivos e zeros digitados são: {numeros[0]}")
print(f"Os números negativos digitados são: {numeros[1]}")'''
