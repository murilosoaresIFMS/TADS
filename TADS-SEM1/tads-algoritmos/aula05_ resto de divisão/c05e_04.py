# 4. Dado um número inteiro representando um tempo em segundos, qual é o tempo em horas, minutos e segundos?

tempo = int(input("Digite o tempo em segundos: "))

conversaoSegundo = tempo % 60
conversaoMinuto = (tempo // 60) % 60
conversaoHora =  ((tempo // 60) // 60)

print(conversaoHora, conversaoMinuto, conversaoSegundo)
