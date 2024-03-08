# Dado um natural menor que 10000, qual sua forma por extenso? Por exemplo, dado o número 9243, sua forma por extenso é "nove mil duzentos e quarenta e três".

n = int(input("Digite um número: "))

unidade = { 1: 'um', 
2: 'dois',
3: 'tres',
4: 'quatro',
5: 'cinco',
6: 'seis',
7: 'sete',
8: 'oito',
9: 'nove'         
}

dezenas = { 11: 'onze', 
12: 'doze',
13: 'treze',
14: 'quatorze',
15: 'quinze',
16: 'dezesseis',
17: 'dezessete',
18: 'dezoito',
19: 'dezenove'
}

dezenas2 = { 2: 'vinte',
3: 'trinta',
4: 'quarenta',
5: 'cinquenta',
6: 'sessenta',
7: 'setenta',
8: 'oitenta',
9: 'noventa',
}

centena = { 1: 'cento',
2: 'duzentos',
3: 'trezentos',
4: 'quatrocentos',
5: 'quinhentos',
6: 'seiscentos',
7: 'setecentos',
8: 'oitocentos',
9: 'novecentos'
}

i = 0

if (n > 999): 
    i = 4
if (n > 99 and n < 1000):
    i = 3 
if (n > 9 and n < 100):
    i = 2 

while (n != 0):

    if (n > 9999):
        print("Erro! Número inválido")
        break  

    if n > 1000: 
        if n == 1000:
            print('mil')
        else:
            divInteira = n // 1000
            print(unidade[divInteira] + ' mil', end = " ")

    n = n % (10 ** i) # Resto da divisão, para extrair os valores - centenas, dezenas e unidade

    if n > 99:
        if n == 100:
            print('cem')
        else:
            divInteira = n // (10 ** (i-1))
            print(centena[divInteira], end = " ")
    
    if n > 9 and n < 100:
        if n == 10:
            print('dez')
            break 
        if n > 10 and n < 20:
            print(dezenas[n])
            break
        if n >= 20 and n < 100: 
            divInteira = n // (10 ** (i - 1))
            print(dezenas2[divInteira], end = " ")

    if n > 0 and n <= 9:
        print(unidade[n])
    
    i -= 1

