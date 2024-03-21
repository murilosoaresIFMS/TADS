
class BombaCombustivel:
    def __init__ (self, valorLitro : float, quantidadeCombustivel : float):
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    def __str__(self): # Volta o objeto
        return (f'Valor litro: R${self.__valorLitro:.2f}, Quantidade combustível: {self.__quantidadeCombustivel:.2f} L')

    # Método que retorna verdadeiro caso tenha conseguido abastecer, ou falso caso contrário;
    def alterarQuantidadeCombustivel(self, litros: float): # setter
        valor = litros * self.__valorLitro
        if self.__quantidadeCombustivel >= litros: 
            self.__quantidadeCombustivel -= litros
            print(f'Abasteceu {litros:.2f} L')
            print(f'Custo: R$ {valor:.2f}')
            return True
        else:
            print('Não há combústivel suficiente')
            return False
    
    def abastecerPorValor(self, valor:float):
        litros = valor / self.__valorLitro 
        self.alterarQuantidadeCombustivel(litros)
    
    def abastecerPorLitro(self, litros:float):
        self.alterarQuantidadeCombustivel(litros)
  
    def alterarValor(self, novo_valor): # setter
        if novo_valor > 0:
            self.__valorLitro = novo_valor
    



b1 = BombaCombustivel(valorLitro = 5.48, quantidadeCombustivel = 121.9)

print(b1)
b1.abastecerPorValor(50)
print(b1)
b1.abastecerPorLitro(20)
print(b1)