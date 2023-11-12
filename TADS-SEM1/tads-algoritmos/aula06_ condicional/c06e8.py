# Dados três números representando os lados de um triângulo, ele é equilátero, isósceles ou escaleno? (como seria esse exercício sem o else?)

lado1 = int(input("Digite o tamanho do primeiro lado de um triângulo: "))
lado2 = int(input("Digite o tamanho do primeiro lado de um triângulo: "))
lado3 = int(input("Digite o tamanho do primeiro lado de um triângulo: "))

if lado1 == lado2:
    if lado1 == lado3: 
        if lado2 == lado3:
            print("Triângulo equilátero")

if lado1 == lado2:
    if lado2 != lado3:
            print("Triângulo escaleno")

if lado2 == lado3:
    if lado3 != lado1:
            print("Triângulo escaleno")
            
if lado3 == lado1:
    if lado1 != lado2:
            print("Triângulo escaleno")
            
if lado1 != lado2:
    if lado2 != lado3:
        print("Triângulo equilátero")
