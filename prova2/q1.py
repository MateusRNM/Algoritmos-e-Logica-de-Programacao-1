upper_lim = int(input("Digite o limite superior: "))
lower_lim = int(input("Digite o limite inferior: "))
soma = 0
qtd = 0
for i in range(upper_lim, lower_lim-1, -3):
    soma += i
    qtd += 1
print(soma/qtd if qtd > 0 else 0)