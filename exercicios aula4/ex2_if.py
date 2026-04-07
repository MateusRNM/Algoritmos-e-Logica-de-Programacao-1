origem = int(input("Digite o código de origem: "))
if origem == 1:
    print("Sul")
elif origem == 2:
    print("Norte")
elif origem == 3:
    print("Leste")
elif origem == 4:
    print("Oeste")
elif origem <= 6:
    print("Nordeste")
elif origem <= 9:
    print("Sudeste")
elif origem <= 20:
    print("Centro-Oeste")
elif origem <= 30:
    print("Nordeste")
else:
    print("Sem origem válida")