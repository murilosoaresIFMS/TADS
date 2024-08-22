class Pessoa:
    # Construtor default não tem parâmetros
    def __init__(self):
        self.disarranged = []
        self.arranged = []

    def append(self, value : str):
        self.disarranged.append(value)
        i = 0
        while self.disarranged[i] < value:
            i+= 1
        self.arranged.insert(i, value)

    def acessa(self, posicao : int):
        try:
            return self.arranged[posicao]
        except IndexError:
            return 'Não existe'
    


obj = Pessoa()

obj.append('Carlos')
obj.append('Barnabé')
obj.append('Ava Max')

print(obj.acessa(3))
print(obj.arranged)