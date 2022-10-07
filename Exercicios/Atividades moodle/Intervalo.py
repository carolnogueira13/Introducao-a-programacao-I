# PROGRAMA PARA INDICAR EM QUAL INTERVALO UM NÚMERO SE ENCONTRA
num = float(input('Insira um número de 0 a 100: '))
if 0 <= num <= 25:
    print('Intervalo [0,25]')

elif 25 < num <= 50:
    print('Intervalo (25,50]')

elif 50 < num <= 75:
    print('Intervalo (50,75]')

elif 75 < num <= 100:
    print('Intervalo (75,100]')

else:
    print('Fora do intervalo.')





