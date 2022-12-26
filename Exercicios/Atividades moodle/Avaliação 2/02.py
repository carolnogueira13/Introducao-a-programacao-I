def tamanho(s, min, max):
    if min <= len(s) <= max:
        return True
    else:
        return False


def senhamaiuscula(s):
    return s.upper()


def senhaminuscula(s):
    return s.lower()


def valid1dig(s):
    for i in s:
        if i.isnumeric():
            return True
    return False


def no1number(s):
    if s[0].isnumeric():
        return False
    else:
        return True


def pelomenos1maisc(s):
    for i in s:
        if i.isupper():
            return True
    return False


# Programa principal
while True:
    senha = str(input("Digite a sua senha: "))
    if tamanho(senha, 6, 8) and valid1dig(senha) and no1number(senha) and pelomenos1maisc(senha):
        break
    if not tamanho(senha, 6, 8):
        print("Senha inválida! Sua senha deve ter entre 6 e 8 caracteres.")
    if not valid1dig(senha):
        print("Senha inválida! Sua senha precisa ter pelo menos um número.")
    if not no1number(senha):
        print("Senha inválida! Sua senha não pode começar com um número.")
    if not pelomenos1maisc(senha):
        print("Senha inválida! Sua senha precisa ter pelo menos uma letra maiúscula.")
print(f"Senha válida! Sua senha contém {len(senha)} dígitos.")
print(f"Versão maiúscula da senha: {senhamaiuscula(senha)}")
print(f"Versão minúscula da senha: {senhaminuscula(senha)}")
