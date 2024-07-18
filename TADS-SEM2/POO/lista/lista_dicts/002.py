"""Crie uma função que receba dois dicionários e junte-os em apenas um. 
Exemplo: """
 
def joinDicts(d1, d2):
    this_dict = {}
    for key in d1:
        this_dict[key] = d1[key]
    for key in d2:
        this_dict[key] = d2[key]
    return this_dict 

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}        

dict3 = joinDicts(dict1, dict2)
print(dict3)
