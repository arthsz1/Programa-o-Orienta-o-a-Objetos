s = float(input("Digite a distancia percorrida pelo objeto em km: ")) 
t = float(input("Digite o tempo transcorrido, em h: "))
if t > 0:
          v=s/t
          print("A velocidade do objeto é ",v,"km/h")
else:
          print("Erro, o valor do tempo deve ser positivo!")
          print("Tente novamente")