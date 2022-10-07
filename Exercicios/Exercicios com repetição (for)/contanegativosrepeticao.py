# PROGRAMA QUE LÊ 10 VALORES INTEIROS PARA A VARIAVEL “a” E CONTA QUANTOS VALORES SÃO NEGATIVOS EXIBINDO NA TELA

n = 0
z = 0
p = 0

for cont in range(1, 11):
    a = int(input('Insira o valor de a: '))
    if a < 0:
        n = n + 1
    elif a == 0:
        z = z + 1
    else:
        p = p + 1

print('Nesse conjunto de números o usuário inseriu {} números negativos.' .format(n))
print('Nesse conjunto de números o usuário inseriu {} números iguais a zero.' .format(z))
print('Nesse conjunto de números o usuário inseriu {} números positivo.' .format(p))

