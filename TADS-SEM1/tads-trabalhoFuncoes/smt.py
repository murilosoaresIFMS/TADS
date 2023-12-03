import math
import numpy as np


def juros_Compostos_Aporte(capital, tempo, taxa = 8.17, aporte = 300):
    tempo *= 12
    taxa = (taxa / 12) / 100 # Taxa mensal, decimal
    return math.floor((capital * ((1 + taxa) ** 1)) + (aporte * ((((1 + taxa) ** tempo) - 1) / taxa)))     

tempo2 = 5
tempo = np.arange(0, tempo2 + 1)
montante = [juros_Compostos_Aporte(1000, t) for t in tempo]
print(montante)



