class Pessoa:
    def __init__(self, nome, idade, trabalha):
        self.nome = nome
        self.idade = idade
        self.trabalha = trabalha

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Está trabalhando: {self.trabalha}")

class Cao:
    def __init__(self, nome, idade,comida,sono):
        self.nome = nome
        self.idade = idade
        self.comida = comida
        self.sono = sono
    
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Comida: {self.comida}")
        print(f"sono: {self.sono}")

# Instanciando dois objetos da classe Pessoa
pessoa1 = Pessoa(nome="Pedro", idade=41, trabalha=False)
pessoa2 = Pessoa(nome="Arthur", idade=18, trabalha=True)

# Instanciando dois objetos da classe Cao
cao1 = Cao(nome="Rex", idade=5, comida=5, sono=True)
cao2 = Cao(nome="Atena", idade=9, comida=1, sono = False)

# Mostrando informações das pessoas
print("Informações da Pessoa 1:")
pessoa1.mostrar_informacoes()
print("\nInformações da Pessoa 2:")
pessoa2.mostrar_informacoes()

# Mostrando informações dos cães
print("\nInformações do Cão 1:")
cao1.mostrar_informacoes()
print("\nInformações do Cão 2:")
cao2.mostrar_informacoes()
