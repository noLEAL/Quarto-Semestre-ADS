#Questão 32. Entre com uma data e mostre a data no formato: DD/MM/ANO

date = input("Informe uma data: DDMMAAAA")

dia = date[:2:]
mes = date[2:4:]
ano = date[4:8:]

print(f"Formatada:{dia}/{mes}/{ano}")