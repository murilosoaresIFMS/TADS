"""Escreva um código em Python que, dadas duas listas, converta-as em um 
dicionário de tal forma que os itens da primeira lista sejam chaves e os 
itens da segunda lista sejam valores do dicionário, na mesma ordem. Exem-
plo:"""

keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30] 

dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]

print(dict)