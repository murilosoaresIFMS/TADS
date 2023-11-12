"""Uma faculdade oferece um curso que prepara os candidatos a obter licença estadual para corretores de imóveis. No ano passado, dez estudantes que concluíram esse curso prestaram o exame. A universidade quer saber como foi o desempenho dos seus estudantes nesse exame. Você foi contratado para escrever um programa que resuma os resultados.
Ler o nome e o resultado de cada estudante, sendo o resultado um valor que indica se o estudante foi aprovado ou reprovado no exame. Escrever a quantidade de estudantes aprovados, a quantidade de reprovados, e se mais de oito estudantes foram aprovados, escrever “Bônus ao instrutor!”."""

c = 0
ap = 0
rep = 0

nome = input("Digite o nome do estudante (ou -1 para encerrar): ")
resultado = input("Digite o resultado do estudante (AP / REP) - (ou -1 para encerrar): ").lower()

while (c == 0):
    if (resultado == 'ap'): 
        ap += 1
        nome = input("Digite o nome do estudante: ")
        resultado = input("Digite o resultado do estudante (AP / REP): ").lower()
    elif (resultado == 'rep'):
        rep += 1
        nome = input("Digite o nome do estudante: ")
        resultado = input("Digite o resultado do estudante (AP / REP): ").lower()
    elif (nome == '-1'):
            c += 1
    if (resultado == '-1'):
            c += 1

print(f"Quantidade aprovados: {ap}")
if (ap > 8):
    print("Bônus ao instrutor!")
print(f"Quantidade reprovados: {rep}")
        