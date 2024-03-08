class contaCorrente:
    def __init__(self, numero : int, saldo : float): # Self: simboliza o objeto
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor : float):
        if valor > 0:
            self.saldo = self.saldo + valor 
        else: 
            print('Valor insuficiente')

c1 = contaCorrente(123456, 1000.59) # Inicia objeto
c2 = contaCorrente(654321, 500.09) # Inicia objeto

print(f'Conta corrente: {c1.numero}, R$ {c1.saldo}')
print(f'Conta corrente: {c2.numero}, R$ {c2.saldo}')

