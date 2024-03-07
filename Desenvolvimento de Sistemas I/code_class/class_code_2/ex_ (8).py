"""
Questão 8. Faça um programa que mostra na tela os números de 50 até 5 e mostra os valores
ímpares.
"""
nr1 = 50
x = nr1
aux = 0
result = 0

while x > 4:

    if x % 2 != 0:
        print(f"{x} - é impar")
        result = result + x
    else:
        print(f"{x}")

    x = x -1

print(f"Seu resultado é:{result}")