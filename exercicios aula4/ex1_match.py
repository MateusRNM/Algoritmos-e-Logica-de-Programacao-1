idade = int(input("Digite sua idade: "))
match idade:
    case i if i > 30:
        print("Sênior")
    case i if i >= 16:
        print("Adulto")
    case i if i >= 11:
        print("Adolescente")
    case i if i >= 8:
        print("Juvenil")
    case i if i >= 5:
        print("Infantil")
    case _:
        print("Sem categoria")