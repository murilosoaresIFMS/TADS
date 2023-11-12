
"""Dado um natural no sistema decimal, qual seu equivalente no sistema binário? Para realizar a conversão do sistema decimal para binário, realiza-se a divisão sucessiva por 2. O resultado da conversão será dado pelo último quociente (MSB) e o agrupamento dos restos das divisões."""

n = int(input("Digite um número: "))

while n > 2: 
    resto = n % 2 
    print(resto, end = '')
    n = n // 2
    