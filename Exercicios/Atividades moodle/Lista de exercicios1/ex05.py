# PROGRAMA PARA O USUÁRIO INFORMAR SUA IDADE E EXIBIR O VALOR DE SEGURO PAGO.
idade = int(input("Insira a sua idade: "))
valor = 100.00
if idade <= 10:
    valor = valor + 60.00
elif 10 < idade <= 30:
    valor = valor + 90.00
elif 30 < idade <= 45:
    valor = valor + 130.00
elif 45 < idade <= 59:
    valor = valor + 250.00
elif idade >= 60:
    valor = valor + 400.00

print(f"O valor para o plano contratado será de R${valor}.")
