from django.core.validators import MinValueValidator

from exemplo.models.base import *

class Example(BaseModel):
    nome = models.CharField(max_length=200,
                            help_text='Nome da pessoa')
    torcedores = models.IntegerField(default=0,
                                     help_text='Número de tocedores',
                                     validators=[MinValueValidator(0)])

    class Meta:
        pass

    def __str__(self):
        return f"{self.nome} - {self.torcedores}"
