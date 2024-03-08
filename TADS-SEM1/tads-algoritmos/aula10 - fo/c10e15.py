# Sejam dois naturais n≥p, podemos calcular seu número binomial como n ! / p! (n-p)!

n = float(input("Digite um número natural N: "))
p = float(input("Digite um número natural P: "))

if n >= p:
    op = n - p
    for i in range(int(n-1), 0, -1):
        n *= i 
    for i in range(int(p-1), 0, -1):
        p *= i 
    for i in range(int(op -1), 0, -1):
        op *= i
    binomio = n / (p * (op))
    print(f"Binômio de N e P: {binomio}")
else:
    print("P é maior que N! Não é possível calcular.")
    
