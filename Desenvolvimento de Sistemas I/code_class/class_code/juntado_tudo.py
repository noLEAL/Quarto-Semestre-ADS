
flag = True
while flag:
    try:

        x = 0
        fim = int(input("digite ate que numero vc gostaria de contar(digite numero negativos para sair)"))

        while x <= fim:
            print(x)
            x = x + 1
        if fim < 0:
            flag = False
    except:
        print("erro no numero negativo")