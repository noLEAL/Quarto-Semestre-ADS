import datetime

from country import Country
class Author():
    """Documentação da classe Author"""

    nome = ''
    data_nascimento = ''
    pseudonimo = ''
    pais = Country

    def __init__(self, nome : str, data_nascimento : str, pseudonimo : str, pais):
        self.nome = nome
        convet_datetime = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d")
        self.data_nascimento = convet_datetime
        self.pseudonimo = pseudonimo
        self.pais = pais

    def __str__(self):
        to_string = f'Nome: {self.nome}\nData nascimento: {self.data_nascimento}\nPseudonimo: {self.pseudonimo}'
        return to_string
