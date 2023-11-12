# Dado um caractere, ele é uma letra?

caractere = input("Digite um caractere: ")
codigo = ord(caractere)

if codigo >= 65: # Testa se o código é maior que 65
     # Se True, entra aqui. Testa se é menor que 90 ou maior que 97
     if codigo <= 90: 
        print("É uma letra")
     if codigo >= 97: # Caso for maior que 97 e for True, ele testa novamente
        if codigo <= 123: # E verifica se abaixo é menor que 123
            print("É uma letra")
else: # Caso tudo for false, executa isso
    print("Não é uma letra")
    