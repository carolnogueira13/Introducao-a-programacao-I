# Escreva uma função que transforma qualquer ângulo dado em graus, no intervalo [0 – 360), em um ângulo em radianos.
def radianos(grau):
    from math import pi
    return (grau * pi)/180


x = float(input("Insira o valor do ângulo em graus: "))
print(f"O ângulo {x} graus corresponde a {radianos(x):.2f} radianos")
