# PROGRAMA PARA LER IDADE E GENERO DOS 40 ALUNOS
F = 0
M = 0
N = 0
aluno21 = 0
media = 0

for cont in range(1, 41):
    print("\nAluno {}" .format(cont))
    idade = int(input("Idade: "))
    genero = str(input("Gênero (digite masculino(M), feminino(F) ou Neutro(N)): "))
    if genero == "Masculino" or genero == "masculino" or genero == "m" or genero == "M":
        M += 1
        media = media + idade
    elif genero == "Feminino"or genero == "feminino" or genero == "f" or genero == "F":
        F += 1
    elif genero == "Neutro" or genero == "neutro" or genero == "n" or genero == "N":
        N += 1

    if idade > 21:
        aluno21 += 1
print("\n")
print("\033[35mNessa turma existem {} alunos de gênero feminino, {} alunos do gênero masculino e "
      "{} alunos de gênero não identificado\033[m" .format(F, M, N))
print("Nesse turma existem {} alunos com mais de 21 anos." .format(aluno21))
print("A média das idades dos alunos que se identificam no gênero masculino é {} " .format(media/M))
