# Exercício raíz quadrada

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

raizQuadrada = (b**2) - 4 * a * c 
bhaskara1 = (-b + (raizQuadrada ** 0.5)) / (2  * a) 
bhaskara2 = (-b - (raizQuadrada ** 0.5)) / (2  * a) 


if (a == 0):
    print("Não é equação de segundo grau!")
elif (raizQuadrada < 0):
    print("Não existe raíz!")
elif (raizQuadrada == 0):
    print("Raiz única")
else:
    print("X1 = ", bhaskara1, "X2 = ", bhaskara2)