"""
Escreva uma função chamada nested_sum que receba uma lista de listas de 
números inteiros e adicione os elementos de todas as listas aninhadas. Por 
exemplo:

"""

def lista_sum(t, sum = 0):
    for index in range(len(t)):
        for nested_index in range(len(t[index])):
            sum += t[index][nested_index]
    return sum

t = [[1, 2], [30], [4, 5, 6]]
print(lista_sum(t))