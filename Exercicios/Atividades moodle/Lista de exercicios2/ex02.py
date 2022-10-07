# PROGRAMA PARA CALCULAR A HIPOTENUSA
# Posso fazer de duas formas, irei deixar uma como comentário e a outra rodando

# 1ª forma utilizando a biblioteca math
from math import hypot
cateto1 = float(input("Insira o valor de um dos catetos: "))
cateto2 = float(input("Insira o valor do outro cateto: "))
hip = hypot(cateto1, cateto2)
print(f"Considerando os catetos {cateto1} e {cateto2}, a hipotenusa será {hip:.2f}.")

# 2ª forma sem usar a biblioteca math
cateto1 = float(input("Insira o valor de um dos catetos: "))
cateto2 = float(input("Insira o valor do outro cateto: "))
hip = (cateto1**2 + cateto2**2)**(1/2)
print(f"Considerando os catetos {cateto1} e {cateto2}, a hipotenusa será {hip:.2f}.")

