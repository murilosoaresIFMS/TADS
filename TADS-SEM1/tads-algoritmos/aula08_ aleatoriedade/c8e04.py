# Dados dois inteiros m e n, gerar três inteiros aleatórios entre m e n.

import random

m = int(input("Digite um número: ")) 
n = int(input("Digite um número: "))

if m > n:
    numerosEntre = m - n
if n > m:
    numerosEntre = n - m 

print(m + int(random.random() * numerosEntre)) 
print(m + int(random.random() * numerosEntre))
print(m + int(random.random() * numerosEntre))
