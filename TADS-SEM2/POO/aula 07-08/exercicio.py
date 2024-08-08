"""
// mrl
from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, velocidade:float, marca:str, metros:int):
        self.velocidade = velocidade
        self.marca = marca 
        self.metros = metros
    
    @abstractmethod
    def mover():
        pass

class Carro(Veiculo):

    def __init__(self, velocidade, marca, metros, numPortas:int):
        super().__init__(velocidade, marca, metros)
        self.numPortas = numPortas

    def mover(self):
        print(f"Carro se moveu {self.metros} m")

class Aviao(Veiculo):

    def __init__(self, velocidade, marca, metros, tipo:str):
        super().__init__(velocidade, marca, metros)
        self.tipo = tipo

    def mover(self):
        print(f"Aviao se moveu {self.metros} m")

class Barco(Veiculo):

    def __init__(self, velocidade, marca, metros, tamanho:int):
        super().__init__(velocidade, marca, metros)
        self.tamanho = tamanho

    def mover(self):
        print(f"Barco se moveu {self.metros} m")

carro = Carro(velocidade=2, marca='Fiat', metros=100, numPortas=4)
aviao = Aviao(velocidade=2, marca='Sla', metros=160, tipo="De 2 asas")
barco = Barco(velocidade=2, marca='OBarco', metros=130, tamanho=40000)

carro.mover()
aviao.mover()
barco.mover()

"""
# correcao

from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, velocidade:int=0, marca:str = ''):
        self.velocidade = velocidade
        self.marca = marca

    @abstractmethod
    def mover(self, metros:int):
        pass

class Carro(Veiculo):
    def __init__(self, velocidade:int=0, marca:str = '', numPortas:int = 0):
        super().__init__(velocidade, marca)
        self.numPortas = numPortas

    def mover(self, metros:int):
        print(f'O carro {self.marca} moveu {metros} m')

c1 = Carro(marca='Honda', velocidade=100, numPortas=4)
c1.mover(300)