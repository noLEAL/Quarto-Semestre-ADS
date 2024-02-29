"""
Questão 22. Um colega pediu dinheiro emprestado,
 você aceitou emprestar com a condição de que ele irá devolver o valor emprestado com juros de 15%.
 Qual o valor que o colega pediu e quanto ele irá devolver depois?
"""

loan = float(input("Digite o valor em reais a emprestar:"))

time = int(input("Tempo em messes para devolver:"))

result = float(loan * time * 0.15)

print("Valor a devolver:{:.3f}".format(result))