notas = [0.0]*10
for cont in range(0,10):
    notas[cont] = float(input(f"Digite a {cont+1}ª nota : "))
    print(notas)

for pos, i in enumerate(notas):
    print(f"{i} na posição {pos}")

"""notas = []
for cont in range(0,9):
    notas.append(float(input("Digite uma nota: ")))
    print(notas)"""