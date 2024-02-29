"""
Questão 35. Elabore um algoritmo que converta um valor em dólar (U$) para real (R$). O
 algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares a ser
 convertida.
"""

dolar = float(input("Digite o valor"))

cotacao = float(input("Digite o valor da cotação"))

real = dolar / cotacao

print(f"Valor em reais é:{real:.2f}")


