a = []
b = []

for i in range(6):
    a.append(float(input(f"Digite o número {i} da lista A: ")))

for i in range(6):
    b.append(float(input(f"Digite o número {i} da lista B: ")))
    a[i] += b[i]

print(a)