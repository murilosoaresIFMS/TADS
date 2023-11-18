n = int(input("Quantos amigos você quer adicionar na sua lista: "))
amigos = []

print(f"Digite o nome de seus {n} amigos: ")
for i in range(n):
    amigo = input()
    amigos.append(amigo)

print("Digite os amigos que você quer remover da lista: ")

continuar = True

while continuar:
    continuar = False
    removido = input()
    for i in range(n):
        if amigos[i] == removido:
            amigos[i] = 0
            continuar = True
            print(f"{removido} excluído da sua lista")
            break

print("Sua lista de amigos resultante é: ")
print(amigos)
