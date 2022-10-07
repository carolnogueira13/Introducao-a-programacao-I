# PROGRAMA QUE CALCULE A HIPOTENUSA DO TRIÂNGULO RETÂNGULO
print("-" * 50)
print("CÁLCULO DA HIPOTENUSA DO TRIÂNGULO RETÂNGULO")
print("-" * 50)
print("Informe o valor dos catetos:")
a = float(input("Cateto a: "))
b = float(input("Cateto b: "))
print("-" * 50)
hip = ((a ** 2 + b ** 2)) **(1/2)  # Primeira forma de calcular
print("O valor da hipotenusa de um triãngulo retângulo com "
      f"os cateto {a} e {b} é {hip:.2f}")

"""from math import hypot

hip = hypot(a, b)  # Segunda forma de calcular
print("O valor da hipotenusa de um triãngulo retãngulo com "
      f"os cateto {a} e {b} é {hip}")"""
