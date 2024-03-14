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
combustível restante na bomba.

• OBS: Sempre que acontecer um abastecimento é necessário atualizar a
quantidade de combustível total na bomba."""

class BombaCombustivel:

    def __init__(self, valorLitro, quantidadeCombustivel):  
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        self.quantidadeCombustivel += valor / self.valorLitro
        print(f'Quantidade disponível: {self.quantidadeCombustivel} L')

    def abastecerPorLitro(self, valor):
        valorPago = valor * self.quantidadeCombustivel
        print(f'Valor pago: R$ {valorPago}')
    """
    def alterarValor():
    def alterarQuantidadeCombustivel:
    """

carro = BombaCombustivel(10, 0)
