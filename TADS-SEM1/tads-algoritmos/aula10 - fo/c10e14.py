# Dado um natural, qual seu fatorial? (sugestão: use long ao invés de int)

n = float(input("Digite um número: "))
fatorial = int(n)

for i in range(fatorial-1, 1, -1):
    fatorial *= i 

print(f"Fatorial de N: {fatorial}")
