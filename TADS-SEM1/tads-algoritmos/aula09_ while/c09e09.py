n = int(input("Digite um número: "))
c = 0

while(n > 1): 
    d = n / 10
    n = d
    c += 1

print(f"O número digitado possui {c+1} digitos")