# PROGRAMA COM A FUNÇÃO POTÊNCIA
def potencia(base, exp):
    pot = 1
    for c in range(exp):
        pot *= base
    return pot


# Programa principal
a = int(input("Digite a base da potência: "))
b = int(input("Digite o expoente da potência: "))
print(f"{a} elevado a {b} = {potencia(a, b)}")

