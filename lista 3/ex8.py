n = int(input())
pares = []
impares = []
for i in range(n):
    num = int(input())
    if num & 1:
        impares.append(num)
    else:
        pares.append(num)
print(f"{len(pares)} pares digitados. Soma total: {sum(pares)}")
print(f"{len(impares)} ímpares digitados. Soma total: {sum(impares)}")