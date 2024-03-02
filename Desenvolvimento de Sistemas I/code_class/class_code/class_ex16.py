"""
Questão 54. Escreva um algoritmo para ler o salário mensal e o percentual de reajuste. Calcular e
 escrever o valor do novo salário.
"""

salary = float(input("Informe o valor do salrio:"))

readjustment = float(input("Informe o percentual de reajuste:"))

result = salary + (salary * (readjustment / 100))

print(f"O valor do salario:{result}")