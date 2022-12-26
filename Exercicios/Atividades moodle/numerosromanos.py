# PROGRAMA PARA CONVERTER DE NÚMEROS ROMANOS PARA DECIMAL
simbolos = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
romano = str(input("Insira o número em romanos: ")).upper()
decimal = 0
for i in range(len(romano)-1, -1, -1):
    if i < len(romano) - 1 and simbolos[romano[i]] < simbolos[romano[i + 1]]:
        decimal -= simbolos[romano[i]]
    else:
        decimal += simbolos[romano[i]]
print(f"O número {romano} no sistema decimal é {decimal}")
