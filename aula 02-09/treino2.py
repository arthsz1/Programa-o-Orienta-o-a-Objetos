class cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
cliente1 = cliente("Arthur Saraiva", "123.456.789-00", 18)
print(cliente1.nome, cliente1.cpf, cliente1.idade)

class curso:
    def __init__(self, idCurso,nome,qntdalunos):
        self.idCurso = idCurso
        self.nome = nome
        self.qntdalunos = qntdalunos
curso1 = curso(1, "Ciência da Computação", 90) 
print(curso1.idCurso, curso1.nome, curso1.qntdalunos)