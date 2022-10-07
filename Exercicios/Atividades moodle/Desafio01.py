# PROGRAMA RELÓGIO DO ATLETA
print("-"*50)
print("BEM-VINDO AO RELÓGIO DO ATLETA".center(50))
print("O LOCAL DE MONITORAMENTO DA SUA ATIVIDADE FÍSICA".center(50))
print("-"*50)

R = 0
while R < 35 or R > 100:
    R = int(input("Frequência cardíaca do atleta em repouso: ")) # Para o programa perguntar a frequência do
    # atleta até que ele indique um valor dentro dos parâmetros

print("-"*50)
F = 0
while F < 35 or F > 200:
    F = int(input("Frequência cardíaca atual do atleta: ")) # Para o programa perguntar a frequência do
    # atleta até que ele indique um valor dentro dos parâmetros

print("-"*50)
C = 0
while C < 50 or C > 100:
    C = int(input("Capacidade de oxigenação atual do atleta: ")) # Para o programa perguntar a oxigenação do
    # atleta até que ele indique um valor dentro dos parâmetros

print("-"*50)
if F > 3*R or C < 95:
    print("\033[34mDIMINUIR!\033[m")

elif F < 2*R and C > 97:
    print("\033[32mAUMENTAR!\033[m")

else:
    print("\033[33mMANTER!\033[m")
