# PROGRAMA PARA CALCULAR O FATORIAL DE UM NÚMERO POSITIVO
# Esse exercício possui três formas de fazer, irei fazer as três, mas deixar duas como comentário e apenas uma rodando

# 1ª forma usando o for
n = int(input("Digite um número positivo: "))
if n < 1:
    print("O número digitado está inválido, digite um número positivo.")
else:
    fatorial = 1
    print(f"{n}! =", end=" ")
    for c in range(n, 0, -1):
        print(f"{c} *" if c != 1 else f"{c}", end=" ")
        fatorial = fatorial * c
    print(f"= {fatorial}")

# 2ª forma usando o while
"""n = int(input("Digite um número positivo: "))
if n < 1:
    print("O número digitado está inválido, digite um número positivo.")
else:
    fatorial = 1
    print(f"{n}! =", end=" ")
    c = n
    while c >= 1:
        print(f"{c} *" if c != 1 else f"{c}", end=" ")
        fatorial = fatorial * c
        c -= 1
    print(f"= {fatorial}")"""

# 3ª forma fazendo o cálculo do fatorial com a biblioteca math
"""import math

n = int(input("Digite um número positivo: "))
if n < 1:
    print("O número digitado está inválido, digite um número positivo.")
else:
    fatorial = math.factorial(n)  # Usar a função math.factorial para fazer o cálculo do fatorial
    print(f"{n}! =", end=" ")
    while n >= 1:  # Esse while é apenas para deixar a formatação do print final bonita!
        print(f"{n} *" if n != 1 else f"{n}", end=" ")
        n -= 1
print(f"= {fatorial}")"""
