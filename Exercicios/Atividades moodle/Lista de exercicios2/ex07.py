# PROGRAMA PARA EXIBIR A SÉRIE: 1, 4, 9, 16, 25, 36, ... ATÉ O N-ÉSIMO TERMO
n = int(input("Quantos números você quer que a sequência tenha? "))
S = 1
print("A sequência é", S, end="")
for cont in range(1, n):
    S += (2 * cont) + 1
    print(f", {S}", end="")






