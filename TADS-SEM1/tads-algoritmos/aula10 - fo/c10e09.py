"""Dado um inteiro n e um dígito d, quantas vezes d ocorre em n? Por exemplo, o dígito 2 ocorre 3 vezes em 762021192."""

n = int(input("Digite um número inteiro: "))
digito = int(input("Qual dígito deseja ler nesse número? ")) 

divisao = n
contadorDigito = 0

while divisao > 0:
    resto = divisao % 10 
    if resto == digito: 
        contadorDigito += 1
    divisao = divisao // 10 

print(f"Quantas vezes {digito} aparece em {n} -> ", contadorDigito)
