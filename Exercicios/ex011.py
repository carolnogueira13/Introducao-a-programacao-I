def soma(x, y):
    s = x + y
    return s


def LerNumero():
    n = int(input("Digite um numero: "))
    return n


n1 = LerNumero()
n2 = LerNumero()
print(f"A soma de {n1} e {n2} é {soma(n1, n2)}")
