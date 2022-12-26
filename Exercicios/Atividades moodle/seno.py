# PROGRAMA CALCULO DE SENO
from math import factorial, sin, radians


def seno(angulo):
    n = sen = 0
    while True:
        sen += ((-1) ** n / factorial((2 * n) + 1)) * angulo ** ((2 * n) + 1)
        termo = ((-1) ** n / factorial((2 * n) + 1)) * angulo ** ((2 * n) + 1)
        if termo < 0:
            termo = -termo
        if termo < 0.00001:
            break
        n += 1
    return sen


# Programa principal:
x = int(input("Insira o valor do ângulo em graus: "))
rad = radians(x)
s = seno(rad)

print(f"Utizando a função seno criada - O seno de {x}º é {s:.3f} ")
print(f"Utiliando a função seno da biblioteca math - O seno de {x}º é {sin(rad):.3f}")
