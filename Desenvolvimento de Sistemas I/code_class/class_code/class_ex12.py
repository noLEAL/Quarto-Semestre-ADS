#Questão 37. Elabore um algoritmo que lê o raio de um círculo e mostre como saída o perímetro e a área.

import math

ray = float(input("Digite o valor do raio:"))

perimetro = 2 * math.pi * ray

area = math.pi * ray**2

print(f"Perimetro:{perimetro:.2f}")
print(f"Area:{area:.2f}")
