"""Programa de cálculo de juros compostos. Imagine que você está investindo teu dinheiro em um ativo financeiro que te proporciona juros compostos. A fórmula dos juros compostos é
M=C(1+i)  ^ t
 
, onde: C é o valor inicial do investimento (o capital); i é a taxa de juros por período (por exemplo, utilize 0.05 para 5% de juros); t é a quantidade de períodos investidos; M é o montante total ao final de t períodos. Por exemplo, ao investir $1000 em um ativo que rende 5% ao ano, ao final de 10 anos você terá acumulado M=$1000(1+0.05) 
10
 =$1628.89.
Dado o capital investido, a taxa de juros anual e a quantidade de anos de investimento, qual o montante ao final de cada ano?"""

capital = float(input("Digite o capital investido: "))
taxa = float(input("Digite a taxa de juros anual: "))
anos = int(input("Digite a quantidade de anos de investimento: "))

for ano in range(1, anos+1):
    montante = capital * (1+taxa) ** anos

print(f"Montante: U$ {montante:.2f}")
