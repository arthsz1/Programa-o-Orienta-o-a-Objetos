class Circulo:
    def __init__(self, raio = 0, area=0, pi=3.1415):
        self.raio = raio
        self.area = area
        self.pi = pi

    def calcular_area(self):
        # Calcula a área do círculo
        self.area = self.pi * (self.raio ** 2)

    def mostrar_dados(self):
        # Exibe os dados do raio e da área
        print(f"\nRaio: {self.raio}")
        print(f"Área: {self.area:.2f}")


circulos = []  # Cria uma lista vazia para armazenar os objetos Circulo

# Loop para criar dois objetos Circulo com dados fornecidos pelo usuário
for i in range(2):
    raio = float(input(f"\nDigite o valor do raio do círculo {i + 1}: "))
    circulo = Circulo(raio)  # Cria um objeto Circulo com o raio fornecido
    circulo.calcular_area()   # Calcula a área do círculo
    circulos.append(circulo)  # Adiciona o objeto à lista de círculos
    circulo.mostrar_dados()    # Exibe os dados do círculo


