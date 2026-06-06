for i in range(5):
    codigo = int(input("Digite o código: "))
    if codigo == 2024:
        print(f"Cofre Aberto em {i+1} tentativas.")
        break
    elif codigo > 2024:
        print("A senha digitada é numericamente maior do que o correto.")
    else:
        print("A senha digitada é numericamente menor do que o correto.")
else:
    print("Acesso Bloqueado")