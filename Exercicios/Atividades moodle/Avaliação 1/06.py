# PROGRAMA POSTO DE GASOLINA
gasolina = alcool = diesel = 0
print("-"*30)
print("""Qual combustível deseja inserir:
[1] Gasolina
[2] Álcool
[3] Diesel
[4] Sair""")
while True:
    print("-" * 30)
    código = 0
    while código not in [1, 2, 3, 4]:
        código = int(input("Opção: "))
    if código == 1:
        gasolina += 1
        print("Gasolina computada!")
    if código == 2:
        alcool += 1
        print("Álcool computado!")
    if código == 3:
        diesel += 1
        print("Diesel computado!")
    if código == 4:
        break
print("-"*30)
print("Muito obrigado!")
print(f"Gasolina: {gasolina}")
print(f"Álcool: {alcool}")
print(f"Diesel: {diesel}")







