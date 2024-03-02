"""
Questão 48. A fabrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de
 350 ml, garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada
 quantidade de cada formato, faca um algoritmo para calcular quantos litros de refrigerante ele
 comprou.
"""


lata = 0.35

garafinha = 0.62

garrfa = 2

compra_lata = int(input("Quantas latas deseja:"))

compra_garrafinha = int(input("Quantas garrafa de 600ml deseja:"))

compra_litro = int(input("Quantas garrafa de 2L deseja:"))

resultado = float((compra_litro * garrfa) + (compra_garrafinha * garafinha) + (compra_lata * lata))

print(f"Total de litros comprados: {resultado}")
