# PROGRAMA PARA CALCULAR A RAIZ QUADRADA COM UM ERRO INFERIOR A 0.00001
x = int(input("Insira um número para saber a raiz quadrada dele: "))
x0 = int(input("Insira chute inicial para o valor da raiz: "))
cont = 0
while True:
    x1 = (x0 + (x/x0))/2
    cont += 1
    if x1 == x0:
        break
    if x1 > x0 and x1 - x0 < 0.00001:
        break
    if x0 > x1 and x0 - x1 < 0.00001:
        break
    x0 = x1
print(f"O valor aproximado da raiz desse número é {x1:.5f}")
print(f"Para chegar a esse valor foram necessárias {cont} iterações")
