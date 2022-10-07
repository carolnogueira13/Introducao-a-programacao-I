# PROGRAMA PARA LER 10 VALORES INTEIROS E PARA CADA VALOR INFORMAR SE É PAR OU IMPAR
for cont in range(1, 11):
    print('\n--Número {}--'.format(cont))
    num = int(input('Indique um valor inteiro: '))
    resto = num % 2
    if resto == 0:
        print('{} é par!'.format(num))
    else:
        print('{} é ímpar!'.format(num))
