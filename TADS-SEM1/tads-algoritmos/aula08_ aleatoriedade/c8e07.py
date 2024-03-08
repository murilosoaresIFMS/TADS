# Gerar uma letra aleatória entre 'a' e 'z'.

import random

gerador = 97 + int(random.random() * 27)
letra = chr(gerador)

print(f'Letra: {letra}')
