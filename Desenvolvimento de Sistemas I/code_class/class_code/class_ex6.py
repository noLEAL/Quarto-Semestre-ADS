"""
Questão 17. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
 Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
size = float(input("Informe o tamanho do arquivo em MB:"))

speed = float(input("Informe a velocidade do link em Mbps:"))

result = (size / (speed / 8)) / 60

print("{:.3f}".format(result))