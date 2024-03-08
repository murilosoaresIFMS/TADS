# Dada uma letra maiúscula, qual sua correspondente em minúsculo?

letra = input("Digite uma letra maiúscula: ")
codigo = ord(letra)

minusculo = codigo + 32

print(f"A letra minúscula correspondente é {chr(minusculo)}")
