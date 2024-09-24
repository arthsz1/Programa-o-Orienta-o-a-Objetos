class Cliente:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def informacao_cliente(self):
        print("Informações do Cliente:")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Idade: {self.idade}")
        

class Curso:
    def __init__(self, nome, descricao, carga_horaria, qtdalunos):
        self.nome = nome
        self.descricao = descricao
        self.carga_horaria = carga_horaria
        self.qtdalunos = qtdalunos

    def mostrar_informacoes(self):
        print("\nInformações do Curso:")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Carga Horária: {self.carga_horaria}")
        print(f"A sala é composta por: {self.qtdalunos}")
        
        
# Instanciando um objeto da classe Cliente
cliente1 = Cliente("Arthur Saraiva", "arthursaraiva51@gmail.com", 18)

# Instanciando um objeto da classe Curso
curso1 = Curso("Ciências da Computação", "Aprenda os fundamentos da programação.", 3000, "90 alunos\n" )

# Mostrando informações do cliente

cliente1.informacao_cliente()

curso1.mostrar_informacoes()
