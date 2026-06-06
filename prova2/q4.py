total_itens = 0
valor_total = 0
maiores_50 = 0
while(True):
    valor = float(input("Digite o valor da venda (0 para finalizar): "))
    if valor == 0:
        break
    elif valor > 50:
        maiores_50 += 1
    valor_total += valor
    total_itens += 1
print(f"Foram cadastrados {total_itens} itens, com um valor total de {valor_total}. A média de preço foi de {valor_total/(1 if total_itens == 0 else total_itens)} e há {maiores_50} produtos que custam mais de 50.")