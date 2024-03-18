# Questão 13. Faça uma função que recebe 3 valores inteiros por parâmetro e
# retorna-os ordenados em ordem crescente.

def orden_cresente(a: int, b: int, c: int):
    na = isinstance(a, int)
    nb = isinstance(b, int)
    nc = isinstance(c, int)

    if na and nb and nc:
        container = [a, b, c]
        sorted(container)
        return print(container)


orden_cresente(int(input("Informe o primeiro:")), int(input("Informe o segundo:")), int(input("Informe o terceiro:")))
