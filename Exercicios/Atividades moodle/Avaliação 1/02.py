# PROGRAMA PARA DETERMINAR SE UM TRIÂNGULO É RETÂNGULO OU NÃO
print("-" * 30)
print("Informe os lados do triângulo: ")
a = float(input("1º lado: "))
b = float(input("2º lado: "))
c = float(input("3º lado: "))
if c == (a ** 2 + b ** 2)**(1 / 2) or b == (a ** 2 + c ** 2)**(1/2) or a == (b ** 2 + c ** 2)**(1/2):
    print(f"Os lados {a}, {b} e {c} formam um triângulo retângulo.")
else:
    print(f"Os lados {a}, {b} e {c} não formam um triângulo retângulo.")