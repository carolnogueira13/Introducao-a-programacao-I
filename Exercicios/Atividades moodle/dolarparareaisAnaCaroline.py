# PROGRAMA PARA CONVERTER UM VALOR EM DOLARES PARA REAL
dol = float(input('Insira quantos dólares você possui: US$ '))
conv = float(input('Indique qual o valor da cotação do dia de dólares para reais: '))
real = dol * conv
print('Você possui {} dólares que equivalem a {} reais.'.format(dol, real))

