# Encapsulamento: proteger dados de um objeto

class contaCorrente:
    
    def __init__(self, numero : int, saldo : float):
        self.numero = numero
        self.__saldo = saldo # Atributo __privado

    # É recomendado criar métodos para acessar atributos privados
    def getSaldo(self):
        return self.__saldo
    
    # Também há o método de alteração de atributo
    def setSaldo(self, valor : float):
        self.__saldo = valor

    def depositar(self, valor : float):
        if valor > 0:
            self.__saldo = self.__saldo + valor 
        else: 
            print('Valor insuficiente')

    def sacar(self, valor: float):
        if self.__saldo >= valor: 
            self.__saldo = self.__saldo - valor 

c1 = contaCorrente(123456, 1000.59) 
c2 = contaCorrente(654321, 500.09) 

print(f'Conta corrente: {c1.numero}, R$ {c1.getSaldo()}') # Acesso livre aos atributos
print(f'Conta corrente: {c2.numero}, R$ {c2.getSaldo()}') # Acesso livre aos atributos

# c1.saldo = 100000 # Ação indesejada, evitada pelo encapsulamento

# ----------------------------------------------------------------------- #

class Pessoa:
    def __init__(self, nome, sobrenome, ano):
        self.__nome = nome 
        self.sobrenome = sobrenome
        self.ano = ano

    def getNome(self):
        return self.__nome 
    
    def setNome(self, novo_nome : str):
        if (len(novo_nome) >= 2):
            self.__nome = novo_nome

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def idade(self):
        return 2024 - self.ano 

p1 = Pessoa("Fulano", "Da Silva", 2005)
p2 = Pessoa("Ciclano", "De Souza", 2002)

print(p1.nome_completo())
print(p1.idade())
