class Data:
    # ==== 1. Represente uma data utilizando três atributos ====
    def __init__(self, dia , mes, ano):
        
        # ==== 2. Verifica validade dos dados ====

        if mes <= 0 or mes > 12:
            raise('Mês instanciado não EXISTE!!')
        
        if dia <= 0 or dia > 31:
            raise('O dia instanciado não EXISTE!!')

        if mes == 4 or mes == 6 or mes == 9 or mes == 1:
            if dia > 30:
                raise ('O dia demarcado não existe para o mês especificado!')        

        if mes == 2: 
            if dia > 28:
                raise ('O dia demarcado não existe para o mês especificado!')
        
        self.__mes = mes 
        self.__ano = ano 
        self.__dia = dia

    # ==== 3. Getters & Setters ====

    @property
    def getDay(self):
        return self.__dia
    
    @property
    def getMonth(self):
        return self.__mes
    
    @property
    def getYear(self):
        return self.__ano
    
    @getDay.setter
    def setDay(self, value):
        self.__dia = value
    
    @getMonth.setter
    def setMonth(self, value):
        self.__mes = value

    @getYear.setter
    def setYear(self, value):
        self.__ano = value

    # ==== 4. Método STR ====

    def __str__(self):
        if (self.__dia <= 9 and self.__mes <= 9): return f'0{self.__dia}/0{self.__mes}/{self.__ano}'
        if (self.__mes <= 9): return f'{self.__dia}/0{self.__mes}/{self.__ano}'
        if (self.__dia <= 9):  return f'0{self.__dia}/{self.__mes}/{self.__ano}'
        else: return f'{self.__dia}/{self.__mes}/{self.__ano}'
    
    def avancarDia(self):

        if (self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11) and (self.__dia == 30):
            self.__dia = 1 
            self.__mes += 1

        elif (self.__mes == 2 and self.__dia == 28):
            self.__dia = 1 
            self.__mes += 1
        
        elif (self.__mes == 12 and self.__dia == 31):
            self.__dia = 1
            self.__mes = 1 
            self.__ano += 1

        elif (self.__dia == 31): 
            self.__dia = 1
            self.__mes += 1

        else: 
            self.__dia += 1


        print(Data.__str__(self))
    
    
novaData = Data(1, 1, 2024)
