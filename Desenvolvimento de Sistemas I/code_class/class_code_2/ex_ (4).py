"""
Questão 4. Faça um programa que mostra na tela a soma dos números pares de 1 até 50
    e mostra quantos números foram utilizados para calcular a soma.
"""

nr1 = 1

nr2 = 50

x = 0

result = 0

cont = 0

while x < 50:

    if nr1 % 2 == 0:
        print(f"{nr1}")
        result = result + nr1
        cont = cont + 1

    nr1 = nr1 + 1

    x = x + 1

print(f"A soma dos pares:{result} foram usados:{cont}")