class Produto:
    def __init__(self, marca, fabricante, cod_barras, preco):
        self.marca = marca
        self.fabricante = fabricante
        self.cod_barras = cod_barras
        self.preco = preco

# Criando o primeiro objeto
marca = input("Digite o nome da marca: ")
fabricante = input("Digite o nome do fabricante: ")
cod_barras = input("Digite o código de barras: ")
preco = float(input("Digite o preço: "))
produto1 = Produto(marca, fabricante, cod_barras, preco)

# Criando o segundo objeto
marca = input("\nDigite o nome da segunda marca: ")
fabricante = input("Digite o nome do fabricante: ")
cod_barras = input("Digite o código de barras: ")
preco = float(input("Digite o preço: "))
produto2 = Produto(marca, fabricante, cod_barras, preco)

# Exibindo os dados dos objetos
print("\nDados do primeiro produto:")
print(f"Marca: {produto1.marca}, Fabricante: {produto1.fabricante}, Código de Barras: {produto1.cod_barras}, Preço: {produto1.preco:.2f}")

print("\nDados do segundo produto:")
print(f"Marca: {produto2.marca}, Fabricante: {produto2.fabricante}, Código de Barras: {produto2.cod_barras}, Preço: {produto2.preco:.2f}")
