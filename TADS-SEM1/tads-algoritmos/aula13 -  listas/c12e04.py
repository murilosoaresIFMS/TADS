vezesRepetidas = 0
lista = []

quantidadeDeElementos = int(input("Digite a quantidade de elementos na lista: "))

for i in range(quantidadeDeElementos):
    elemento = input("Digite um elemento: ")
    lista.append(elemento)

for i in range(len(lista)): # Lê os itens individualmente
    for q in range(len(lista)): # Lê a lista por inteiro, para cada item individual

        if i == q: continue # Pula a comparação entre elementos de mesmo indíce (sempre serão iguais)
        if (lista[i] == lista[q]): vezesRepetidas += 1 # Verifica se o elemento se repete em outros pontos

if vezesRepetidas > 0: print("Sim")
else: print("Não")
