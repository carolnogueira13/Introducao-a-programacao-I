# PROGRAMA QUE LÊ UM VALOR n INTEIRO E POSITIVO e CALCULA S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
S = 0
n = int(input("Insira um valor: "))
print("S =", end=" ")
for cont in range(1, n + 1):
    S += 1 / cont
    print(f"1/{cont}" if cont != 1 else "1", end=" ")
    print("+" if cont != n else "=", end=" ")
print(f"{S:.2f}")