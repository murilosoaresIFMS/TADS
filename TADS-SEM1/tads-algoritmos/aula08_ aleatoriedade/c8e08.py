# Gerar uma senha aleatória de 8 dígitos com letras maiúsculas, minúsculas e inteiros.

import random 

p1 = chr(97 + int(random.random() * 26))
p2 = chr(65 + int(random.random() * 26))
p3 = chr(97 + int(random.random() * 26))
p4 = chr(65 + int(random.random() * 26))
p5 = str(int(random.random() * 10))
p6 = str(int(random.random() * 10))
p7 = str(int(random.random() * 10))
p8 = str(int(random.random() * 10))

print(f"Senha: {p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8}")