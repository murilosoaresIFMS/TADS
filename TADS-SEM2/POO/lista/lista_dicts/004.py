"""Escreva uma função que receba um inteiro k e retorne um novo dicionário 
cujas chaves são os valores de 1 a k e os valores sejam o valor da chave ao 
quadrado. Exemplo, se k = 15, a saída deve ser o dicionário: 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 
100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} 
 """

def square_dict(n):
    this_dict = {}
    for i in range(1, n+1):
        this_dict[i] = i ** 2
    return this_dict

dict = square_dict(15)
print(dict)