# PROGRAMA PARA CALCULAR E IMPRIMIR O VALOR DE x ELEVADO A n
n = int(input("Insira o valor de n: "))
x = int(input("Insira o valor de x: "))
if n > 1:
    if x >= 2:
        result = x ** n
        print(f"O resultado de {x} elevado a {n} é {result}")
    else:
        print("Não é possível fazer a operação porque o x deve ser maior ou igual a 2.")
else:
    print("Não é possível fazer a operação porque o n deve ser maior que 1.")