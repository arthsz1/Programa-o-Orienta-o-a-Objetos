class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando duas instâncias da classe Pessoa
pessoa1 = Pessoa("Fulano", 25)
pessoa2 = Pessoa("Ciclano", 30)

def mostrar_informacoes(self):
    print("Nome:", self.nome, ", Idade:", self.idade)

# Exibindo os atributos das pessoas
print("Nome:", pessoa1.nome, ", Idade:", pessoa1.idade)
print("Nome:", pessoa2.nome, ", Idade:", pessoa2.idade)

class Caes:
    def __init__(self, raca, idade):
        self.raca = raca
        self.idade = idade

# Criando duas instâncias da classe Caes
caes1 = Caes("vira-lata", 5)
caes2 = Caes("labrador", 3)

# Exibindo os atributos dos cães
print("Raça:", caes1.raca, ", Idade:", caes1.idade)
print("Raça:", caes2.raca, ", Idade:", caes2.idade)


