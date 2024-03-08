# 9. Ler um número inteiro e escrever um valor aleatório com base nesse número: uma letra maiúscula se o usuário inseriu 1, uma letra minúscula se o usuário inseriu 2 e um dígito se o usuário inseriu qualquer valor que não seja 1 ou 2.

import random

intNumber = int(input("Digite um número: "))

if intNumber == 1: 
    print(chr(97 + int(random.random() * 26)))
elif intNumber == 2:
    print(chr(64 + int(random.random() * 26)))
else:
    print(int(random.random() * 10))