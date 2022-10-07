# PROGRAMA QUE IMPRIMA OS 100 PRIMEIROS NÚMEROS ÍMPARES
num = cont = 1
print("Os 100 primeiros números ímpares são: ")
while cont <= 100:  # Um contador para determinar os 100 primeiros números
    print(num)
    num += 2  # Para aumentar de 2 em 2, a partir do número 1 e pegar apenas os números ímpares
    cont += 1
