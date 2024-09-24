x = float(input('Digite o valor de X: '))

if x>= 0 and x<=10:
    print('O valor digitado se encontra entre 0 e 10.')
elif x > 10 and x<=20:
    print('O valor digitado se encontra entre 10 e 20.')
elif x > 20 and x<=30:
    print('O valor digitado se encontra entre 20 e 30.')
elif x > 30 and x<=40:
    print('O valor digitado se encontra entre 30 e 40.')
elif x > 40 and x<=50:
    print('O valor digitado se encontra entre 40 e 50.')
else:
    print('O valor de X é negativo ou maior que 50.')