class Conta_Agua:
    def calcular_valor_conta(self):
        valor = self.consumo_m3 * self.tarifa_por_m3
        print("Titular:", self.titular)
        print("Conta de água: R$", valor)

    def cadastrar_conta(self, titular, consumo_m3, tarifa_por_m3):
        self.titular = titular
        self.consumo_m3 = consumo_m3
        self.tarifa_por_m3 = tarifa_por_m3

# Criando dois objetos da classe Conta_Agua
conta1 = Conta_Agua()
conta2 = Conta_Agua()

# Utilizando os métodos dos objetos
conta1.cadastrar_conta("Carlos", 30, 2.5)
conta1.calcular_valor_conta()

conta2.cadastrar_conta("Mariana", 45, 2.5)
conta2.calcular_valor_conta()
