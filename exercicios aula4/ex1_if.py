idade = int(input("Digite sua idade: "))
if idade > 30:
    print("Sênior")
elif idade >= 16:
    print("Adulto")
elif idade >= 11:
    print("Adolescente")
elif idade >= 8:
    print("Juvenil")
elif idade >= 5:
    print("Infantil")
else:
    print("Sem categoria")