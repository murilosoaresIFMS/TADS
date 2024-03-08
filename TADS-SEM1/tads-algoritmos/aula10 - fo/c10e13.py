"""Decompor um número em fatores primos ou, fatorá-lo, é escrever este número como uma multiplicação de números primos. Os fatores são termos da multiplicação que, neste caso, são números primos. A fatorização é uma técnica usada em muitos algoritmos de criptografia sem os quais a internet não existiria da forma como a conhecemos. A fatoração de um número natural qualquer se dá pela seguinte forma: Divida o número pelo seu menor divisor primo. O quociente será o novo número. Continue dividindo o número pelo seu menor divisor primo até chegar em 1. A multiplicação de todos os divisores dará o valor do número original."""

print("FATORAÇÃO: ")

n = int(input("Digite um número: "))
print(f'{n}', end = ' = ')

# Essa estrutura de repetição serve para retirar de N qualquer divisão possível por 2.

while n % 2 == 0:
    n = n // 2 
    print('2', end = ' * ')

# Essa estrutura de repetição faz duas coisas:
    # 1. Encontra os números primos dentro do intervalo (3, n). Isto é, se n = 5, ele procura números primos na sequência: 3, 4, e 5.
        # Isso é feito através da divisão individual de cada número por valores entre 2 e primo -1. Logo, se quero saber se 5 é um número primo,
        # serão realizadas as divisões de 5, será realizada a divisão de 5 por 3 e 5 por 4. Se todos os valores diferem de zero, não existe intervalo entre 1 e 5 no qual 5 possui um múltiplo - logo, ele é primo. 
    # 2. Ao encontrar um número primo, é verificado se esse número primo divide n. Caso aconteça, isso significa que ele é um múltiplo.

for primo in range(3, n + 1):
    nPrimo = True 
    for d in range(2, primo):

        if ((nPrimo == True) and (primo % d == 0)):
            nPrimo = False 

        if ((d == primo - 1) and (nPrimo == True)): # Esta condição serve para certificar
            while n % primo == 0: 
                n = n // primo
                print(f'{primo}', end = ' * ')

print('1', end = ' ')
