"""No código do exercício anterior, modifique o setter de
forma que não seja permitido armazenar um valor
negativo para a idade"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property # Acessar atributo privado como se fosse público
    def age(self):
        return self.__age

    @age.setter # Alterar atributo privado como se fosse público
    def age(self, age):
        if age > 0:
            self.__age = age

stud = Student('Vanessa', 19)
print('Name:', stud.name, stud.age) # obtém idade usando getter
stud.age = 1 # altera idade usando setter
print('Name:', stud.name, stud.age) # obtém idade usando getter