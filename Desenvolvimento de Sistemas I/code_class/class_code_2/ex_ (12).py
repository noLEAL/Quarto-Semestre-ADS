"""
Questão 12. Faça um programa que mostra os números entre 121 e 201 de 4 em 4 (usando FOR
ou WHILE).
"""
print("FOR:")
for x in range(121, 201, 4):
    print(x)

print("WHILE:")

nr1 = 121
y = nr1
while y < 201:
    print(nr1)
    nr1 = nr1 + 4
    y = y + 4

