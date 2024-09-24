class Aluno:
    # Construtor da classe Aluno
    def __init__(self, nome, endereco, ra, idade):
        self.nome = nome
        self.endereco = endereco
        self.ra = ra
        self.idade = idade

    # Método para mostrar os dados do aluno
    def mostrar_dados(self):
        print("\nNome:", self.nome)
        print("Endereço:", self.endereco)
        print("RA:", self.ra)
        print("Idade:", self.idade)

# Coletando dados do usuário para o primeiro aluno
nome = input("Digite o nome do aluno 1: ")
endereco = input("Digite o endereço: ")
ra = input("Digite o RA: ")
idade = int(input("Digite a idade: "))

# Criando o primeiro objeto aluno1
aluno1 = Aluno(nome, endereco, ra, idade)

# Coletando dados do usuário para o segundo aluno
nome = input("\nDigite o nome do aluno 2: ")
endereco = input("Digite o endereço: ")
ra = input("Digite o RA: ")
idade = int(input("Digite a idade: "))

# Criando o segundo objeto aluno2
aluno2 = Aluno(nome, endereco, ra, idade)

# Mostrando os dados dos dois alunos
aluno1.mostrar_dados()
aluno2.mostrar_dados()
