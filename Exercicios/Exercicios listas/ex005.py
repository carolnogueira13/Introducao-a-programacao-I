# LER UM VETOR AO CONTRÁRIO
vetor = [0.0]*5
contrario = [0.0]*5
for i in range(0,5):
    vetor[i] = int(input("Digite um número: "))
print(f"O vetor formado foi {vetor}")
n = 4
for i in range(0,5):
    contrario[i] = vetor[n]
    n = n-1
print(f"Lendo o vetor ao contrário ficaria: {contrario}")



