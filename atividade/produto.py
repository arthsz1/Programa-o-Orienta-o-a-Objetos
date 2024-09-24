class Produto:  
    def __init__(self, marca='', fabricante='', cod_barras='', preco=0.0): 
        # Definimos valores padrão: strings vazias para texto e 0.0 para preço
        self.marca = marca 
        self.fabricante = fabricante 
        self.cod_barras = cod_barras 
        self.preco = preco 

for i in range(2):
    print("Digite os dados do {}o. produto:"(i+1))
    marca = input("Digite o nome da marca: ")
    fabricante = input("Digite o nome do fabricante: ")
    cod_barras = input("Digite o código de barras: ")
    preco = float(input("Digite o preço: "))

    print("Dados do {}o. produto:"(i+1))
    print("Marca: {}"(marca))
    print("Fabricante: {}"(fabricante))
    print("Cod. Barras: {}"(cod_barras))
    print("Preço: {}"(preco))


produto1 = Produto()
print(produto1.marca, produto1.fabricante, produto1.cod_barras, produto1.preco)

produto2 = Produto()
print(produto2.marca, produto2.fabricante, produto2.cod_barras, produto2.preco)
