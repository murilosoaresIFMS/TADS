# Dado um inteiro n, gerar três inteiros aleatórios entre 0 e n

import random 

n = int(input("Digite um inteiro: "))

print(int(random.random() * n))

