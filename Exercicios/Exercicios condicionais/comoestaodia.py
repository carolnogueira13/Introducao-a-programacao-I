celsius = float(input("Usuário digite a temperatura em Celsius: "))
if celsius >= 30:
    print("Está quente demais!")
elif celsius<30 and celsius>=15:
    print("Está uma temperatura agradavel!")
else:
    print("Está frio!")