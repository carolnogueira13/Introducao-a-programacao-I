# PROGRAMA PARA CALCULAR QUADRADO DO NÚMERO
num = int(input("Informe um número - O para sair: "))
while num != 0:
    quad = num * num
    print("O quadrado de {} è {}" .format(num, quad))
    num = int(input("\nInforme um número - O para sair: "))

