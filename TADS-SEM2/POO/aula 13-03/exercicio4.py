"""
Faça um programa que possua uma classe chamada
BombaCombustivel, com os atributos:

• valorLitro
• quantidadeCombustivel
• E com os métodos:

• abastecerPorValor() – método onde é informado o valor a ser
abastecido e mostra a quantidade de litros que foi colocada no
veículo
• abastecerPorLitro() – método onde é informado a quantidade
em litros de combustível e mostra o valor a ser pago pelo cliente.
• alterarValor() – altera o valor do litro do combustível.
• alterarQuantidadeCombustivel() – altera a quantidade de
combustível restante na bomba. b

• OBS: Sempre que acontecer um abastecimento é necessário atualizar a
quantidade de combustível total na bomba."""

class BombaCombustivel:
    def __init__ (self, valorLitro : float, quantidadeCombustivel : float):
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        abastecimento = valor / self.__valorLitro
        return f'Abastecimento: {abastecimento:.2f} L'

    def abastecerPorLitro(self, valor):
        abastecimento = self.__valorLitro * valor 
        return f'Abastecimento: R$ {abastecimento:.2f}' 

    def alterarValor(self): # setter
        pass 

    def alterarQuantidadeCombustivel(self): # setter
        pass

b1 = BombaCombustivel(valorLitro = 5, quantidadeCombustivel = 121.9)

print(b1.abastecerPorValor(50))
print(b1.abastecerPorLitro(10))