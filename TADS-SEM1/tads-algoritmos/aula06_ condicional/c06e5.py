# Dados três inteiros, a soma deles é ímpar?

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
soma = n1 + n2 + n3

if soma % 2 == 1:
    print("Sim")
else:
    print("Não")
    