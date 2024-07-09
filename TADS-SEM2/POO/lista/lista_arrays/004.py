"""Escreva uma função chamada chop que tome uma lista alterando-a para re-
mover o primeiro e o último elementos, e retorne None. Por exemplo:"""

def chop(t):
    for i in range(len(t)): 
        if i == 0:
            del t[i]
        elif (i == len(t) - 1):
            del t[i]
    return None 

t = [1, 2, 3, 4] 
print(chop(t))
