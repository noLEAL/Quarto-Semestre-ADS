#Questão 10. Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

import math

nr1 = int(input("Informe um nuemro inteiro:"))
nr2 = int(input("Informe um numero inteiro:"))

nreal = float(input("Informe un numero real:"))


result = ((nr1*2)+(nr2/2))+((nr1*3)+nreal)+(nreal**3)

print(result)


