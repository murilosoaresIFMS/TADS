class Funcionario:
    def __init__(self, nome:str, cargo:str, valor_hora_trabalhada:float):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    @property # Faz o método se comportar como um Get
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    @property # Faz o método se comportar como um Get
    def salario(self):
        return self.__salario
    
    @salario.setter 
    def set_salario(self, valor):
        self.__salario = valor

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1 # incremento de um

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


f1 = Funcionario(nome = 'Pedro', 
                 cargo = 'Programador', 
                 valor_hora_trabalhada = 35)

f1.calcula_salario()

print('Horas trabalhadas: ', f1.horas_trabalhadas)
print('Salário: ', f1.salario * 30)

