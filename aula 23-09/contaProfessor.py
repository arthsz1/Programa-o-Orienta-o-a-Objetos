class Conta_Agua:
    def __init__(self, titular, consumo_m3, tarifa_por_m3):
        self.titular = titular
        self.consumo_m3 = consumo_m3  # Consumo de água
        self.tarifa_por_m3 = tarifa_por_m3  # Tarifa por m3

    def calcular_valor_conta(self):
        valor = self.consumo_m3 * self.tarifa_por_m3
        print("Titular:", self.titular)
        print("Conta de água: R$", valor)

    def cadastrar_conta(self, titular, consumo_m3, tarifa_por_m3):
        self.titular = titular
        self.consumo_m3 = consumo_m3
        self.tarifa_por_m3 = tarifa_por_m3

# Criando dois objetos da classe Conta_Agua
conta1 = Conta_Agua("Carlos", 30, 2.5)
conta2 = Conta_Agua("Mariana", 45, 2.5)

# Utilizando os métodos dos objetos
conta1.calcular_valor_conta()
conta2.calcular_valor_conta()
