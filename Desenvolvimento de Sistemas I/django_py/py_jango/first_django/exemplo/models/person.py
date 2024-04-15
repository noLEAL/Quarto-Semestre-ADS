from exemplo.models.base import *


class Person(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Full name',
                            help_text='Nome da pessoa')
    birth = models.DateField(help_text='Data de nascimento', verbose_name='Birth date')
    cpf = models.CharField(max_length=100, verbose_name='CPF number',
                           help_text='CPF da pessoa')

    def __str__(self):
        to_string = f'Nome:{self.name} - CPF:{self.cpf}'
        return to_string
