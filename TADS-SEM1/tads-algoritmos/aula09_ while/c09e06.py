# Dada uma sequência de números seguida pelo número zero, qual a soma dos números?

sequencia = int(input("Digite: "))

i = 0
s = 0

while(i < sequencia):
    s = i + s # Variável s é somada com o valor de i  
    print(f'{i} + {i + 1} = {s}') # Exibição visual da soma
    i += 1 # I é incrementado por 1


 