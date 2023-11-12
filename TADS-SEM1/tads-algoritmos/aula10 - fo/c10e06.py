"""Programa de caixa de loja. Ler uma sequência de triplas que correspondem às informações dos produtos comprados: quantidade, preço unitário, nome do produto. Escrever, em uma linha para cada produto, seu nome e o preço total. Escrever na última linha o preço total da compra."""

precoTotal = 0 

for i in range(3):
    print(f"PRODUTO {i + 1}")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))

    precoUnitario = preco * quantidade 
    print(f"PRODUTO: {nome.upper()}, PRECO TOTAL DOS PRODUTOS: R$ {precoUnitario}")
    
    precoTotal += precoUnitario 
    print()

print(f"PREÇO TOTAL DA COMPRA: R$ {precoTotal}")
