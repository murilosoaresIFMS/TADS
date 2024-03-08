# 9. Joãozinho fez sua viagem até os Estados Unidos. Porém, chegando lá, descobriu que a temperatura é medida em graus Fahrenheit, e não em Celsius. Dada a temperatura em graus Fahrenheit, qual a temperatura correspondente em graus Celsius? C= 9(F−32)⋅5

temperaturaF = float(input("Digite a temperatura em Fahrenheit: "))

conversaoCelsius = 9 - (temperaturaF - 32) * 5

print("O valor de ", temperaturaF, "F° em Celsius é igual a ", conversaoCelsius, "C°")
