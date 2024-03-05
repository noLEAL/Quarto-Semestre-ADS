#Questão 3. Faça um programa que mostra na tela os números de 23 até 55 ->>>>>>>> mostra a soma dos valores.

nr1 = 23

nr2 = 55

x = 23

resultado = 0

while x < nr2+1:
    print(f"{x}")

    resultado = x + resultado

    x = x + 1

print(f"{resultado}")