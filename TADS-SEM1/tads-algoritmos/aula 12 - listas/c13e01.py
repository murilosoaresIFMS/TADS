# Ler uma lista de n itens. Escrever os n itens normalmente em uma linha e do último para o primeiro em outra linha.

lista = []

n = int(input("Digite: "))

for i in range(n):
    elemento = input("Digite um elemento: ")
    lista.append(elemento)

for i in range(n):
    print(lista[i], end = " ")