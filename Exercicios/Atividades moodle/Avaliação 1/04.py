# PROGRAMA PARA CALCULAR A MÉDIA DA IDADE DE INDIVÍDUOS DE UM GRUPO
somatório = cont = 0
print("-"*60)
print("Informe a IDADE de uma pessoa [valor negativo para o programa]")
while True:
    print("-" * 60)
    print(f"{cont + 1}ª pessoa")
    idade = int(input("Idade: "))
    if idade < 0:
        break
    somatório += idade
    cont += 1
media = somatório/cont
print(f"A média de idade do grupo de {cont} pessoas é {media:.2f} anos.")

