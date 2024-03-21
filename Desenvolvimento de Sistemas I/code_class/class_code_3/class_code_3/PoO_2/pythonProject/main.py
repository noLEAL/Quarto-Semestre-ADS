from atleta import Atleta

comissao = []

atleta_rugby = Atleta("Ricardo", "2001-10-20", "Rugby")
atleta_ping = Atleta("Carlos", "2010-10-15", "Ping Pong", "A Rua")
atleta_futebol = Atleta("Kannemann", "1980-05-15", "Futebol", "Geromel")
atleta_futebol2 = Atleta("George", "1990-03-02","Futebol")

comissao.append(atleta_rugby)
comissao.append(atleta_ping)
comissao.append(atleta_futebol)
comissao.append(atleta_futebol2)

comissao.remove(atleta_futebol)
del(atleta_futebol)


print("_______________Atletas proficionais Cadastro______________")
for atleta in comissao:
    print(atleta)
print("_______________Atletas proficionais Futebol______________")
for atleta in comissao:
    if atleta.esporte:
        if atleta.esporte == "Futebol":
            print(atleta)

print("__________Totais de pessoas na comissão__________")
print(f"Atletas {Atleta.numero_atletas}")
print(f"Responsaveis {Atleta.numero_responsavel}")
print(f"TOTAL: {Atleta.numero_atletas + Atleta.numero_responsavel}")

