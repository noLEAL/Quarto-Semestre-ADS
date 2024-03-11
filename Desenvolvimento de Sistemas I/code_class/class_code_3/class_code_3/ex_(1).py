#Questão 19. Faça uma função que lê 50 valores inteiros e retorna o maior e o menor deles.


def retorna_maior_menor():

    valores = []

    for x in range(1, 6):
        valores.append(int(input("Digite os valores:")))

    return print(f"Maior valor:{max(valores)}, Menor valor:{min(valores)}")

retorna_maior_menor()