"""Dada uma sequência de duplas de números, representando valores e seus respectivos pesos, seguida por uma dupla de zeros, qual a média ponderada desconsiderando a dupla de zeros?"""

# 1. Ler uma sequência de duplas de números: valor e peso desse valores
    #1.1 Criar variáveis que armazenem: 
        # -> a múltiplicação de valor pelo peso
        # -> a soma entre os pesos
        # -> a quantidade de totais acima 
    #1.2 O loop é encerrado com uma flag
# 2. Criar variável para média ponderada

soma = 0
quantidade = 0
sentinela = 0

while(sentinela == 0):
    print("DIGITE UMA SEQUÊNCIA DE ZEROS PARA ENCERRAR A LEITURA!")
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite o peso: "))
    if (n1 != 0 or n2 != 0): # Sequência de zeros barrada pois não entra no cálculo
        peso = n1 * n2
        soma += peso
        quantidade += 1  
    else:
        sentinela += 1 

if quantidade == 0:
    print("Nenhum valor foi inserido!")
else:
    mediaPonderada = soma / quantidade
    print("A média ponderada é ", mediaPonderada)
    