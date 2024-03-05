GASOLINA = 5.58
ALCOOL = 3.42
valor = 0.0

nome = input("Digite seu nome completo:")

print(f"Ola {nome}!!!")

compustivel = input("Digite G - Gasolina ou A - Alcool")
quantidade = float(input("Digite a quantidade de litros:"))

if compustivel == "G":

    aditivo = input("C - Comum ou A - aditivada")

    if aditivo == "A":
        valor = quantidade * 5.77
    else:
        valor = quantidade * GASOLINA

else:
    valor = quantidade * ALCOOL

print(f"Valor total a ser pago em R$:{valor:.2f}")