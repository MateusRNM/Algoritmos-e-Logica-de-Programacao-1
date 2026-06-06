origem = int(input("Digite o código de origem: "))
match origem:
    case o if o == 1:
        print("Sul")
    case o if o == 2:
        print("Norte")
    case o if o == 3:
        print("Leste")
    case o if o == 4:
        print("Oeste")
    case o if o <= 6:
        print("Nordeste")
    case o if o <= 9:
        print("Sudeste")
    case o if o <= 20:
        print("Centro-Oeste")
    case o if o <= 30:
        print("Nordeste")
    case _:
        print("Sem origem válida")