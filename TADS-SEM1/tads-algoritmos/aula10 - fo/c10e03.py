"""Dados dois números inteiros, multiplicá-los usando somas repetidas. Não pode usar o operador de multiplicação "*". Sugestão: usar um laço e o operador de soma (+)."""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: ")) 

m = 0

if (n2 > n1):
    for i in range(1, n2+1): 
        m += n1 
else: 
    for i in range(1, n1+1):
        m += n2 

print(f"Multiplicação de {n1} por {n2} = {m}")
