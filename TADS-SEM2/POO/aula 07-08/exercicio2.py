from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo 
        self.autor = autor

    @abstractmethod
    def informacoes():
        pass

class Livro(Publicacao):
    def __init__(self, titulo:str, autor:str, num_paginas:int):
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas

    def informacoes(self):
        return f'Livro: {self.titulo}, do autor(a) {self.autor} e com {self.num_paginas} páginas'
    
class Artigo(Publicacao):
    def __init__(self, titulo:str, autor:str, revista:str):
        super().__init__(titulo, autor)
        self.revista = revista

    def informacoes(self):
        return f'Artigo: {self.titulo}, do autor(a) {self.autor}, publicado na revista {self.revista}'
    
class Revista(Publicacao):
    def __init__(self, titulo:str, autor:str, edicao:int):
        super().__init__(titulo, autor)
        self.edicao = edicao

    def informacoes(self):
        return f'Revista: {self.titulo}, do autor(a) {self.autor} e da edição {self.edicao}'
    
livro = Livro('Harry Potter', 'JK Rowling', '260')
artigo = Artigo('Computadores', 'Murilo Soares', 'IF')
revista = Revista('Revistando', 'João Silva', '1')

print(livro.informacoes())
print(artigo.informacoes())
print(revista.informacoes())