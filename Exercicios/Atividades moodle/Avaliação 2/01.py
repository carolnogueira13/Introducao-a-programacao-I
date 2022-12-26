# PROGRAMA SENHAS CRITICADAS
while True:
    senha = str(input("Digite a sua senha: "))
    Existenumero = ExisteLetraM = TamanhoCorreto = SenhaIniciadacomNum = False
    if 6 <= len(senha) <= 8:
        TamanhoCorreto = True
    if not senha[0].isnumeric():
        SenhaIniciadacomNum = True
    for i in senha:
        if i.isnumeric():
            Existenumero = True
        if i.isupper():
            ExisteLetraM = True
    if Existenumero and ExisteLetraM and TamanhoCorreto and SenhaIniciadacomNum:
        break
    if not TamanhoCorreto:
        print("Senha inválida! Sua senha deve ter entre 6 e 8 caracteres.")
    if not Existenumero:
        print("Senha inválida! Sua senha precisa ter pelo menos um número.")
    if not SenhaIniciadacomNum:
        print("Senha inválida! Sua senha não pode começar com um número.")
    if not ExisteLetraM:
        print("Senha inválida! Sua senha precisa ter pelo menos uma letra maiúscula.")
print(f"Senha válida! Sua senha contém {len(senha)} dígitos.")
print(f"Versão maiúscula da senha: {senha.upper()}")
print(f"Versão minúscula da senha: {senha.lower()}")
