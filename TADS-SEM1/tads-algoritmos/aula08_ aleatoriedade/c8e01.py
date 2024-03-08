# Dado um inteiro como semente, gerar três inteiros aleatórios.

import random 

random.seed(700)

print(int(random.random() * 1000))
print(int(random.random() * 100))
print(int(random.random() * 10))
