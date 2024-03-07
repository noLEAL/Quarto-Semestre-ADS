"""
Questão 7. Faça um programa que mostra na tela a soma dos números ímpares de 20 até 50 e
mostra o total de valores somados.
"""

nr1 = 20

nr2 = 50

x = 0

result = 0

cont = 0

while x < 50:

    if nr1 % 2 != 0:
        print(f"{nr1}")
        result = result + nr1
        cont = cont + 1

    nr1 = nr1 + 1

    x = x + 1

print(f"A soma dos inpares:{result} foram usados:{cont}")