# Dados dois números, qual o maior deles e a diferença absoluta entre eles? (a diferença absoluta é o maior menos o menor)

n1 = int(input("Digite um número:  "))
n2 = int(input("Digite outro número:  "))

if n2 > n1:
    maior = n2
    menor = n1 
else: 
    maior = n1
    menor = n2

diferenca = maior - menor

print("A diferença absoluta entre os valores é: ", diferenca)
