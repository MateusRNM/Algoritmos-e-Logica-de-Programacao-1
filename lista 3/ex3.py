valores = []
for i in range(5):
    valores.append(int(input()))
valores.sort()
print(f"Valores em ordem crescente: {[valores[x] for x in range(5)]}")
print(f"Valores em ordem decrescente: {[valores[x] for x in range(4, -1, -1)]}")