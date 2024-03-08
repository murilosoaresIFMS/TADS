# Dado um natural, quais seus divisores? Por exemplo, os divisores de 90 são 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90.

n = int(input("Digite um número: "))

print(f"Divisores: ", end = '')
for i in range(1, n+1):
    if n % i == 0:
        print(i, end = ' ')
        