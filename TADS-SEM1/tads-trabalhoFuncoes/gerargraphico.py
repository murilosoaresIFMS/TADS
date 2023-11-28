<<<<<<< HEAD
import matplotlib.pyplot as plt
import random as rd

# Função que retorna o cálculo de juros compostos (MONTANTE)
def jurosCompostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

capital = 1000 # Capital pré-fixado como R$ 1000

coresDoGrafico = ['b', 'c', 'g', 'r', 'm', 'y', 'k'] # Lista que contém os 'comandos' que passam cores para cada linha do gráfico ('b' = blue, por exemplo)
indiceCores = 0 # Índice que irá percorrer a lista 

print("=========== CÁLCULO DE JUROS COMPOSTOS ==============")

while (True):
    modalidade = input("Digite a modalidade de investimento ou 0 para encerrar: ")
    if (modalidade == '0'):
        break
    else:
        taxa = (float(input("Digite a taxa de juros correspondente ao modelo de investimento: ")) / 100) # Converte porcentagem para decimal diretamente na linha
        tempo = rd.randrange(1, 11) # Range entre 1 e 10 (referente aos anos de investimento)
        montantes = [jurosCompostos(capital, taxa, t) for t in tempo] 
        # A variável acima (montantes) utiliza um list 'Compreehension' para armazenar todos os montantes possíveis no limite de tempo (1 a 10):
        plt.plot(tempo, montantes, marker='o', linestyle='-', color= coresDoGrafico[indiceCores], label=f'{modalidade} (Taxa = {taxa:.2%})')
        indiceCores += 1
        print()

plt.xlabel('Anos Decorridos')
plt.ylabel('Montante Acumulado (R$)')
plt.title('Gráfico de Juros Compostos ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()
=======
import numpy as np
import matplotlib.pyplot as plt

# Função que retorna o cálculo de juros compostos (MONTANTE)
def jurosCompostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

capital = 1000 # Capital pré-fixado como R$ 1000

coresDoGrafico = ['b', 'c', 'g', 'r', 'm', 'y', 'k'] # Lista que contém os 'comandos' que passam cores para cada linha do gráfico ('b' = blue, por exemplo)
indiceCores = 0 # Índice que irá percorrer a lista 

print("=========== CÁLCULO DE JUROS COMPOSTOS ==============")

while (True):
    modalidade = input("Digite a modalidade de investimento ou 0 para encerrar: ")
    if (modalidade == '0'):
        break
    else:
        taxa = (float(input("Digite a taxa de juros correspondente ao modelo de investimento: ")) / 100) # Converte porcentagem para decimal diretamente na linha
        tempo = np.arange(1, 11) # Range entre 1 e 10 (referente aos anos de investimento)
        montantes = [jurosCompostos(capital, taxa, t) for t in tempo] 
        # A variável acima (montantes) utiliza um list 'Compreehension' para armazenar todos os montantes possíveis no limite de tempo (1 a 10):
        plt.plot(tempo, montantes, marker='o', linestyle='-', color= coresDoGrafico[indiceCores], label=f'{modalidade} (Taxa = {taxa:.2%})')
        indiceCores += 1
        print()

plt.xlabel('Anos Decorridos')
plt.ylabel('Montante Acumulado (R$)')
plt.title('Gráfico de Juros Compostos ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()
>>>>>>> 0da1ab61c89ffe1c5c9bb8bb1a29c8e3367cfd85
