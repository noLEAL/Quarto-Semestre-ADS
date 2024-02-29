"""
Questão 9. Faça um Programa que peça a temperatura em graus Fahrenheit,
 transforme e mostre a temperatura em graus Celsius.C = (5 * (F-32) / 9).
"""

Fahrenheit = float(input("Digite o valor da temperatura em fahrenheit:"))

celsius = (5 * (Fahrenheit - 32) / 9)

print(f"sua temperatura é:{celsius}Cº")