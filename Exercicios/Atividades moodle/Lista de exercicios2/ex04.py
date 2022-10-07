# PROGRAMA QUE LEIA O NÚMERO DA CONTA E O SALDO DO CLIENTE. TERMINA QUANDO FOR DIGITADO -999 OU ACABAR
# OS 10000 NÚMEROS. TOTAL DE CLIENTES COM SALDO NEGATIVO, O TOTAL DE CLIENTES DA AGÊNCIA E SALDO DA AGÊNCIA

neg = saldo_agência = clientes = 0
print("BANCO FICTÍCIO")
while clientes < 10000:
    print("-" * 50)
    resp = " "
    while resp != "S" and resp != "-999":
        resp = str(input("Você deseja inserir os dados de clientes da agência: (S - Sim "
                         "e -999 para Sair): ")).strip().upper()
    if resp == "-999":
        break
    print(f"\nCliente {clientes + 1}")
    conta = str(input("Insira a conta do cliente: "))
    saldo = float(input("Insira o saldo do cliente: "))
    if saldo < 0:
        neg += 1
    saldo_agência = saldo_agência + saldo
    clientes += 1
print(f"Essa agência possui {clientes} clientes, {neg} clientes possuem saldo negativo e o saldo da agência é "
      f"{saldo_agência}.")
