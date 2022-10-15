# PROGRAMA PARA CALCULAR A MÉDIA DA NOTAS DOS ALUNOS COM LISTAS
notas = [0.0]*5
qtde = 0
media = 0.0
for i in range(5):
    notas[i] = float(input("Informe a nota: "))
    media = media + notas[i]

# Calcula a media
media = media / 5
print(f"{media:.2f}")

for i in notas:
    if i > media:
        qtde = qtde + 1
        print(i)
print(f"Média:{media:.2f}")
print(f"Notas acima da média: {qtde}")


'''notas = []
media = 0.0
for i in range(0,5):
    notas.append(float(input("Informe a nota: ")))
    media = media + notas[-1]
# Calcula a media
media = media / len(notas)
print(media)'''
