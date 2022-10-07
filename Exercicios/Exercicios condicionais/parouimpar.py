# PROGRAMA PARA IDENTIFICAR SE O NÚMERO É PAR OU ÍMPAR
num = int(input('Insira um número inteiro: '))
resto = num % 2
if resto == 0:
    print(f'{num} é um número par!')
else:
    print(f'{num} é um número ímpar!')
