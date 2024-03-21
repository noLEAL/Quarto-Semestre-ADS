class Publisher():

    cod = ''
    razao_social = ''
    nome_fantasia = ''
    email = ''

    def __init__(self, cod, razao_social, nome_fantasia, email):
        self.cod = cod
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.email = email

    def __str__(self):
        to_string = f'Codigo: {self.cod}\nRazao social: {self.razao_social}'
        to_string += f'Nome fantasia: {self.nome_fantasia}\nEmail: {self.email}'