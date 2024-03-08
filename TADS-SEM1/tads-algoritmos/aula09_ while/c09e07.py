# Dada uma sequência de números que termina quando sua soma ultrapassar 1000, qual o maior número?

n = int(input("Digite um número: "))
soma = n
maior = 0

while soma <= 1000:
    n_Reserva = n 
    n = int(input("Digite um número: "))
    if n > n_Reserva:
        if n > maior:
            maior = n 
    elif n_Reserva > n:
        if n_Reserva > maior:
            maior = n_Reserva 
    soma += n 
    
print("A soma é ", soma, " e o maior número digitado foi ", maior)