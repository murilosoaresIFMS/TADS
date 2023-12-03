import numpy as np
import matplotlib.pyplot as plt
from math import floor 

def jurosCompostos(capital, taxa, tempo):
    tempo *= 12
    taxa = (taxa / 12) / 100
    return floor(capital * ((1 + taxa) ** tempo))

def jurosCompostos_Aporte(capital, taxa, tempo, aporte):
    tempo *= 12
    taxa = (taxa / 12) / 100
    return floor((capital * ((1 + taxa) ** 1)) + (aporte * ((((1 + taxa) ** tempo) - 1) / taxa)))

tempo = np.arange(1, 13)
montante = [jurosCompostos_Aporte(1000, 8.24, t, 0) for t in tempo]
print(jurosCompostos(1000, 8.24, 1))
print(montante)