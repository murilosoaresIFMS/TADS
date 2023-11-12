#Dados três números, qual o maior?

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2:
    if n1 > n3:
        print("O maior número é ", n1)
elif n2 > n1:
     if n2 > n3:
         print("O maior número é ", n2)
elif n3 > n1:
     if n3 > n2:
        print("O maior número é ", n3)
