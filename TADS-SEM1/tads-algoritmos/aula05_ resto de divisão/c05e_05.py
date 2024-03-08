# 5. Dada uma data, qual é o seu dia juliano?

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
 
juliano = (1461 * (ano + 4800 + (mes - 14) / 12)) / 4 + (367 * (mes - 2 - 12) * ((mes - 14) / 12)) / 12 - (3 * (ano + 4900 + (mes - 14)/12)/100) / 4 + dia - 32075

print(juliano)
