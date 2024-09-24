class Circulo:

    def __init__(self, raio=0, area=0, pi = 3.1415):
        self.raio = raio
        self.area = area
        self.pi = pi

    def calcular_area(self):
        self.area = self.pi * (self.raio ** 2)

    def mostrar_dados(self):
        print(f"\nRaio: {self.raio}")
        print(f"Área: {self.area:.2f}")

# Função para criar um círculo a partir de dados do usuário
def criar_circulo():
    raio = float(input("Digite o valor do raio: "))  # Lê o raio do círculo
    circulo = Circulo(raio)  # Cria um objeto Circulo com o raio fornecido
    circulo.calcular_area()  # Calcula a área
    return circulo

# Cria o primeiro Circulo
print("Informe os dados do Circulo 1: ")
circulo1 = criar_circulo()
# Mostra as informações do primeiro Circulo
print("\nInformações do Circulo 1:")
circulo1.mostrar_dados()

# Cria o segundo Circulo
print("\nInforme os dados do Circulo 2: ")
circulo2 = criar_circulo()
# Mostra as informações do segundo Circulo
print("\nInformações do Circulo 2:")
circulo2.mostrar_dados()
