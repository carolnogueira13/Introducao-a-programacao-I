# PROGRAMA PARA CÁLCULO DE IRRF (IMPOSTO DE RENDA RETIDO NA FONTE)
def IRRF(salario):
    if salario > 4664.68:
        imposto = (salario * 0.2750) - 869.36
        aliquota = 27.50
    elif salario > 3751.06:
        imposto = (salario * 0.2250) - 636.13
        aliquota = 22.5
    elif salario > 2826.66:
        imposto = (salario * 0.15) - 354.80
        aliquota = 15.00
    elif salario > 1903.99:
        imposto = (salario * 0.075) - 142.80
        aliquota = 7.50
    else:
        print("Essa faixa salarial é isenta de IRRF.")
        aliquota = 0
        imposto = 0
    salarionovo = salario - imposto
    print(f"""O salário após a dedução do IRRF é {salarionovo}
O valor de imposto pago foi R${imposto:.2f}
E a alíquota foi de {aliquota}%""")


# Programa principal:
while True:
    print("-"*70)
    sal = float(input("Insira o seu salário do funcionário antes da dedução do IRRF: R$ "))
    if sal < 0:
        print("Programa encerrado!")
        break
    else:
        IRRF(sal)


