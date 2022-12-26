# Criando classes em Python
class Filhote:
    def __init__(self, nome, brinquedo):
        self.nome = nome
        self.brinquedo = brinquedo

    def brincar(self):
        print(f"{self.nome} brinca com o {self.brinquedo}")


# Programa principal:
animal1 = Filhote("Bruna", "chinelo")
animal1.brincar()
animal2 = Filhote("Bolota", "rato de brinquedo")
animal2.brincar()
