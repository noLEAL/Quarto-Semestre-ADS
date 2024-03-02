"""
Questão 70. Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
 prestação = valor + (valor * (taxa/100)*tempo)
 """

value = float(input("Valor da prestação:"))
tax = float(input("Taxa de atraso:"))
time = int(input("Meses atrasSO:"))

prestacao = value + (value * (tax/100)*time)

print(f"O valor :{prestacao}")