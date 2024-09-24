class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
       
       self.cor = cor
       self.altura = altura
       self.profundidade = profundidade
       self.largura = largura
    # def passar_canal(self, botao):
    #    if botao == "+":
    #     print("Aumentar o Canal ") 
    #    elif botao == "-":
    #     print("Diminuir o Canal ")

controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.cor)
# controle_remoto.passar_canal("+")

controle_remoto2 = ControleRemoto("azul", "5cm", "3cm", "5cm")
# controle_remoto2.passar_canal("-")

