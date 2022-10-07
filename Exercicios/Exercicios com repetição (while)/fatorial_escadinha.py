n = int(input("Insira um valor de n: "))
fat = 1
while n >= 0:
    print(f"{n}! =", end=" ")
    for c in range(n, 0, -1):
        fat = fat * c
        print(f"{c} *", end=" ") if c != 1 else print(f"{c} =", end=" ")
    print(f"{fat}")
    n -= 1
    fat = 1