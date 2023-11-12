# Dadas duas letras, quantas letras há entre as duas?

letra = input("Digite uma letra: ")
codigo1 = ord(letra)

letra2 = input("Digite outra letra: ")
codigo2 = ord(letra2)

if codigo1 > codigo2:
    letrasMeio = codigo1 - codigo2 
else:
    letrasMeio = codigo2 - codigo1

print(f"Existem {letrasMeio} letras entre {letra} e {letra2}")