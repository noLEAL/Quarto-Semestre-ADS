"""
Questão 35. Faça um algoritmo para ler dois valores (valide para que o segundo valor seja maior
que o primeiro), mostrar os valores existentes entre os dois valores lidos.
"""

nr1 = int(input("Informe o primeiro valor:"))
nr2 = int(input("Informe o segundo valor:"))

if nr1 > nr2:
    print("VALOR VALIDADO")

    for x in range(nr1,nr2):
        print(f"{x}")

else:
    print("VALOR INVALIDO")
    print("Primeiro valor digitado foi menos que o segundo.")

