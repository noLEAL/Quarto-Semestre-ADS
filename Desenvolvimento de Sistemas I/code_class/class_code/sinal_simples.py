nome = input('Digite seu nome: ')

print(f"Ola {nome}!!!")

nr1 = int(input("Digite o primeiro"))
nr2 = int(input("Digite o segundo"))

soma = nr1 + nr2

print(f"O resultado é: {soma}")

if nr1 > nr2:
    print(f"O primeiro é maior que o segundo.")
if nr2 > nr1:
    print(f"O segundo é maior que o segundo.")
if nr1 == nr2:
    print(f"Os numeros são iguais.")