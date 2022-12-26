# PROGRAMA ÁREA E PERÍMETRO
from math import pi


def area(r):
    a = pi * (r**2)
    return f"A área de um círculo de raio igual a {r}cm é {a:.2f}cm²"


def perimetro(r):
    p = 2 * pi * r
    return f"O perímetro de um círculo de raio igual a {r}cm é {p:.2f}cm"


raio = float(input("Raio do círculo (em cm): "))
print(perimetro(raio))
print(area(raio))
