##Crie uma função que receba um número e retorne o fatorial desse número. O fatorial de um número n é dado por n! = n × (n-1) × ... × 1.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1) 

n = int(input("Digite um número: "))

print(fatorial(n))