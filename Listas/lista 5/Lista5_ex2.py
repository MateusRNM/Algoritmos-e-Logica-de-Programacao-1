def depositar(saldo, valor):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return saldo
    return saldo + valor

def sacar(saldo, valor):
    if valor <= 0:
        print("Valor inválido para saque.")
        return saldo
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo
    return saldo - valor

saldo = 0
while True:
    print("1 - Ver Saldo\n2 - Depositar\n3 - Sacar\n4 - Sair")
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        print(f"Saldo atual: {saldo}")
    elif op == 2:
        saldo = depositar(saldo, float(input("Digite o valor do depósito: ")))
        print(f"Saldo: {saldo}")
    elif op == 3:
        saldo = sacar(saldo, float(input("Digite o valor do saque: ")))
        print(f"Saldo: {saldo}")
    elif op == 4:
        break
    else:
        print("Opção inválida.")