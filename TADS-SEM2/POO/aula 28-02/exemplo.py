class Pessoa:
    def __init__(self, nome, sobrenome, ano):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.ano = ano

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def idade(self):
        return 2024 - self.ano 

p1 = Pessoa("Fulano", "Da Silva", 2005)
p2 = Pessoa("Ciclano", "De Souza", 2002)

print(p1.nome_completo())
print(p1.idade())