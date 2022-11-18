# PROGRAMA PARA FATORIAL DE OUTRO VETOR
from random import randint
from math import factorial

vetor1 = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),
          randint(1,10), randint(1,10), randint(1,10)]

vetor2 = [factorial(vetor1[0]), factorial(vetor1[1]), factorial(vetor1[2]), factorial(vetor1[3]), factorial(vetor1[4]),
          factorial(vetor1[5]), factorial(vetor1[6]), factorial(vetor1[7]), factorial(vetor1[8]), factorial(vetor1[9])]

print(f"Vetor 1 é igual a {vetor1}")
print(f"Fatorial dos elementos do vetor 1 é igual a {vetor2}")
