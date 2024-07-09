"""Escreva uma função chamada is_sorted que tome uma lista como parâme-
tro e retorne True se a lista estiver classificada em ordem ascendente, e 
False se não for o caso. Por exemplo:"""

def is_sorted(list):
    for i in range(len(list)):
        if (type(list[i]) != int):
            return False
            
    for i in range(len(list)):
        if i + 1 != (len(list)):
            if (list[i] != (list[i + 1] - 1)):
                return False
            
    return True

print(is_sorted([2, 3,4,5]))
