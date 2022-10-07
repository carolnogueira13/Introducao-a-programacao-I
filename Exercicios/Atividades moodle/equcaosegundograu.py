# CALCULAR RAÍZES DA EQUAÇÃO DE SEGUNDO GRAU
import math
a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))
baskara = (b ** 2) - (4 * a * c)

if a == 0:
    print('Impossível de calcular!')

elif baskara < 0:
    print('Impossível de calcular!')

else:
    R = math.sqrt(baskara)
    R1 = ((- b) + R) / (2 * a)
    R2 = ((- b) - R) / (2 * a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
