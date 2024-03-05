"""
Questão 50. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
 mostre-a expressa apenas em dias.
"""



dia = int(input("informe dias de vida:"))
mes = int(input("informe meses de vida:"))
ano = int(input("informe anos de vida:"))

resultado = (ano * 365 + mes * 30) + 2

print(f"você tem {resultado} dias de vida")

