# PROGRAMA QUE IMPRIMA OS NÚMEROS PARES ENTRE 85 E 907. E A SOMA DESSES VALORES.
num = 86 # Primeiro número par entre 85 e 907
soma = 0
while num <= 906: # Último número par entre 85 e 907
    print(num)
    soma = soma + num
    num += 2

print(f"A soma de todos os números pares entre 85 e 907 é igual a {soma}")
    