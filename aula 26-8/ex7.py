def parcela(valor,qtdeparc):
    res = (valor + 0.05*valor) / qtdeparc
    return (res)
valor = float(input("Digite o valor da comprar R$: "))
qtdeparc = int(input("Digite a quantidade de parcelas: "))
print("Valor das parcelas: R$", parcela(valor, qtdeparc)) 