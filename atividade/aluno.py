class Aluno:
    def __init__(self, nome='', endereco='', ra='', idade=0):
        self.nome = nome
        self.endereco = endereco
        self.ra = ra
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"RA: {self.ra}")
        print(f"Idade: {self.idade}")

    def criar_aluno(self):
        self.nome = input("Digite o nome do aluno: ")
        self.endereco = input("Digite o endereço do aluno: ")
        self.ra = input("Digite o RA do aluno: ")
        self.idade = int(input("Digite a idade do aluno: "))

# Criando os objetos Aluno
aluno1 = Aluno()
print("Informe os dados do aluno 1: ")
aluno1.criar_aluno()
print("\nInformações do aluno 1:")
aluno1.mostrar_dados()

aluno2 = Aluno()
print("\nInforme os dados do aluno 2: ")
aluno2.criar_aluno()
print("\nInformações do aluno 2:")
aluno2.mostrar_dados()
