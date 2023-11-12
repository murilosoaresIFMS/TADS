# Dado um natural, ele é primo?

n = int(input("Digite um número: "))
primo = True
divisor = 2 
meta = n / 2 

while divisor <= meta:
    if n % divisor == 0:
        primo = False
    divisor += 1

if n == 2:
    print("Sim")
elif primo:
    print("Sim")
else:
    print("Não")