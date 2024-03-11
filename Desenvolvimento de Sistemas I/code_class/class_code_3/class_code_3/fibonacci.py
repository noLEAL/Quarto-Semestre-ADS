#bibilioteca TK
#bibiliteca QT
def fibonacci(posicao):
    """função quer permite gerar a sequencia fibonacci de forma recursiva.
     Imprime o n-esimo (posição) numero da sequencia"""

    if posicao == 0 or posicao == 1:
        return 1
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)

for x in range(1,40):
    print("A possicao {} da sequencia fibonacci é {}".format(x, fibonacci(x)))