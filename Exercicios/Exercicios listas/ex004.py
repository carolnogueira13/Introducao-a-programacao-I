# PROGRAMA PARA DETERMINAR A SEQUÊNCIA DE FIBONACCI DE 20 TERMOS
sequencia = [0.0]*20
sequencia[0] = 0
sequencia[1] = 1
for i in range(2, 20):
    sequencia[i] = sequencia[i-1] + sequencia[i-2]
print(f"Os 20 primeiros termos da sequência de Fibonacci são {sequencia}")
