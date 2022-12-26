# PROGRAMA VETORES ESTRANHOS
vetor = ['']*20
soma = media = cont = menor = maior = 0
for i in range(20):
    numero = int(input("Digite um número: "))
    if numero >= 0:
        vetor[i] = numero
        soma += numero
        cont += 1
        if cont == 1:
            maior = menor = numero
        elif numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    else:
        break
media = soma/cont
print("-"*100)
print(f"""O vetor final = {vetor}
A soma dos valores = {soma}
A quantidade de valores de entrada = {cont}
A média dos valores = {media}
O maior valor = {maior}
O menor valor = {menor}""")
