class Quadrado:
    def __init__(self, lado = 0, area=0):
        # Inicializa o atributo 'lado' e a área é inicialmente 0
        self.lado = lado
        self.area = area

    def calcular_area(self):        
        # Calcula a área do quadrado
        self.area = self.lado ** 2

    def mostrar_dados(self):
        # Exibe os dados do lado e da área
        print(f"\nLado: {self.lado}")
        print(f"Área: {self.area}")


quadrados = []  # Cria uma lista vazia para armazenar os objetos Quadrado

# Loop para criar dois objetos Quadrado com dados fornecidos pelo usuário
for i in range(2):
    lado = float(input(f"Digite o valor do lado do quadrado {i + 1}: "))
    quadrado = Quadrado(lado)  # Cria um objeto Quadrado com o lado fornecido
    quadrado.calcular_area()   # Calcula a área do quadrado
    quadrados.append(quadrado) # Adiciona o objeto à lista de quadrados
    quadrado.mostrar_dados()   # Exibe os dados do quadrado
