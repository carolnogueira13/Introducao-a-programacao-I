# PROGRAMA PARA IMPRIMIR A TABUADA DE UM VALOR
tab = int(input('Indique o número que você quer a tabuada: '))
for cont in range(0, 11):
    print('{} * {} = {}' .format(tab, cont, tab*cont))


