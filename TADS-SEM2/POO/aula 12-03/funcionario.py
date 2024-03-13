class Funcionario:
    def __init__(self, nome:str, cargo:str, valor_hora_trabalhada:float):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    def getHorasTrabalhadas(self):
        return self.__horas_trabalhadas

    def getSalario(self):
        return self.__salario

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1 # incremento de um

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


f1 = Funcionario(nome = 'Pedro', 
                 cargo = 'Programador', 
                 valor_hora_trabalhada = 35)

f1.registra_hora_trabalhada()
f1.registra_hora_trabalhada()
f1.registra_hora_trabalhada()
f1.registra_hora_trabalhada()
f1.calcula_salario()

print('Horas trabalhadas: ', f1.getHorasTrabalhadas())
print('Salário: ', f1.getSalario())