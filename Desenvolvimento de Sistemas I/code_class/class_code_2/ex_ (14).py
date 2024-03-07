#Questão 32. Faça um programa que calcula a tabuada de um número.


entrada = int(input("Informe o valor que deseja a tabuada:"))

print(f"Tabuada do {entrada}")
for i in range(0,11):
    print(f"{entrada} X {i} = {entrada*i}")