# PROGRAMA PARA MOSTRAR NÚMEROS ÍMPARES DE 1 A N
n = int(input("Indique o seu número:"))
if n < 1000:
    print(f"O números ímpares de 1 a {n} são: ")
    for c in range(1, n+1, 2):
        print(c, end=" ")
else:
    print("Número informado acima do limite, repita o programa com um número menor que 1000.")

