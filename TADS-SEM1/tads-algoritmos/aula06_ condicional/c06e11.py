"""Dado o código de determinado produto, qual a sua classificação? Utilize a seguinte tabela de referência:
Código	Classificação
1	        Alimento não perecível
2, 3 ou 4	Alimento perecível
5 ou 6	    Vestuário
7	        Higiene pessoal
8 até 15	Limpeza e utensílios domésticos
Qualquer 	Inválido"""

codigo = int(input("Digite o código de produto: "))

if codigo == 1:
    print("Alimento não perecível")    
elif codigo == 2:
    print("Alimento perecível")
elif codigo == 3:
    print("Alimento perecível")
elif codigo == 4:
    print("Alimento perecível")
elif codigo == 5:
    print("Vestuário")
elif codigo == 6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene Pessoal")
elif codigo == 8:
    print("Limpeza e utensílios domésticos")
elif codigo == 9:
    print("Limpeza e utensílios domésticos")
elif codigo == 10:
    print("Limpeza e utensílios domésticos")
elif codigo == 11:
    print("Limpeza e utensílios domésticos")
elif codigo == 12:
    print("Limpeza e utensílios domésticos")
elif codigo == 13:
    print("Limpeza e utensílios domésticos")
elif codigo == 14:
    print("Limpeza e utensílios domésticos")
elif codigo == 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido")



