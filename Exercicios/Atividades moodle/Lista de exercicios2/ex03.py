# PROGRAMA QUE LEIA A MÉDIA DA NOTA DOS ALUNOS, ENCONTRE E EXIBA O MAIOR VALOR DE UMA MÉDIA INSERIDA
maior_media = 0
print("PROGRAMA PARA SABER A MAIOR MÉDIA DE NOTA DE AULNOS DE UMA TURMA")
print("-"*80)
while True:
    resp = " "
    while resp not in "SN":
        resp = str(input("Você gostaria de informar as notas de um aluno da turma"
                         "(S para Sim e N para Não): ")).strip().upper()
    if resp == "N":
        break
    media = float(input("Insira a média de um aluno: "))
    print("-"*80)
    if media > maior_media:
        maior_media = media
print("-"*80)
print(f"A maior média entre os alunos é {maior_media}.")
