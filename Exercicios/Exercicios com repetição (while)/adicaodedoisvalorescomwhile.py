# PROGRAMA UTILIZANDO A ESTRUTURA WHILE, QUE PERMITA O USUÁRIO FAZER CONTAS DE ADIÇÃO DE DOIS VALORES
num1 = float(input("Insira um número (digite 0 para parar o programa): "))
num2 = float(input("Insira um número (digite 0 para parar o programa): "))
while num1 != 0 and num2 != 0:
    soma = num1 + num2
    print("A soma dos dois números informados é {}" .format(soma))
    num1 = float(input("\nInsira um número (digite 0 para parar o programa): "))
    num2 = float(input("Insira um número (digite 0 para parar o programa): "))