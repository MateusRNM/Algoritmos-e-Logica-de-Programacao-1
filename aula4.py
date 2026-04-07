while True:
    option = input()
    match option:
        case "novo":
            print("Novo documento")
        case "salvar":
            print("Salvar documento")
        case "sair":
            break
        case _:
            print("Opção inválida")