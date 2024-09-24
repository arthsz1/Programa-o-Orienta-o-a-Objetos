aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

notas_aluno1 = [
    int(input(f"Digite a nota da primeira prova de {aluno1}: ")),
    int(input(f"Digite a nota da segunda prova de {aluno1}: ")),
    int(input(f"Digite a nota da terceira prova de {aluno1}: ")),
    int(input(f"Digite a nota da quarta prova de {aluno1}: "))
]

notas_aluno2 = [
    int(input(f"Digite a nota da primeira prova de {aluno2}: ")),
    int(input(f"Digite a nota da segunda prova de {aluno2}: ")),
    int(input(f"Digite a nota da terceira prova de {aluno2}: ")),
    int(input(f"Digite a nota da quarta prova de {aluno2}: "))
]

notas_aluno3 = [
    int(input(f"Digite a nota da primeira prova de {aluno3}: ")),
    int(input(f"Digite a nota da segunda prova de {aluno3}: ")),
    int(input(f"Digite a nota da terceira prova de {aluno3}: ")),
    int(input(f"Digite a nota da quarta prova de {aluno3}: "))
]

notas_aluno4 = [
    int(input(f"Digite a nota da primeira prova de {aluno4}: ")),
    int(input(f"Digite a nota da segunda prova de {aluno4}: ")),
    int(input(f"Digite a nota da terceira prova de {aluno4}: ")),
    int(input(f"Digite a nota da quarta prova de {aluno4}: "))
]

# Calcular as médias
media1 = sum(notas_aluno1) / 4
media2 = sum(notas_aluno2) / 4
media3 = sum(notas_aluno3) / 4
media4 = sum(notas_aluno4) / 4

# Calcular a média da sala
mediasala = (media1 + media2 + media3 + media4) / 4

# Exibir as médias  
print(f"A média de {aluno1} é {media1:.2f}")
print(f"A média de {aluno2} é {media2:.2f}")
print(f"A média de {aluno3} é {media3:.2f}")
print(f"A média de {aluno4} é {media4:.2f}")
print(f"A média da sala é {mediasala:.2f}")
