def celsius_fahrenheit(c):
    return c * 9/5 + 32

def metros_cm(m):
    return m*100

while True:
    print("---- Menu interativo ----")
    print("Opção 1: Converter Celsius para Fahrenheit")
    print("Opção 2: Converter Metros para Centímetros")
    print("Opção 3: Sair")
    opc = int(input("Digite a opção: "))
    if opc == 1:
        print(celsius_fahrenheit(float(input("Digite os graus celsius: "))))
    elif opc == 2:
        print(metros_cm(float(input("Digite os metros: "))))
    elif opc == 3:
        break
    else:
        print("Opção inválida")