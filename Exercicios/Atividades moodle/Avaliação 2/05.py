# PROGRAMA FRASES MALUCAS
import random
artigos = ["o", "a", "um", "uma"]
sujeitos = ["gato", "cachorro", "homem", "mulher"]
verbos = ["cantar", "correr", "pular", "nadar"]
adverbios = ["vagarosamente", "silenciosamente", "bem", "mal"]
print("-"*50)
print(f"{'Gerador de frases malucas':^50}")
print("-"*50)
for c in range(5):
    frase0 = [random.choice(artigos), random.choice(sujeitos), random.choice(verbos), random.choice(adverbios)]
    frase1 = [random.choice(artigos), random.choice(sujeitos), random.choice(verbos)]
    escolha = random.randint(0, 1)
    if escolha == 0:
        frase = frase0
    if escolha == 1:
        frase = frase1
    print(f"Frase {c+1}:", end=" ")
    for palavra in frase:
        print(f"{palavra}", end=" ")
    print()
