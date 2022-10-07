# PROGRAMA PARA SABER O QUADRANTE QUE SE ENCONTRAM X E Y
x = float(input("Qual o valor de X: "))
y = float(input("Qual o valor de Y: "))

if x == 0 or y == 0:
    if x == 0 and y == 0:
        Quadrante = "Origem"
    if x == 0 and y != 0:
        Quadrante = "Eixo y"
    if x != 0 and y == 0:
        Quadrante = "Eixo x"
else:
    if x > 0 and y > 0:
        Quadrante = "Quadrante Q1"
    elif x < 0 and y > 0:
        Quadrante = "Quadrante Q2"
    elif x < 0 and y < 0:
        Quadrante = "Quadrante Q3"
    else:
        Quadrante = "Quadrante Q4"

print(f"As coordenadas ({x},{y}) se encontram na posição {Quadrante}")

