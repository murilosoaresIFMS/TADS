"""Escreva uma função chamada cumsum que receba uma lista de números e 
retorne a soma cumulativa; ou seja, uma nova lista onde o elemento com 
índice i é a soma dos primeiros i+1 elementos da lista original. Por exemplo:"""

def cums_sum(t, new_list = []):
    for index in range(len(t)):
        if (index==0):
            new_list.append(t[index])
            continue 
        if (index <= len(t)):
            sum = t[index] + t[index - 1] 
            new_list.append(sum)
    return new_list

t = [1, 2, 3]
print(cums_sum(t))