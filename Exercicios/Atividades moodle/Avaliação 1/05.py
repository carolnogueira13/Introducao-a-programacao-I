# PROGRAMA PARA CALCULAR OS DIVISORES DE n
n = int(input("Insira um número: "))
cont = 1
print(f"Os divisores de {n} são: ")
while cont <= n:
    resto = n % cont
    if resto == 0:
        print(cont)
    cont += 1

