class Funcionario: 
    def __init__(self, nome: str, cargo: str, valor_hora_trabalhada: float):
        self.nome = nome 
        self.cargo = cargo 
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0 
        self.__salario = 0

    def getHoras(self):
        return self.__horas_trabalhadas 
    
    def setSalario(self):
        return self.__salario

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1 

    def calcula_horario(self):
        self.__salario = self.getHoras * self.valor_hora_trabalhada


f = Funcionario('João', 'Projetista', '30')
