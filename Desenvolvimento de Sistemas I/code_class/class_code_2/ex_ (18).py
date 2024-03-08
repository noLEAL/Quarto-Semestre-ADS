#Questão 90. Faça um programa que lê a altura de 10 pessoas e mostra a maior.

altura = []

aux = 0.0

for x in range(0,10):
    altura.append(float(input("Digite a altura:")))


for elemento in altura:

    if elemento > aux:
        aux = elemento

print(f"A maior autura é :{aux}")