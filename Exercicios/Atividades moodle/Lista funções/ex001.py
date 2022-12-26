# PROGRAMA PARA CONVERTER DE FAH PARA CELCIUS COM FUNÇÃO
def conversor(f):
    c = 5/9 * (f - 32)
    return f"A temperatura em {f}ºF corresponde a {c:.2f}ºC"


fah = float(input("Insira a temperatura em Fahrenheit: "))
print(conversor(fah))
