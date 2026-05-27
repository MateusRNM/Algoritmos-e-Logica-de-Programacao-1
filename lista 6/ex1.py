pares = []
impares = []
for i in range(6):
    num = int(input("Digite um número: "))
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Foram digitados {len(pares)} números pares:")
for i in pares:
    print(i)

print(f"Foram digitados {len(impares)} números ímpares:")
for i in impares:
    print(i)