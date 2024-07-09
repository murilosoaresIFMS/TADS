"""Escreva uma função chamada middle que receba uma lista e retorne uma 
nova lista com todos os elementos originais, exceto o primeiro e o último 
elementos. Por exemplo:"""

def middle(t):
    if len(t) == 2:
        return 'Adicione mais elementos na lista para retornar o meio!'
    for i in range(len(t)): 
        if i == 0:
            del t[i]
        elif (i == len(t) - 1):
            del t[i]
    return t

print(middle([2, 5]))