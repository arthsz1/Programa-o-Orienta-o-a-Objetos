resp = 'Sim' 
while resp == "Sim": 
    peso = float(input("\nDigite o peso da pessoa, em Kg: ")) 

    altura = float(input("\nDigite a estatura da pessoa, em Metros: ")) 
    if(peso > 0 and altura > 0.10 and altura < 2.5):  
        imc = peso / altura**2 
        print("O IMC é", imc, "kg/m") 

    if(imc <= 18.5): 
        print('Baixo peso.')  
    elif(imc > 18.6 and imc <= 24.9): 
        print("Peso Normal.")  
    elif(imc > 25 and imc <= 29.9): 
        print("Sobrepeso.")  
    elif(imc > 30 and imc <= 34.9): 
        print("Obesidade grau 1.")  
    elif(imc > 35 and imc <= 39.9): 
        print("Obesidade grau 2.")  
    elif(imc > 40): 
        print("Obesidade grau 3.")  
    else: 
        print("Erro nos dados. Por favor, verifique os valores digitados!") 
    resp = input("\n Deseja continuar (Sim ou Não)? ") 
print("\n Até logo") 