"""
Questão 86. Elabore um algoritmo que depois de ler uma sequência de N números (N deve ser
    solicitado para o usuário), mostre os seguintes resultados:
    a) o maior valor
    b) o menor valor
    c) a soma dos valores
    d) a média dos valores
    e) quantos números maiores a 20
    f) a percentagem de valores maiores que 10
    g) a média dos valores entre 10 e 100
"""

n = int(input("Digite o N de números que deseja:"))

for x in range(1,n+1):
    arm = float(input("Digite o número:"))

