n = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(n):
    lista.append(0)

while True: 
    i = int(input("Digite o índice: "))
    if i >= n or i < 0:
        print("índice inválido!")
        break
    x = int(input("Digite o item: "))

    lista[i] = x

print("A lista resultante é:")
print(lista)

