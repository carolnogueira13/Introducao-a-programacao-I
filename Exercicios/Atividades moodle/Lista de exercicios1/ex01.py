# PROGRAMA QUE LEIA A MEDIDA DE UM RAIO E EFETUA O CÁLCULO DA ÁREA, EXIBINDO O RESULTADO NO FINAL
import math
raio = float(input("Insira o valor do raio do círculo (em cm): "))
area = math.pi * (raio ** 2)
print(f"A área desse círculo é {area:.1f}.")

