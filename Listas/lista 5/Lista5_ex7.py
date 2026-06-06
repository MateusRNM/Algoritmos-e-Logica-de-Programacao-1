numeros = []
while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida.")
print(f"Média dos números: {sum(numeros) / len(numeros) if len(numeros) > 0 else 0}\nMaior número: {max(numeros) if len(numeros) > 0 else 0}\nMenor número: {min(numeros) if len(numeros) > 0 else 0}")