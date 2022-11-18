primos = []
cont = 0
n = int(input("Número: "))
for c in range(2, n+1):
    for div in range(1, c+1):
        if c % div == 0:
            cont += 1
    if cont <= 2:
        primos.append(c)
    cont = 0
print(f"Os números primos de 0 a {n}: {primos}")