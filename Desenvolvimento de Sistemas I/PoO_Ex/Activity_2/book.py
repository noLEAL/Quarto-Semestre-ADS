import datetime


class Book():
    """Documentação da classe Book"""

    cod = ''
    titulo = ''
    resumo = ''
    isbn = ''
    publicacao = datetime

    def __init__(self, cod, titulo, resumo, isbn):
        self.cod = cod
        self.titulo = titulo
        self.resumo = resumo
        self.isbn = isbn
        self.publicacao = datetime.date.today()

    def __str__(self):
        to_string = f'Codigo: {self.cod}\nTitulo: {self.titulo}'
        to_string += f'\nResumo: {self.resumo}\nISBN: {self.isbn}'
        to_string += f'\nPublicacao: {self.publicacao}'
        return to_string
