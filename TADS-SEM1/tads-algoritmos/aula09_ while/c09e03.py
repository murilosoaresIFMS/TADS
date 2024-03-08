# Dado um natural n, qual a soma dos pares entre 1 e n?

# 1. Ler um valor natural  
    #1.1 - Inicializar variável soma com 0
# 2. Retirar dele todos os pares
    #2.1 - Estrutura de repetição para diminui-lo de 1 em 1 
    #2.2 - Testar se o valor novo é par ou ímpar 
    #2.3 - Se for par, somá-lo com soma
# 3. Exibir a soma

soma = 0

n = int(input("Digite um número natural: "))

while(n > 0):
    if (n % 2 == 0):
        soma = n + soma 
    n -= 1

print('Soma dos pares entre 1 e 8 ', soma)
