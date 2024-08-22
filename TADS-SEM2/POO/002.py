class Idades:
    def __init__(self, lista = [19,20]):
        self.lista = lista 

    def append(self, value : int):
        if type(value) == str:
            print('Não pode adicionar STRING')
            return 
        self.lista.append(value)

    def media(self):
        soma = 0
        for i in range(len(self.lista)):    
            soma += self.lista[i]
        return soma // len(self.lista)
    
obj = Idades()
obj.append(35)
obj.append('Oi')
print(obj.media())