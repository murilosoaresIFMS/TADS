"""Para descobrir o peso ideal de uma pessoa, calcula-se o Índice de Massa Corporal (IMC) utilizando a seguinte fórmula: imc=peso/altura 
2
 . Dados o peso e a altura de uma pessoa, de acordo com a tabela a seguir, qual é o seu IMC e a sua condição atual?
Condição	IMC em mulheres	    IMC em homens
Abaixo do peso	IMC<19.1	      IMC<20.7
No peso ideal	19.1≤IMC<25.8	  20.7≤IMC<26.4
Acima do peso	25.8≤IMC	       26.4≤IMC"""

genero = input("Digite seu gênero: (F ou M) - ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura

if genero == "M": 
    if imc < 20.7:
        print("Você está abaixo do peso!")
    if imc <= 20.7:
        print("Você está no peso ideal")
    elif imc < 26.4:
        print("Você está no peso ideal")
    if imc <= 26.4:
        print("Você está acima do peso!")
        

