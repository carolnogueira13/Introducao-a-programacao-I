f = open("nome.txt")  # Abrir arquivo
# s = f.read() # Lê o arquivo
# print(s)

# s = f.readlines() # Lê cada linha do arquivo e transforma em uma lista
# print(s)

s = f.read().split()  # Lê cada palavra do arquivo e transforma em uma lista
print(s)

f.close()  # Fechar arquivo
