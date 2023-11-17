print('\t\tCalcular juro composto\n')

Capital = input('Insira o valor do capital inicial:  ')
Taxa = input('Insira o valor da taxa em %:  ')
Tempo = input('Insira o valor do Tempo:  ')

Capital = float(Capital)

for i in range(0, len(Taxa)):
    if Taxa[i] == "%":
        Taxa = Taxa.replace(Taxa[i], "")

Taxa = float(Taxa)
Taxa = Taxa/100
Tempo = float(Tempo)

print('\nUsando uma fórmula onde C = Capital, i = taxa, t = tempo e M = Montante')
print('M = C*(1+i)^t')

Montante = (Capital*(1-Taxa)**Tempo)

print(f'\nM = {Capital}*(1 + {Taxa})^{Tempo}')
print(f'M = {Capital}*({1+Taxa})^{Tempo}')
print(f'M = {Capital}*{(1+Taxa)**Tempo}')
print(f'\nMontante = {Capital*(1+Taxa)**Tempo}')

_ = input("Pressione 'Enter' para encerrar o programa...")