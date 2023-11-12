# Dado um inteiro n, gerar três inteiros aleatórios entre −n e n.

import random 

N2 = int(input("Digite um número: "))
  
print(-N2 + int(random.random() * N2) )
print(-N2 + int(random.random() * N2) )
print(-N2 + int(random.random() * N2) )
