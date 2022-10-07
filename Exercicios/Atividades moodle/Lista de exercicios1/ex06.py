# PROGRAMA QUE SOLICITA A ENTRADA DE 3 VALORES(A,B E C) E VERIFICA SE ESSES VALORES FORMAM UM TRIÂNGULO
a = int(input("Insira um valor: "))
b = int(input("Insira um valor: "))
c = int(input("Insira um valor: "))
if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        print("Os valores formam um triângulo!")
        perimetro = a + b + c
        print(f"O perímetro desse triângulo é {perimetro}.")
    else:
        print("Os valores não formam um triângulo!")
else:
    print(" Os valores não formam um triângulo!")
