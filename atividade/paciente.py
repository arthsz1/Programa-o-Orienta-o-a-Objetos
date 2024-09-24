class Paciente:
    def __init__(self, nome, rg='', endereco='', telefone='', dataNasc='', profissao=''):
        # Definindo o nome como obrigatório, os outros parâmetros são opcionais com valores padrão
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.dataNasc = dataNasc
        self.profissao = profissao

    def mostrar_informacoes(self):
        print(f"\nNome: {self.nome}")
        print(f"RG: {self.rg}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Data de Nascimento: {self.dataNasc}")
        print(f"Profissão: {self.profissao}")

    def criar_paciente(self):
        # Atualizando os atributos da instância com os inputs do usuário
        self.rg = input("Digite o RG do paciente: ")
        self.endereco = input("Digite o endereço do paciente: ")
        self.telefone = input("Digite o telefone do paciente: ")
        self.dataNasc = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
        self.profissao = input("Digite a profissão do paciente: ")

# Criando o primeiro objeto com o nome obrigatório
nome1 = input("Informe o nome do paciente 1: ")
paciente1 = Paciente(nome1)
paciente1.criar_paciente()  # Preenche os atributos adicionais

print("\nInformações do paciente 1:")
paciente1.mostrar_informacoes()  # Exibe as informações do paciente 1

# Criando o segundo objeto com o nome obrigatório
nome2 = input("\nInforme o nome do paciente 2: ")
paciente2 = Paciente(nome2)
paciente2.criar_paciente()  # Preenche os atributos adicionais

print("\nInformações do paciente 2:")
paciente2.mostrar_informacoes()  # Exibe as informações do paciente 2


