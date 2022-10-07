# PROGRAMA PARA SABER SE O NUM É DIVISIVEL POR 2,3 3E 6
num = int(input('Insira o número inteiro: '))
resto = num % 2
resto2 = num % 3
if resto == 0 and resto2 == 0:
    print('O número é divisível por seis!')

elif resto2 == 0:
    print('O número é divisivel por três!')

elif resto == 0:
    print('O número é divisível por dois!')

else:
    print('O número não é divisivel por dois nem por três e nem por seis!') 