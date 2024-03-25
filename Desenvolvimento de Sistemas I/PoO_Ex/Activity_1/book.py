import datetime
from gender import Gender


class Book():
    """Documentação da classe Book"""

    cod = ''
    titulo = ''
    resumo = ''
    isbn = ''
    publicacao = datetime
    genero = Gender

    def __init__(self, cod, titulo, resumo, isbn,genero):
        self.cod = cod
        self.titulo = titulo
        self.resumo = resumo
        self.isbn = isbn
        self.publicacao = datetime.date.today()
        self.genero = Gender()

    def __str__(self):
        to_string = f'Codigo: {self.cod}\nTitulo: {self.titulo}'
        to_string += f'\nResumo: {self.resumo}\nISBN: {self.isbn}'
        to_string += f'\nPublicacao: {self.publicacao}'
        return to_string
