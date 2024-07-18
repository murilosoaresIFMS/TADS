"""Escreva uma função chamada extract que receba um dicionário e uma lista 
como parâmetro. A função deve retornar um novo dicionário que extraia os 
elementos do dicionário original usando os elementos da lista como chaves 
a extrair. Exemplo:"""

def extract(dict, keys):
    the_dict = {}
    for key in dict:
        for element in keys: 
            if (key == element):
                the_dict[key] = sample_dict[key]
    return the_dict

sample_dict = { 
    "name": "Kelly", 
    "age": 25, 
    "salary": 8000, 
    "city": "New York"}

keys = ["name", "salary"]

dict = extract(sample_dict, keys)
print(dict)    
    