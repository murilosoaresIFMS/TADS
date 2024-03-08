# Dada uma sequência de inteiros seguida por um múltiplo de 6, qual a soma dos múltiplos de 3 e a soma dos múltiplos de 2? Múltiplos de 6 não devem ser contabilizados na soma. Exemplo: Dada a sequência 5 3 9 11 14 7 4 12, as somas dos múltiplos de 3 e 2 respectivamente são 12 e 18.

n = int(input("Digite um número (ou -1 para encerrar): "))
multiplos_2 = 0
multiplos_3 = 0
while (n >= 0):
    if (n % 2 == 0):
        multiplos_2 += n
        if (n % 6 == 0):
            multiplos_2 -= n 
    if (n% 3 == 0):
       multiplos_3 += n 
       if (n % 6 == 0):
            multiplos_3 -= n 
    n = int(input("Digite um número (ou -1 para encerrar): "))

print(multiplos_3, multiplos_2)
