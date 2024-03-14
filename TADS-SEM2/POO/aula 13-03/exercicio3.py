"""Implemente a classe Cadastro que representa um
perfil de usuário com atributos login e senha.
O login deve ter entre 5 e 15 caracteres, e a senha
deve ter no mínimo 8 caracteres.
Ambos os atributos devem ser privados e a classe
deve implementar getters e setters através de
propriedades."""

class Cadastro:

    def __init__(self, login, senha):
        self.login = login # vai chamar o setter
        self.senha = senha # vai chamar o setter

    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
     
    @login.setter
    def login(self, valor):
        if len(valor) >= 5 and len(valor) <= 15:
            self.__login = valor
        else:
            print('Valor inválido ')

    @senha.setter
    def senha(self, valor):
        if len(valor) >= 8:
            self.__senha = valor 
        else:
            print('Valor inválido ')

c1 = Cadastro('Murilo', '123')

print(c1.login, c1.senha)
c1.login = 'a' # Executa o setter
print(c1.login, c1.senha)