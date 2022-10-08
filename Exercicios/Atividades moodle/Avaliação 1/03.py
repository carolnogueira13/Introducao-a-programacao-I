# PROGRAMA PARA MOSTRAR NÚMEROS ÍMPARES DE 1 A N
n = int(input("Insira um número de 1 a 1000:"))
if 1000 > n > 0:
    print(f"O números ímpares de 1 a {n} são: ")
    for c in range(1, n+1, 2):
        print(c, end=" ")
else:
    print("Número informado fora do limite do programa.")

