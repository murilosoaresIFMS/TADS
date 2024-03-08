import numpy as np
import matplotlib.pyplot as plt

# Função que retorna o cálculo de juros compostos (MONTANTE)
def jurosCompostos(capital, taxa, tempo, aporte):
    return (capital * (1 + taxa) ** tempo)

def jurosCompostosComAporteMensal(capital, taxa, tempo, aporteMensal):
    jurosCompostos = (capital * (1 + taxa) ** 1)
    valorMensal = aporteMensal * ((((1+taxa) ** (tempo)) - 1) / taxa)
    return jurosCompostos + valorMensal

capital = 1000 # Capital pré-fixado como R$ 1000
tempo = np.arange(1, 6) # Range entre 1 e 10 (referente aos anos de investimento)

coresDoGrafico = ['b', 'c', 'g', 'r', 'm', 'y', 'k'] # Lista que contém os 'comandos' que passam cores para cada linha do gráfico ('b' = blue, por exemplo)
indiceCores = 0 # Índice que irá percorrer a lista 

print("=========== CÁLCULO DE JUROS COMPOSTOS ==============")

while (True):
    modalidade = input("Digite a modalidade de investimento ou 0 para encerrar: ")
    if (modalidade == '0'):
        break
    else:
        taxa = (float(input("Digite a taxa de juros correspondente ao modelo de investimento: ")) / 100) # Converte porcentagem para decimal diretamente na linha
        aporte = input("Há a aplicação de aporte mensal? (sim / não)").lower()
        if (aporte == 'sim'):
            aporteMensal = float(input("Digite a quantidade de aporte mensal: "))
            montantes = [jurosCompostosComAporteMensal(capital, taxa, t, aporteMensal) for t in tempo]
        else:
            montantes = [jurosCompostos(capital, taxa, t, aporte) for t in tempo] 
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
