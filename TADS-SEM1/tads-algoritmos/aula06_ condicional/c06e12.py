"""Dado o preço da etiqueta de um produto e o código da condição de pagamento, qual o valor a ser pago pelo produto? Utilize a seguinte tabela de referência:
Código	Condição de pagamento
1	À vista em dinheiro ou cheque, recebe 10% de desconto
2	No cartão de débito ou PIX, recebe 5% de desconto
3	Em duas vezes, preço normal de etiqueta sem juros
4	Em três vezes, preço normal de etiqueta mais juros de 10%"""

preco = float(input("Digite o valor do produto: R$ "))
codigo = int(input("Digite o código de condição de pagamento: "))

if codigo == 1:
   valor = preco * 0.9
   print("O valor a ser pago será de R$ ", valor, " com desconto de 10%.")
elif codigo == 2:
    valor = preco * 0.95
    print("O valor a ser pago será de R$ ", valor, " com desconto de 5%.")
elif codigo == 3:
    valor = preco / 2 
    print("O valor a ser pago será de R$ ", valor, " dividido em duas vezes.")
elif codigo == 4:
    valor = (preco / 3) + 3 * (preco * 0.9)
    print("O valor a ser pago será de R$ ", valor, " dividido em três vezes e com adicional de 10 % de juros.")
    
