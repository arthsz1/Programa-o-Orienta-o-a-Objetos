class Paciente:
    def __init__(self, nome, rg='', endereco='', telefone='', dataNasc='', profissao=''):
        # Definindo o nome como obrigatório, os outros parâmetros são opcionais com valores padrão
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.dataNasc = dataNasc
        self.profissao = profissao


# Coletando dados do primeiro paciente
nome = input("Digite o nome do paciente: ")
rg = input("Digite o RG do paciente: ")
endereco = input("Digite o endereço do paciente: ")
telefone = input("Digite o telefone do paciente: ")
dataNasc = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
profissao = input("Digite a profissão do paciente: ")

paciente1 = Paciente(nome, rg, endereco, telefone, dataNasc, profissao)

# Coletando dados do segundo paciente
nome = input("\nDigite o nome do segundo paciente: ")
rg = input("Digite o RG do paciente: ")
endereco = input("Digite o endereço do paciente: ")
telefone = input("Digite o telefone do paciente: ")
dataNasc = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
profissao = input("Digite a profissão do paciente: ")

paciente2 = Paciente(nome, rg, endereco, telefone, dataNasc, profissao)

# Exibindo informações dos pacientes
print("\nInformações do paciente 1:")
print(f"Nome: {paciente1.nome}")
print(f"RG: {paciente1.rg}")
print(f"Endereço: {paciente1.endereco}")
print(f"Telefone: {paciente1.telefone}")
print(f"Data de Nascimento: {paciente1.dataNasc}")
print(f"Profissão: {paciente1.profissao}")

print("\nInformações do paciente 2:")
print(f"Nome: {paciente2.nome}")
print(f"RG: {paciente2.rg}")
print(f"Endereço: {paciente2.endereco}")
print(f"Telefone: {paciente2.telefone}")
print(f"Data de Nascimento: {paciente2.dataNasc}")
print(f"Profissão: {paciente2.profissao}")
