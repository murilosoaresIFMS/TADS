# Dada uma letra, ela é maiúscula ou minúscula?

letra = input("Digite uma letra: ")
codigo = ord(letra)

if codigo >= 65: 
     if codigo <= 90: 
        print("Letra maiúscula")
     if codigo >= 97: 
        if codigo <= 123:
            print("Letra minúscula")
else: 
    print("Não é uma letra")
    