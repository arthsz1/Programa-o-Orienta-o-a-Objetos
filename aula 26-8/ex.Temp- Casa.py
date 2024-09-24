# Faça um programa que converta uma temperatura digitada em Celsius para Fahrenheit e vice-versa.
print("Digite uma opção: \n 1. Celsius para Fahrenheit \n 2. Fahrenheit para Celsius")

opcao = int(input("Digite sua opção: "))

if opcao == 1: 
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"A temperatura em Celsius é: {celsius:.2f}°C")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
