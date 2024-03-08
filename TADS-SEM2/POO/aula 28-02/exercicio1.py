class ContaCorrente:

    def __init__(self, numero, saldo):
        self.numero = numero 
        self.saldo = saldo 

    def depositar(self, deposito):

        if deposito > 0:
            self.saldo = self.saldo + deposito 
            return f'Depósito realizado com sucesso'
        else: 
            return 'Depósito deve ser maior que R$ 0!'
        
    def sacar(self, saque):
        if self.saldo > saque and saque > 1:
            self.saldo = self.saldo - saque
            return f'Saldo realizado com sucesso!' 
        else:
            return 'Valor indisponível para o saque!'
        
    def visualizarSaldo(self):
        return f'Saldo disponível: R$ {self.saldo}'
    

conta = ContaCorrente(2, 10000)

saque = 0
deposito = 10

print(conta.sacar(saque))
print(conta.depositar(deposito))
print(conta.visualizarSaldo())

print('a')