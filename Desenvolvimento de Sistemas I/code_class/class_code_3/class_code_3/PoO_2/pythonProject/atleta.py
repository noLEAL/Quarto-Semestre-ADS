
from datetime import datetime


class Atleta():
    """Classe atecla que permite criar proficional para diferentes esportes"""
    def __init__(self, name, birth_date, sport, responsible=None):
        try:
            birth_date = datetime.fromisoformat(birth_date)
            if ((datetime.today() - birth_date).days / 365.25) < 18:
                if responsible is None:
                    raise TypeError("Responsible")
            self.nome = name
            self.esporte = sport
            self.nascimento = birth_date
            self.responsavel = responsible

        except Exception as e:
            raise e

        def __str__(self):
            """Metodo padrão para retorno de informaçoes sobre um atleta"""
            if self.responsavel is None:
                return f"{self.nome}: {self.esporte}"
            else:
                return f"{self.nome} ({self.responsavel}):{self.esporte}"
