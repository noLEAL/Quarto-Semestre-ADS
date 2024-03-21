import datetime


class Author():
    """Documentação da classe Author"""

    nome = ''
    data_nascimento = ''
    pseudonimo = ''

    def __init__(self, nome, data_nascimento, pseudonimo):
        self.nome = nome
        convet_datetime = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d")
        self.data_nascimento = convet_datetime
        self.pseudonimo = pseudonimo

    def __str__(self):
        to_string = f'Nome: {self.nome}\nData nascimento: {self.data_nascimento}\nPseudonimo: {self.pseudonimo}'
        return to_string
