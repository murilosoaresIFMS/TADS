# Dado um caractere, ele é um algarismo?

caractere = input("Digite um caractere: ")
codigo = ord(caractere)

if codigo >= 48: # Código maior ou igual a 48: TRUE
    if codigo <= 57: # FALSE
        print("É um algarismo")
    else: # TRUE
        print("Não é um algarismo")
