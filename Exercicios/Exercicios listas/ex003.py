# PROGRAMA QUE LEIA 10 VALORES E EXIBA O MAIOR e MENOR VALOR DA LISTA
"""numeros = []
for i in range(0, 10):
    numeros.append(int(input("Insira um número: ")))
print(numeros)
print(f"O maior valor da lista é {max(numeros)}")"""

numeros = [0.0]*10
maior = 0
menor = 0
for i in range(0, 10):
    numeros[i] = int(input("Insira um número: "))
    if i == 0:
        maior = menor = numeros[i]
    elif numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
print(numeros)
print(f"O maior valor da lista é {maior}.")
print(f"O menor valor da lista é {menor}.")


