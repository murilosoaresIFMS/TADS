# 7. Dado um dia juliano, qual é o dia da semana?

diaJuliano = int(input("Digite o dia da semana: "))

diaSemana = (diaJuliano + 1) % 7

print("O dia da semana é o dia", diaSemana)