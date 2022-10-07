# PROGRAMA PARA FAZER UMA CALCULADORA
print("--" * 20)
print("BEM-VINDO A CALCULADORA! PRIMEIRAMENTE DIGITE OS NÚMEROS!")
print("--" * 20)
num1 = float(input("Insira um número: "))
num2 = float(input("Insira um número: "))
print("--" * 20)
print("AGORA ESCOLHA A OPERAÇÃO QUE DESEJA FAZER!")
print("--" * 20)
operação = input("\nEscolha a operação que deseja fazer entre esses dois números ("
                 "1 - SOMA, 2 - DIFERENÇA, 3 - PRODUTO, 4 - DIVISÃO, 5 - SAIR): ")
while operação != "5":

    if operação == "1":
        soma = num1 + num2
        print(f"\n{num1} + {num2} = {soma}")

    if operação == "2":
        if num1 > num2:
            diferença = num1 - num2
            print(f"\n{num1} - {num2} = {diferença}")
        elif num2 > num1:
            diferença = num2 - num1
            print(f"\n{num2} - {num1} = {diferença}")
        else:
            print(" \nO resultado da diferença dos dois números informados é zero")

    if operação == "3":
        produto = num1 * num2
        print(f"\n{num1} x {num2} = {produto}")

    if operação == "4":
        if num1 != 0 and num2 != 0:
            div1 = num1 / num2
            div2 = num2 / num1
            print(f"\n{num1} / {num2} = {div1:.2f} "
                  f"\n{num2} / {num1} = {div2:.2f} ")
        else:
            print("\nOperação inválida porque um dos números é igual a zero!")

    if operação != "1" and operação != "2" and operação != "3" and operação != "4":
        print("\nOperação inválida!! Digite uma operação válida ou 5 para sair.")


    operação = input("\nEscolha a sua próxima operação entre esses dois números "
                     "(1 - SOMA, 2 - DIFERENÇA, 3 - PRODUTO, 4 - DIVISÃO, 5 - SAIR): ")

print("--" * 20)
print("CALCULADORA FINALIZADA!")
print("--" * 20)
