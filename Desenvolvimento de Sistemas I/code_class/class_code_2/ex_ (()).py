#Questão 16. Faça um programa que mostra a soma dos valores de um intervalo informado pelo usuário (faça 2 programas, use FOR e WHILE).

nr1 = int(input("Ecolha o inicio do intervalo:"))

nr2 = int(input("Ecolha o fim do intevalo:"))

x = nr1
aux = 0
result = 0

while x < nr2+1:

    #print(f"{nr1 + aux}")

    result = result + (nr1 + aux)

    aux = aux + 1
    x = x + 1

print(f"a soma do intervalo é:{result}")


   