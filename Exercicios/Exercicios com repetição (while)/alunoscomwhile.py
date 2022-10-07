# PROGRAMA PARA LER IDADE E GENERO DOS ALUNOS
F = 0
M = 0
N = 0
aluno21 = 0
media = 0

resp = input("Você gostaria de saber a idade e o gênero de um aluno da turma (S para Sim e N para Não)? ")
while resp == "Sim" or resp == "sim" or resp == "S" or resp == "s":
    idade = int(input("Idade: "))
    genero = str(input("Gênero (digite masculino(M), feminino(F) ou Nâo identificado (N)): "))
    if genero == "Masculino" or genero == "masculino" or genero == "m" or genero == "M":
        M += 1
        media = media + idade
    elif genero == "Feminino" or genero == "feminino" or genero == "f" or genero == "F":
        F += 1
    elif genero == "Nâo identificado" or genero == "nâo identificado" or genero == "n" or genero == "N":
        N += 1

    if idade > 21:
        aluno21 += 1
    resp = input("\nVocê gostaria de saber a idade e o gênero de mais um aluno (S para Sim e N para Não)? ")

print("\n")
print("Nessa turma existem {} alunos de gênero feminino, {} alunos do gênero masculino e {} alunos de gênero não identificado" .format(F, M, N))
print("Nessa turma existem {} alunos com mais de 21 anos." .format(aluno21))
print("A média das idades dos alunos que se identificam no gênero masculino é {} " .format(media/M))
