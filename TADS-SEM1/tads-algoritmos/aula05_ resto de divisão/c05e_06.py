# 6. Dado um dia juliano, qual é a data correspondente?
diaJuliano = float(input("Digite o dia juliano: "))

f = diaJuliano + 1401 + (4 * diaJuliano + 274277) / 146097 * 3/4 + (-38)
e = 4 * f + 3
g = e % 1461 / 4
h = 5 * g + 2

dia = (h % (153/5)) + 1
mes = (h / 153 + 2) % 12 + 1
ano = e / 1461 - 4716 + (12 + 2 - mes) / 12

print("Data: ", dia, "/", mes, "/", ano)

 

