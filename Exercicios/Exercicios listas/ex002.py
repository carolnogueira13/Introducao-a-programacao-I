# PROGRAMA PARA LER DUAS LISTAS E CALCULAR A SOMA DELAS
v1 = [0.0]*5
v2 = [0.0]*5
vsoma = [0.0]*5
for i in range(0, 5):
    v1[i] = (float(input("Digite um número da lista v1: ")))

for i in range(0, 5):
    v2[i] = (float(input("Digite um número da lista v2: ")))

for i in range(0, 5):
    vsoma[i] = (v1[i] + v2[i])

print(v1)
print(v2)
print(vsoma)