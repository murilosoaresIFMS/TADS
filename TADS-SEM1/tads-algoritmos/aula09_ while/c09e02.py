"""Qual o intervalo de inteiros de cada item a seguir? (escrever cada intervalo em uma linha)
[0, 10[
]10, 0]
[-10, 10]
[100, 1]"""

i = 0 

print('Intervalo de [0, 10[ ', end = ': ')
while(i < 9):
    i += 1 
    print(i, end = ' ')

i = 9

print('\nIntervalo de ]10, 0] ', end = ': ')
while(i > 0):
    i -= 1 
    print(i, end = ' ')

i = -11

print('\nIntervalo de [-10, 10] ', end = ': ')
while(i < 10):
    i += 1 
    print(i, end = ' ')

i = 101

print('\nIntervalo de [100, 1] ', end = ': ')
while(i > 1):
    i -= 1 
    print(i, end = ' ')
    