# Dada uma letra e um inteiro N, qual a letra correspondente ao andar N casas à frente da letra lida (ou atrás, se o N for negativo).

letra = input("Digite uma letra: ")
n = int(input("Digite um numero: "))

codigo = ord(letra)
letraCorrespondente = codigo + n 

print(f"O caractere correspondente é {chr(letraCorrespondente)}")
