from abc import ABC, abstractmethod

class Empregado(ABC):
    def __init__(self, nome:str, idade:int):
        self.nome = nome 
        self.idade = idade 

    @abstractmethod
    def ganha(self):
        pass

# Herança
class Horista(Empregado):
    pass

h1 = Horista(nome='Fulano', idade=30)