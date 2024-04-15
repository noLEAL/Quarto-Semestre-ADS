import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from imdb.models.base import *
from django.db import models


def validate_quantidade(value):

    receba = int(value)

    if receba >= 0:
        return receba
    else:
        raise ValidationError("O valor fornecido não é um número válido.")


class Imdb(BaseModel):
    """[ID] ; [titulo] ; [sinopse] ; [genero] ; [clasificacao] ; [quantidade_avaliacoes] ; [nota]"""

    DEFAULT = "Padrão"
    ACTION = "Ação"
    ADVENTURE = "Adventura"
    SCI_FI = "Ficçao"
    HORROR = "Horor"
    THRILLER = "Suspense"
    WAR = "Guerra"

    GENEROS = [
        (ACTION, "Ação"),
        (ADVENTURE, "Adventura"),
        (SCI_FI, "Ficçao"),
        (HORROR, "Horor"),
        (THRILLER, "Suspense"),
        (WAR, "Guerra"),
        (DEFAULT, "")
    ]

    titulo = models.CharField(max_length=100, help_text='[Titulo do filme aqui]', default="Sem titulo",
                              validators=[MinLengthValidator(1)])
    sinopse = models.CharField(max_length=500, help_text='[Sinipse do filme aqui]', default="Sem sinopse",
                               validators=[MinLengthValidator(10)])
    genero = models.CharField(choices=GENEROS, default=DEFAULT, max_length=15)
    clasificacao = models.CharField(max_length=10, default='padrao')
    quantidade_avaliacoes = models.IntegerField(validators=[MinValueValidator(0)],  default=0,
                                                help_text='quantidade de avaliacoes')
    nota = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(1)], default=00.00)
    duracao = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.time(0, 0, 0))
    popularidade = models.IntegerField(validators=[MinValueValidator(0)],  default=0,
                                       help_text='quantidade de popularidade')
    # espesificacoes = models.CharField(max_length=50, null=False, blank=False, min_lengh=5)
    # lancamento = models.DataField()

    # def __init__(self, titulo, sinopse, genero, clasificacao, quantidade_avaliacoes, duracao, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.titulo = titulo
    #     self.sinopse = sinopse
    #     self.genero = genero
    #     self.clasificacao = clasificacao
    #     self.quantidade_avaliacoes = quantidade_avaliacoes
    #     self.duracao = duracao

    class Meta:
        abstract = False

    def __str__(self):

        to_string = f'Titulo: {self.titulo}\n Sinopse: {self.sinopse}\n Genero: {self.genero}\n'
        to_string += f' Clasificacao: {self.clasificacao}\n Quantidade de Avaliacoes: {self.quantidade_avaliacoes}\n'
        to_string += f' Nota: {self.nota}\n Duracao: {self.duracao}\n Popularidade: {self.popularidade}\n'
        return to_string
