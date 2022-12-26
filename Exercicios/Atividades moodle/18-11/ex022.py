# Escreva uma função que recebe três parâmetros que representam os lados de um triângulo.
# A função deve retornar:
# 0 se os valores não correspondem a um triângulo;
# 1 se correspondem a um triângulo equilátero;
# 2 se correspondem a um triângulo isósceles;
# 3 se correspondem a um triângulo escaleno.

def triangulo(a, b, c):
    if a < b + c and b < a + c and c < b + a:
        if a == b and b == c:
            return 1
        elif a == b or b == c or c == a:
            return 2
        else:
            return 3
    else:
        return 0


lado1 = float(input("Entre com o 1º valor: "))
lado2 = float(input("Entre com o 2º valor: "))
lado3 = float(input("Entre com o 3º valor: "))
resultado = triangulo(lado1, lado2, lado3)
if resultado == 0:
    print("Não é triângulo!")
elif resultado == 1:
    print("É um triângulo equilátero")
elif resultado == 2:
    print("É um triângulo isosceles")
elif resultado == 3:
    print("É um triângulo escaleno")
