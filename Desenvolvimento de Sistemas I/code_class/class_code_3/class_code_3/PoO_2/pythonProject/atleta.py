
from datetime import datetime


class Atleta():
    """Classe atecla que permite criar proficional para diferentes esportes"""
    numero_atletas = 0
    numero_responsavel = 0
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
            Atleta.numero_atletas += 1
            if self.responsavel is not None:
                Atleta.numero_responsavel += 1

        except Exception as e:
            raise e

    def __str__(self):
        """Metodo padrão para retorno de informaçoes sobre um atleta"""
        if self.responsavel is None:
            return f"{self.nome}: {self.esporte}"
        else:
            return f"{self.nome} ({self.responsavel}):{self.esporte}"

    def __del__(self):
        """Metodo destrutor que decrementa o contador"""
        if self.responsavel is not None:
            Atleta.numero_responsavel -= 1
        Atleta.numero_responsavel -= 1