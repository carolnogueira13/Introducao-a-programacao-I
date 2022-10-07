# Programa que leia 10 valores inteiros e encontre quantos destes valores são pares,ímpares e a média de todos os
# números.
p = 0
i = 0
media = 0

for cont in range(1, 11):
    num = int(input('Insira um valor maior que zero:'))
    resto = num % 2
    if resto == 0:
        p += 1
    else:
        i += 1
    media = media + num

print("\nNesses números informados temos {} números pares e {} números ímpares.".format(p, i))
print("A média entre esse números é {}".format(media / 10))
