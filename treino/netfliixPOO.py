class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.tipos_planos = ["basic", "premium"]
        if plano in self.tipos_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
    
    def alterar_plano(self, novo_plano):
        if novo_plano in self.tipos_planos:
            self.plano = novo_plano
        else:
           ("Plano inválido")

    def ver_filme(self, filme):
        if self.plano == "premium":
            print(f"Assistindo {filme}")
        else:
            print(f"Faça upgrade para premium para assistir {filme}")

# Exemplo de uso
cliente = Cliente("Arthur Souza", "arthursouza@gmail.com", "basic")
print(cliente.nome)
cliente.ver_filme("Matrix")
cliente.alterar_plano("premium")
cliente.ver_filme("Matrix")
