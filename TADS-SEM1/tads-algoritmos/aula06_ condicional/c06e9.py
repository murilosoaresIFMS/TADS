""" Em certa região, o preço pelo fornecimento de energia elétrica depende do consumo em kWh, conforme a seguinte tabela:
Faixa (kWh)	Preço (R$)
    500	        0,40
Acima de 500	0,65 

Dado o consumo de uma residência em kWh, qual o preço da energia a ser pago?

"""

consumo = int(input("Digite o consumo de sua residência em kWh: "))

if consumo <= 500:
    preco = 0.40 * consumo
    print("O preço a ser pago é de R$ ", preco)
elif consumo > 500:
    preco = 0.65 * consumo
    print("O preço a ser pago é de R$ ", preco)

