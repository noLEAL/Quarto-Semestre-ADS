"""
Questão 46. Uma fabrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma
 sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário
 forneça a quantidade de camisetas pequenas, medias e grandes referentes a uma venda, e a
 maquina informe quanto será o valor arrecadado.
"""

qtd_small = int(input(f"Quantidade de camisetas Pequenas:"))
qtd_average = int(input(f"Quantidade de camisetas Media:"))
qtd_big = int(input(f"Quantidade de camisetas Grande:"))

print(f"Valor total da venda é:{(qtd_small * 10) + (qtd_average * 12) + (qtd_big * 15)}" )

