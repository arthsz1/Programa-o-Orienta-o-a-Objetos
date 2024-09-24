N = int(input("Quantas pessoas serão processadas? "))
for i in range(N):
    peso = float(input("\nDigite o peso da pessoa, em Kg: ")) 
    altura = float(input("\nDigite a estatura da pessoa, em Metros: ")) 
    if(peso > 0 and altura > 0.10 and altura < 2.5):  
        imc = peso / altura**2 
        print("O IMC é", imc, "kg/m") 
    else: 
        print("Verifique por favor, valor digitados errados!")
print("\n Até logo") 