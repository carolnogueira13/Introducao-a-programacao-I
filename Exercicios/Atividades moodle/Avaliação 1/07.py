# PROGRAMA PARA LER NÚMEROS COM RESTO 2
n = int(input("Insira um número: "))
limite = int(input("Digite um limite: "))
cont = 1
if 0 < n <= 10000 and 0 < limite <= 10000:
    while cont <= limite:
        resto = cont % n
        if resto == 2:
            print(cont)
        cont += 1
else:
    print("Números inseridos são inválidos!!")
