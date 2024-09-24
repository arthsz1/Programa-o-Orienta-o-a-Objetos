def parcela(valor,qtde): 
    res = (valor + jur/100.0*valor) / qtde 
    return (res) 

valor = float(input("Digite o valor da comprar R$: ")) 
qtdeparc = int(input("Digite a quantidade de parcelas: ")) 
jur = int(input("Digite o percentual de juros: ")) 
print("Valor das parcelas: R$", parcela(valor, qtdeparc))  