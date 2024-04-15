from exemplo.models.base import *


class Passaport(BaseModel):
    number = models.CharField(max_length=100, verbose_name='Passaport number',
                              help_text='Número do passaporte', default='Sem numero')
    inssue_date = models.DateField(help_text='Data de emissão', verbose_name='Inssue date', default=None)
    expiration_date = models.DateField(help_text='Data de expiração', verbose_name='Expiration date', default=None)
    owner = models.OneToOneField('Person', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        to_string = f'Nome: {self.owner.name} - Número Passaport: {self.number} - Data Expedição: {self.inssue_date}'
        to_string += f' - Data Vencimento:{self.expiration_date}'
        return to_string
