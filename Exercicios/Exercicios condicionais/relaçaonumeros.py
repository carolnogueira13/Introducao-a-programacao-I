# PROGRAMA PARA IDENTIFICAR A RELAÇÃO DE DOIS NÚMEROS
num1 = int(input('Insira um primeiro número inteiro: '))
num2 = int(input('Insira o sugundo número inteiro: '))
if num1 == num2:
    print('Os números são iguais!')
else:
    if num1 > num2:
        print('O primeiro número é maior que o segundo!')
    else:
        print('O segundo número é maior que o primeiro!')