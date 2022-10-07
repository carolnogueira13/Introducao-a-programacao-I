# PROGRAMA PARA LER NÚMEROS COM RESTO 2
n = int(input("Insira um número: "))
cont = 1
if n < 10000:
    while cont <= 10000:
        resto = cont % n
        if resto == 2:
            print(cont)
        cont += 1
else:
    print("O programa só permite a entrada de números menores que 10.000!!")
