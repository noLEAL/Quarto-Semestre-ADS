import random

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 32]

x = "Y"

while x.upper() == "Y":

    nr1 = random.randint(0, 200)

    if nr1 not in mylist:
        mylist.append(nr1)
        print(nr1)

        print(f"( Y ) - Sortear Proximo numero\n"
              f"( N ) - Encerrar programa\n")

        x = input("Informe opção desejada:")
    else:
        print(f"Numero sorteado ja foi escolhido.\n"
              f"( Y ) - Sortear Proximo numero\n"
              f"( N ) - Encerrar programa")

        x = input("Informe opção desejada:")
