class Conta_Agua:
    def __init__(self, titular, consumo_m3, tarifa_por_m3):
        self.titular = titular
        self.consumo_m3 = consumo_m3
        self.tarifa_por_m3 = tarifa_por_m3
    
    def cadastrar_conta(self, titular, consumo_m3, tarifa_por_m3):
        self.titular = titular
        self.consumo_m3 = consumo_m3
        self.tarifa_por_m3 = tarifa_por_m3
    
    def calcular_valor_conta(self):
        valor = self.consumo_m3 * self.tarifa_por_m3
        print("Titular:", self.titular)
        print("Conta de água: R$", valor)

# Inicializando as contas corretamente
conta1 = Conta_Agua("Vanessa", 25, 4.0)
conta2 = Conta_Agua("João", 4, 5.0)

conta1.calcular_valor_conta()
conta2.calcular_valor_conta()
