class Quadrado:
    def __init__(self, lado=0, area=0):
        self.lado = lado
        self.area = area  # Inicializa a área como 0

    def calcular_area(self):
        self.area = self.lado ** 2  # Calcula a área do quadrado (lado^2)

    def mostrar_dados(self):
        print(f"\nLado: {self.lado}")
        print(f"Área: {self.area}")

    def criar_quadrado(self):
        self.lado = float(input("Digite o valor do lado: "))  # Lê o lado do quadrado
        self.calcular_area()  # Calcula a área
        self.mostrar_dados()  # Mostra os dados do quadrado


# Cria o primeiro quadrado
quadrado1 = Quadrado()
print("Informe os dados do Quadrado 1: ")
quadrado1.criar_quadrado()

# Mostra as informações do primeiro quadrado
print("\nInformações do Quadrado 1:")
quadrado1.mostrar_dados()

# Cria o segundo quadrado
quadrado2 = Quadrado()
print("\nInforme os dados do Quadrado 2: ")
quadrado2.criar_quadrado()

# Mostra as informações do segundo quadrado
print("\nInformações do Quadrado 2:")
quadrado2.mostrar_dados()
