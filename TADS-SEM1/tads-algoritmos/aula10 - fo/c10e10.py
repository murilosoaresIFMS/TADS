"""Dado um inteiro, qual o seu reverso? Exemplo de entrada→saída: 5837→7385."""

n = int(input("Digite um número: "))

print(f'Reverso de n:', end = ' ')
while n > 0:
    resto = n % 10 
    print(resto, end = '')
    n = n // 10 
