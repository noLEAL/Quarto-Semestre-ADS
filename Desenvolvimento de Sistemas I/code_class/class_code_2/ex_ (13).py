"""
Questão 18. Faça um programa que mostra a soma dos valores pares, onde o intervalo considera
o valor 1 até um valor que será informado pelo usuário.
"""

nr1 = int(input("Informe o fim do intervalo:"))

result = 0

x = 1

for x in range(x,nr1):
    if x % 2 == 0:
        print(f"{x} - par")
        result = result + x

print(f"Resultado é :{result}")