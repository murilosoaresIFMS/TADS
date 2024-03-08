# Dada a quantidade de estudantes da turma de Algoritmos, seguida pelas notas das provas de cada estudante, qual a maior nota e a média das notas dessa turma?

maior = 0
soma = 0
c = 0

quant = int(input("Digite a quantidade de estudantes da turma: "))
nota = int(input(f"Digite a nota do estudante: "))

while(c < quant-1): 
    soma = soma + nota 
    notaM = nota # Armazeno a nota antiga 
    nota = int(input(f"Digite a nota do estudante: ")) # Atualizo uma nova nota 
    if (notaM > nota):
        if(notaM > maior): # Comparo a nota antiga com a nova nota  # Comparo a nota antiga com o maior
            maior = notaM
    elif (nota > notaM):
        if(nota > maior):
            maior = nota 
    c += 1
media = soma / quant 

print(f"A média da classe é {media:.2f}")
print("A maior nota da classe foi ", maior)