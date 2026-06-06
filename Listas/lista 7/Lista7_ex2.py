entradas = []
arrecadado = 0
gasto = 0

while True:
    valor = float(input("Digite o valor da movimentação: "))
    if valor == 0:
        break
    entradas.append(valor)

for valor in entradas:
    if valor > 0:
        arrecadado += valor
    else:
        gasto += valor

print(f"Arrecadado: {arrecadado}\nDespesas: {gasto}\nSaldo: {arrecadado + gasto}\n {'Lucro' if arrecadado + gasto > 0 else 'Prejuízo'}")