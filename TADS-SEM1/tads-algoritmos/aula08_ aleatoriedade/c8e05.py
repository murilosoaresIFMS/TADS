# Dados dois inteiros m e n, gerar três inteiros aleatórios múltiplos de m entre 0 e n.

import random

m = int(input("Digite um número: "))
n = int(input("Digite um número: "))
sorteio = []

c = 0

while(c<3): 
    s = int(random.random() * n)
    if s % m == 0:
        if s != 0:
            c += 1 
            sorteio.append(s)

print(sorteio)