# Um natural é dito triangular se ele é produto de três naturais consecutivos. Exemplo: 120 é triangular, pois 4⋅5⋅6=120. Dado um natural, ele é triangular?

num = int(input("Digite um número natural: "))

n = 0

triangular = n * (n+1) * (n+2)

while (triangular < num):
    n += 1 
    triangular = n * (n+1) * (n+2)

if (triangular == num):
    print("É triangular")
else:
    print("Não é triangular")
    