
time_coracao = str.lower(input("Digite o time coracao do coracao"))

match time_coracao:
    case "gremio":
        print("gremio")
    case "inter":
        print("inter")
    case "juventude":
        print("juventude")
    case _:
        print("time não avaliado")